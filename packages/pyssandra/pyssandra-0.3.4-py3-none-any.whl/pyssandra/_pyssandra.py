"""Module to provide class to decorate models as tables."""
from typing import Callable, Type

from cassandra.cluster import Session

from pyssandra._query_builder import ModelType, QueryBuilder


class Pyssandra:
    """Class to register models as Cassandra Tables."""

    def __init__(self, session: Session, keyspace: str) -> None:
        """Init an instance of the Pyssandra class.

        :param session: Cassandra session to use.
        :param keyspace: Keyspace of the tables.
        """
        self._session = session
        self._keyspace = keyspace
        self._model_type_to_query_builder: dict[ModelType, QueryBuilder] = {}

    def __getitem__(self, item: Type[ModelType]) -> QueryBuilder[ModelType]:
        """Get a `QueryBuilder` for the given model.

        :param item: Model representing a table.
        :return: A `QueryBuilder` for the given model.
        """
        return self._model_type_to_query_builder[item]

    def table(self, keys: list[str]) -> Callable[[Type[ModelType]], Type[ModelType]]:
        """Register a model as a database table.

        :param keys: Table partition keys.
        :return: Wrapper for the decorated table.
        """

        def _wrapper(cls: Type[ModelType]) -> Type[ModelType]:
            query_builder = QueryBuilder(self._session, self._keyspace, cls, keys)
            self._model_type_to_query_builder[cls] = query_builder
            return cls

        return _wrapper
