import masks


def mask_account_card(num_card: str) -> str:
    """функция принимает номер карты или счета и возвращает маску номера"""
    if "Счет" in num_card:
        return f"{num_card[0:4]} {masks.get_mask_account(int(num_card[-20:]))}"
    else:
        return f"{num_card[:-16]}{masks.get_mask_card_number(int(num_card[-16:]))}"


def get_date(date_string: str) -> str:
    """Фунция возвращает дату в другом формате"""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"


print(mask_account_card("Счет 92345678987654326541"))
print(mask_account_card("Maestro 7000543267892582"))
print(mask_account_card("Visa Platinum 7000321065419873"))
print(get_date("2024-03-12T02:26:18.671407"))
