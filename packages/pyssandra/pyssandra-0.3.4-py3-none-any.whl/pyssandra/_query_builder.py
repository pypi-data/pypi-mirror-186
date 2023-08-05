"""Build CQL queries from Pydantic models."""
import inspect
from typing import Generic, Optional, Type, TypeVar
from uuid import UUID

import caseswitcher
from cassandra.cluster import Session
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


# noinspection SqlNoDataSourceInspection
class QueryBuilder(Generic[ModelType]):
    """Class to build CQL queries."""

    def __init__(
        self,
        session: Session,
        keyspace: str,
        model_type: Type[ModelType],
        keys: list[str],
    ) -> None:
        """Init an instance the QueryBuilder class.

        :param session: Cassandra driver session.
        :param keyspace: Keyspace of the tables.
        :param model_type: Type of model this instance will manage.
        :param keys: Partition keys for this table.
        """
        self._session = session
        self._keyspace = keyspace or session.keyspace
        self._model_type = model_type
        self._keys = keys
        self._tablename = caseswitcher.to_snake(model_type.__name__)
        self._indent = " " * 2
        self._find_one_statement = self._session.prepare(self._get_find_one_query())
        self._insert_statement = self._session.prepare(self._get_insert_query())
        self._update_statement = self._session.prepare(self._get_update_query())

    async def find_one(self, key: UUID) -> Optional[ModelType]:
        """Get one record mapped to the appropriate model.

        :param key: The key of the record to retrieve.
        :return: A model representing the record if one is found.
        """
        result = self._session.execute(
            query=self._find_one_statement, parameters=[key]
        ).one()
        # noinspection PyProtectedMember
        return self._model_type(**result._asdict())

    async def insert(self, model: ModelType) -> None:
        """Insert a record from a model.

        :param model: Model representing row to insert.
        :return: None.
        """
        parameters = [model.__dict__[k] for k, v in model.__fields__.items()]
        self._session.execute(query=self._insert_statement, parameters=parameters)

    async def update(self, model: ModelType) -> None:
        """Update a record from a model.

        :param model: Model representing row to update.
        :return: None.
        """
        parameters = [
            model.__dict__[k]
            for k, v in model.__fields__.items()
            if k not in self._keys
        ] + [model.__dict__[k] for k in self._keys]
        self._session.execute(query=self._update_statement, parameters=parameters)

    def _get_find_one_query(self) -> str:
        where = f"\n{self._indent}AND ".join(f"{k} = ?" for k in self._keys)
        return inspect.cleandoc(
            f"""
            SELECT
              *
            FROM
              {self._keyspace}.{self._tablename}
            WHERE
              {{where}};
            """
        ).format(where=where)

    def _get_insert_query(self) -> str:
        columns = ",".join(self._model_type.__fields__)
        place_holders = ",".join(["?" for _ in range(len(self._model_type.__fields__))])
        return inspect.cleandoc(
            f"""
            INSERT INTO
              {self._keyspace}.{self._tablename} ({columns})
            VALUES
              ({place_holders});
            """
        )

    def _get_update_query(self) -> str:
        set_placeholders = f",\n{self._indent}".join(
            f"{c} = ?" for c in self._model_type.__fields__ if c not in self._keys
        )
        where = f"\n{self._indent}AND ".join(f"{k} = ?" for k in self._keys)
        return inspect.cleandoc(
            f"""
            UPDATE
              {self._keyspace}.{self._tablename}
            SET
              {{set_placeholders}}
            WHERE
              {{where}};
            """
        ).format(set_placeholders=set_placeholders, where=where)
