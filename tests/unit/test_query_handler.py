from gunit.queries.query import Query
from gunit.queries.query_handler import QueryHandler


class NumberQuery(Query):
    pass


class NumberHandler(QueryHandler[NumberQuery, int]):

    def handle(
        self,
        query: NumberQuery,
    ) -> int:
        return 100


def test_query_handler_returns_result() -> None:
    handler = NumberHandler()

    assert handler.handle(NumberQuery()) == 100