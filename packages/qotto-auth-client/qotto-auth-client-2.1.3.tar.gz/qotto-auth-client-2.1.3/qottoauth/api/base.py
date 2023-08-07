import logging
from abc import ABC
from typing import Any, Tuple

__all__ = [
    'QottoAuthApi',
    'QottoAuthApiError',
]

logger = logging.getLogger(__name__)


class QottoAuthApiError(Exception):
    """
    Could not get a response from Qotto Auth API.
    """


class QottoAuthApi(ABC):
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
        raise NotImplementedError

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
        raise NotImplementedError

    def auth_metadata(self) -> dict[str, str]:
        """
        Get metadata from Qotto Auth server

        :return: Dictionary keys: token_cookie_name, token_public_key, token_algorithm, secret_cookie_name

        """
        raise NotImplementedError
