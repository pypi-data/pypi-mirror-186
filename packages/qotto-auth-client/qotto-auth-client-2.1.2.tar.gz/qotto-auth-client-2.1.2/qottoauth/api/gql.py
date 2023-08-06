import logging
from typing import Any, Optional, Tuple
from urllib.parse import urljoin

from eventy.integration import requests
from eventy.trace_id import correlation_id_var, user_id_var
from gql import Client, gql
from gql.transport.exceptions import TransportQueryError, TransportServerError
from gql.transport.requests import RequestsHTTPTransport

from qottoauth.api.base import QottoAuthApi, QottoAuthApiError

__all__ = [
    'QottoAuthGqlApi',
]

logger = logging.getLogger(__name__)


class QottoAuthGqlApi(QottoAuthApi):
    def __init__(
            self,
            url: str,
    ):
        """
        :param url: Qotto Auth Backend URL
        """
        self.url = url

    def _graphql(
            self,
            query: str,
            variable_values: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Execute GraphQL query and return the result.

        :param query: The GraphQL query or mutation
        :param variable_values: The GraphQL params
        :return: The GraphQL response
        :raise QottoAuthError:
        """
        transport = RequestsHTTPTransport(
            url=self.url + '/graphql/',
            headers={
                'x-correlation-id': correlation_id_var.get(),
                'x-user-id': user_id_var.get(),
            },
        )
        client = Client(
            transport=transport,
        )
        try:
            result: dict[str, Any] = client.execute(
                gql(query),
                variable_values=variable_values,
            )
        except TransportQueryError as e:
            raise QottoAuthApiError('; '.join(map(str, e.errors)) if e.errors else 'Unknown error')
        except TransportServerError as e:
            logger.error(f"Transport error: {e.code} {e}")
            raise QottoAuthApiError(str(e))
        except ConnectionError as e:
            logger.error(f"Could not connect to server: {e}")
            raise QottoAuthApiError("Could not connect to Qotto Auth server.")

        if result.get('errors'):
            raise QottoAuthApiError(str(result.get('errors')))

        return result

    def query(
            self,
            name: str,
            variables: list[Tuple[str, str, Any]] = None,
            body: str = None,
    ):
        """
        Execute GraphQL query and return the result.

        :param name: GraphQL query name
        :param body: Body of the GraphQL query
        :param variables: List of (name, type, value) params
        :return: The GraphQL response
        """
        variable_values = {}
        query = ''
        if variables:
            variables_types = ', '.join(map(lambda x: f'${x[0]}: {x[1]}', variables))
            variable_values = dict(map(lambda x: (x[0], x[2]), variables))
            variables_names = ', '.join(map(lambda x: f'{x[0]}: ${x[0]}', variables))
            query += 'query ' + name + '(' + variables_types + ')' + ' {\n'
            query += '  ' + name + '(' + variables_names + ')'
        else:
            query += 'query ' + name + ' {\n'
            query += '  ' + name

        if body:
            query += ' {\n'
            query += '  ' + body + '\n'
            query += '   }\n'

        query += '}\n'
        return self._graphql(
            query=query,
            variable_values=variable_values,
        ).get(name)

    def mutation(
            self,
            name: str,
            body: str,
            input_name: str = 'input',
            input_type: str = None,
            input_value: dict[str, Any] = None,
    ):
        """
        Execute GraphQL mutation and return the result.

        :param name: GraphQL query name
        :param body: Body of the GraphQL query
        :param variables: List of (name, type, value) params
        :return: The GraphQL response
        """
        if input_type is None:
            input_type = name[:1].upper() + name[1:] + 'Input!'
        if input_value is None:
            input_value = {}
        variables = [
            (input_name, input_type, input_value),
        ]
        variables_types = ''
        variables_names = ''
        variable_values = {}
        if variables:
            variables_types = ', '.join(map(lambda x: f'${x[0]}: {x[1]}', variables))
            variable_values = dict(map(lambda x: (x[0], x[2]), variables))
            variables_names = ', '.join(map(lambda x: f'{x[0]}: ${x[0]}', variables))
        query = ''
        query += 'mutation ' + name + '(' + variables_types + ')' + ' {\n'
        query += '  ' + name + '(' + variables_names + ')' + ' {\n'
        query += '  ' + body + '\n'
        query += '   }\n'
        query += '}\n'
        return self._graphql(
            query=query,
            variable_values=variable_values,
        ).get(name)

    def auth_metadata(self) -> dict[str, str]:
        response = requests.get(url=urljoin(self.url, 'auth/metadata'))
        response.raise_for_status()
        return response.json()  # type: ignore
