def mask_account_card(num_card: str) -> str:
    """функция принимает номер карты или счета и возвращает маску номера"""
    if "Счет" in num_card:
        return f"{num_card[0:5]} **{num_card[-4:]}"
    else:
        return f"{num_card[:-16]}{num_card[-16:-12]} {num_card[-12:-10]}** **** {num_card[-4:]}"


def get_date(date_string: str) -> str:
    """Фунция возвращает дату в другом формате"""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"


print(mask_account_card("Счет 12345678987654326545"))
print(mask_account_card("Maestro 7000543267892587"))
print(mask_account_card("Visa Platinum 7000321065419874"))
print(get_date("2024-03-11T02:26:18.671407"))