from gunit.queries.query import Query
from gunit.queries.query_handler import QueryHandler
from gunit.queries.query_registry import QueryRegistry


class UserQuery(Query):
    pass


class UserHandler(QueryHandler[UserQuery, str]):

    def handle(
        self,
        query: UserQuery,
    ) -> str:
        return "Atlas"


def test_registry_registers_handler() -> None:
    registry = QueryRegistry()

    registry.register(
        UserQuery,
        UserHandler(),
    )

    assert registry.contains(UserQuery)