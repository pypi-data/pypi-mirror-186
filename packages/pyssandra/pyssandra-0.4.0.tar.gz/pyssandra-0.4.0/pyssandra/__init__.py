"""Build Cassandra CQL queries from Pydantic models."""

from pyssandra._pyssandra import Pyssandra
from pyssandra._query_builder import QueryBuilder

__all__ = ("Pyssandra", "QueryBuilder")
