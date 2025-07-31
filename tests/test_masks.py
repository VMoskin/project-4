from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number(1234567898765432) == '1234 56** **** 5432'
    assert get_mask_card_number(4567898765433) == 'Неверный номер карты'
    assert get_mask_card_number(1111234567898765432) == 'Неверный номер карты'
    assert get_mask_card_number('') == 'Неверный номер карты'
    assert get_mask_account(11111234567898765432) == '**5432'
    assert get_mask_account(1111234567898765432) == 'Неверный номер счета'
    assert get_mask_account('') == 'Неверный номер счета'