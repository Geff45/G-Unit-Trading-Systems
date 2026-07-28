from gunit.queries.query import Query
from gunit.queries.query_builder import QueryBuilder
from gunit.queries.query_handler import QueryHandler


class UserQuery(Query):
    pass


class UserHandler(QueryHandler[UserQuery, str]):

    def handle(
        self,
        query: UserQuery,
    ) -> str:
        return "Atlas"


def test_builder_registers_handler() -> None:

    builder = QueryBuilder()

    registry = (
        builder
        .add(
            UserQuery,
            UserHandler(),
        )
        .build()
    )

    assert registry.contains(UserQuery)


def test_builder_returns_registry() -> None:

    builder = QueryBuilder()

    registry = builder.build()

    assert registry is builder.registry