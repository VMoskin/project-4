import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize('number_card, value_card', [
    ('1111222233334444', "1111 22** **** 4444"),
    ('111122223333444', "Неверный номер карты"),
    ('1111222O33334444', "Неверный номер карты"),
    ('11112222333344445', "Неверный номер карты"),
    ('', "Неверный номер карты"),
])
def test_get_mask_card_number(number_card: int, value_card: str) -> None:
    assert get_mask_card_number(number_card) == value_card


@pytest.mark.parametrize('name_account, value_account', [
    ('11112222333344445555', "**5555"),
    ('1111222233334444555', "Неверный номер счета"),
    ('111122223333444455576', "Неверный номер счета"),
    ('1111222233334444555O', "Неверный номер счета"),
    ('1111222233334444555o', "Неверный номер счета"),
    ('', "Неверный номер счета")
])
def test_get_mask_account(name_account: int, value_account: str) -> None:
    assert get_mask_account(name_account) == value_account
