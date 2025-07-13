def mask_account_card(num_card: str) -> str:
    """функция принимает номер карты или счета и возвращает маску номера"""
    if "Счет" in num_card:
        return f"{num_card[0:5]} **{num_card[-4:]}"
    else:
        return f"{num_card[:-16]}{num_card[-16:-12]} {num_card[-12:-10]}** **** {num_card[-4:]}"
print(mask_account_card("Счет 12345678987654326545"))
print(mask_account_card("Maestro 7000543267892587"))
print(mask_account_card("Visa Platinum 7000321065419874"))