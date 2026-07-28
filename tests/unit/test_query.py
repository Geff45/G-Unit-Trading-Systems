from gunit.queries.query import Query


class TestQuery(Query):
    pass


def test_query_can_be_inherited() -> None:
    query = TestQuery()

    assert isinstance(query, Query)