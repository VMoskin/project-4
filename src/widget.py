from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(num_card: str) -> str:
    """функция принимает номер карты или счета и возвращает маску номера"""
    if "Счет" in num_card:
        if len(num_card) == 25 and num_card[-20:].isdigit():
            return f"{num_card[0:4]} {get_mask_account(int(num_card[-20:]))}"
        else:
            return "Неверный номер счета"
    else:
        if len(num_card) > 16:
            if num_card[-17] == ' ' and num_card[-16:].isdigit():
                return f"{num_card[:-16]}{get_mask_card_number(int(num_card[-16:]))}"
            else:
                return "Неверный номер карты"
        else:
            return "Неверный номер карты"


def get_date(date_string: str) -> str:
    """Фунция возвращает дату в другом формате"""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"


if __name__ == "__main__":
    print(mask_account_card("Счет 92345678987654326543l"))
    print(mask_account_card("Maestro 7000543267892582"))
    print(mask_account_card("Maestro"))
    print(mask_account_card("Visa Platinum 700032106541987"))
    print(get_date("2024-03-12T02:26:18.671407"))
