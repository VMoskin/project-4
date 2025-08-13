from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(transaction_list: list, sorted_executed: list, sorted_canceled: list) -> None:
    assert filter_by_state(transaction_list) == sorted_executed
    assert filter_by_state(transaction_list, state="CANCELED") == sorted_canceled


def test_sort_by_date(transaction_list: list, sorted_list_date: list, sorted_list_date_rev: list) -> None:
    assert sort_by_date(transaction_list) == sorted_list_date
    assert sort_by_date(transaction_list, sort_rev=False) == sorted_list_date_rev
