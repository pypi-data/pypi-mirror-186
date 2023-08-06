# Copyright (c) Qotto, 2022

from __future__ import annotations

import dataclasses
import re
import typing
from dataclasses import dataclass
from enum import Enum
from typing import Union, Optional

__all__ = [
    'Namespace',
    'Matching',
    'Application',
    'Permission',
    'Organization',
    'Authorization',
    'Role',
    'User',
    'Member',
    'Actor',
    'Account',
    'Cookie',
    'Identity',
    'UserRequest',
    'CookiePair',
    'TokenInfo',
]


class Matching(Enum):
    ALL = 'ALL'
    EXACT = 'EXACT'
    ASCENDANT = 'ASCENDANT'
    DESCENDANT = 'DESCENDANT'
    SAME_BRANCH = 'SAME_BRANCH'

    def __str__(self) -> str:
        return self.name


class Namespace:
    _nodes: list[str]

    def __init__(
            self,
            nodes: Union[str, list[str]],
    ) -> None:
        """
        >>> Namespace('a:::b  :c:d')
        a:b:c:d
        >>> Namespace(['a', '  b  ', 'c', '', '', 'd'])
        a:b:c:d
        >>> Namespace(['a:', 'b', 'c', 'd'])
        Traceback (most recent call last):
            ...
        ValueError: A node cannot contain colons ":".
        >>> Namespace(['a', 1, 'c', 'd'])
        Traceback (most recent call last):
            ...
        TypeError: A node must be a str.
        >>> Namespace('')
        Traceback (most recent call last):
            ...
        ValueError: Namespace must have at least one node.
        """
        if isinstance(nodes, str):
            nodes = list(filter(len, (v.strip().lower() for v in nodes.split(':'))))
        elif isinstance(nodes, list):
            if any(filter(lambda x: not isinstance(x, str), nodes)):
                raise TypeError("A node must be a str.")
            if any(filter(lambda x: ':' in str(x), nodes)):
                raise ValueError("A node cannot contain colons \":\".")
            nodes = list(filter(len, (v.strip().lower() for v in nodes)))
        if not nodes:
            raise ValueError("Namespace must have at least one node.")
        for node in nodes:
            if not node:
                raise ValueError("Namespace node must not be empty.")
        self._nodes = nodes

    @property
    def path(self) -> str:
        return ':'.join(self._nodes)

    @property
    def nodes(self) -> list[str]:
        return self._nodes.copy()

    def matches(self, other: Namespace, matching: Matching = Matching.ALL) -> bool:
        """
        Test is self is <matching> of other.
        """
        if matching == Matching.ALL:
            return True
        if matching == Matching.EXACT:
            return self == other
        if matching == Matching.ASCENDANT:
            return self >= other
        if matching == Matching.DESCENDANT:
            return self <= other
        if matching == Matching.SAME_BRANCH:
            return self <= other or self >= other
        raise ValueError(f"Unknown matching type {matching}.")

    def __eq__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) == len(other)
                and self.path == other.path)

    def __hash__(self):
        return hash(self.path)

    def __le__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) >= len(other)
                and Namespace(self._nodes[:len(other)]) == other)

    def __ge__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) <= len(other)
                and Namespace(other._nodes[:len(self)]) == self)

    def __lt__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) > len(other)
                and Namespace(self._nodes[:len(other)]) == other)

    def __gt__(self, other) -> bool:
        return (isinstance(other, Namespace)
                and len(self) < len(other)
                and Namespace(other._nodes[:len(self)]) == self)

    def __len__(self) -> int:
        return len(self._nodes)

    def __str__(self) -> str:
        return self.path

    def __repr__(self) -> str:
        return self.path


_camel_pattern = re.compile(r"([a-zA-Z][^A-Z0-9]*|[0-9]+)")


def _camel_case(snake_case: str) -> str:
    components = snake_case.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def _snake_case(camel_case: str) -> str:
    components = _camel_pattern.findall(camel_case)
    return "_".join(component.lower() for component in components)


Self = typing.TypeVar("Self", bound="GqlData")


