def filter_by_state(transactions: list, state: str="EXECUTED") -> list:
    """Функция сортирует список словарей по значению ключа 'state'"""
    new_transactions = []
    for transaction in transactions:
        for value in transaction.values():
            if value == state:
                new_transactions.append(transaction)
    return new_transactions


def sort_by_date(transaction_list: list, sort_rev: bool=True) -> list:
    """Функция сортирует список словарей по дате"""
    sorted_list = sorted(transaction_list, key=lambda x: x["date"], reverse=(sort_rev))
    return sorted_list


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
