import pytest

from src.widget import mask_account_card
from src.widget import get_date


@pytest.mark.parametrize('name_card, value_card', [
    ("Maestro 7000543267892582", "Maestro 7000 54** **** 2582"),
    ("Maestro 700054326789258", "Неверный номер карты"),
    ("Maestro 70005432678925k7", "Неверный номер карты"),
    ("Maestro 70005432678925855", "Неверный номер карты"),
    ("Maestro", "Неверный номер карты"),
    ("Visa Platinum 7000321065419873", "Visa Platinum 7000 32** **** 9873"),
    ("Счет 92345678987654326541", "Счет **6541"),
    ("Счет 9234567898765432654", "Неверный номер счета"),
    ("Счет 923456789876543265411", "Неверный номер счета"),
    ("Счет 9234567898765432654k", "Неверный номер счета"),
])
def test_mask_accound_card(name_card: str, value_card: str) -> None:
    assert mask_account_card(name_card) == value_card


def test_get_date() -> None:
    assert get_date("2024-03-12T02:26:18.671407") == "12.03.2024"