@dataclass(frozen=True)
class GqlData:
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        kwargs = dict()
        type_hints = typing.get_type_hints(cls)
        for field in dataclasses.fields(cls):
            field_name = field.name
            field_type = type_hints[field_name]
            value = None
            if field_name in data:
                value = data[field_name]
            elif _camel_case(field_name) in data:
                value = data[_camel_case(field_name)]
            else:
                continue
            if not isinstance(field_type, type):
                for optional_type in field_type.__args__:
                    if issubclass(optional_type, type(None)):
                        continue
                    field_type = optional_type
            if issubclass(field_type, GqlData) and value is not None:
                value = field_type.from_dict(value)
            elif issubclass(field_type, Matching):
                value = Matching(value)
            elif issubclass(field_type, Namespace):
                value = Namespace(value)
            kwargs[field_name] = value
        return cls(**kwargs)  # type: ignore

    def to_dict(self, capitalize: bool = True) -> dict:
        result = dict()
        for field in dataclasses.fields(self):
            field_name = field.name
            key = _camel_case(field_name) if capitalize else field_name
            value = getattr(self, field_name)
            if isinstance(value, GqlData):
                value = value.to_dict(capitalize)
            elif isinstance(value, Namespace):
                value = str(value)
            elif isinstance(value, Matching):
                value = value.value
            result[key] = value
        return result

    @classmethod
    def body(cls) -> str:
        result = list()
        type_hints = typing.get_type_hints(cls)
        for field in dataclasses.fields(cls):
            field_name = _camel_case(field.name)
            field_type = type_hints[field.name]
            result.append(field_name)
            if not isinstance(field_type, type):
                for optional_type in field_type.__args__:
                    if issubclass(optional_type, type(None)):
                        continue
                    field_type = optional_type
            if issubclass(field_type, GqlData):
                result.append('{ ' + field_type.body() + ' }')
        return ' '.join(result)

    def update(self, **kwargs) -> Self:
        data = self.to_dict()
        for k, v in kwargs.items():
            if isinstance(v, GqlData):
                v = v.to_dict()
            data[_camel_case(k)] = v
        return self.from_dict(data)


@dataclass(frozen=True)
class Application(GqlData):
    id: str
    name: str
    description: str


@dataclass(frozen=True)
class Permission(GqlData):
    id: str
    application: Application
    name: str
    description: str


@dataclass(frozen=True)
class Organization(GqlData):
    id: str
    name: str
    namespace: Namespace


@dataclass(frozen=True)
class Authorization(GqlData):
    id: str
    name: str
    description: str
    organization: Organization
    inheritance: bool
    matching: Matching


@dataclass(frozen=True)
class Role(GqlData):
    id: str
    name: str
    description: str
    organization: Organization
    inheritance: bool


@dataclass(frozen=True)
class Identity(GqlData):
    id: str
    name: str
    provider_id: str
    email: str
    user: Optional[User]
    user_request: Optional[UserRequest]
    blocked: bool


@dataclass(frozen=True)
class User(GqlData):
    id: str
    name: str
    is_superuser: bool


@dataclass(frozen=True)
class Member(GqlData):
    id: str
    user: User
    organization: Organization


@dataclass(frozen=True)
class Account(GqlData):
    id: str
    application: Application
    user: User
    enabled: bool
    data: dict


@dataclass(frozen=True)
class UserRequest(GqlData):
    id: str
    name: str
    comment: Optional[str] = None


@dataclass(frozen=True)
class Actor(GqlData):
    user: Optional[User] = None
    member: Optional[Member] = None


@dataclass(frozen=True)
class Cookie(GqlData):
    name: str
    value: str
    domain: str
    max_age: int
    secure: bool
    http_only: bool

    def __str__(self):
        return f'Cookie"{self.name}={self.value}"'


@dataclass(frozen=True)
class CookiePair(GqlData):
    token_cookie: Cookie
    secret_cookie: Cookie


@dataclass(frozen=True)
class TokenInfo:
    user_id: Optional[str] = None
    display_name: Optional[str] = None
    given_name: Optional[str] = None
    middle_name: Optional[str] = None
    family_name: Optional[str] = None
    email: Optional[str] = None
    is_superuser: Optional[bool] = None
    member_id: Optional[str] = None
    organization_id: Optional[str] = None
    organization_name: Optional[str] = None
    organization_namespace: Optional[str] = None
    applications: Optional[list[str]] = None
