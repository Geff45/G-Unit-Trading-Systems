from gunit.queries.query import Query
from gunit.queries.query_dispatcher import QueryDispatcher
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


def test_dispatcher_dispatches_query() -> None:

    registry = QueryRegistry()

    registry.register(
        UserQuery,
        UserHandler(),
    )

    dispatcher = QueryDispatcher(
        registry
    )

    result = dispatcher.dispatch(
        UserQuery()
    )

    assert result == "Atlas"