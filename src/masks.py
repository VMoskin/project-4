def get_mask_card_number(card_number_1: int) -> str:
    """Функция принимает на вход номер карты и возвращает маску номера"""
    card_number = str(card_number_1)
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number_1: int) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера"""
    account_number = str(account_number_1)
    return f"**{account_number[-4:]}"


print(get_mask_card_number(1234567898765411))
print(get_mask_account(24681357984629753155))
