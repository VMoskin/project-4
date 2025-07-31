def get_mask_card_number(card_number_1: int) -> str:
    """Функция принимает на вход номер карты и возвращает маску номера"""
    card_number = str(card_number_1)
    if len(card_number) == 16:
        return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    else:
        return 'Неверный номер карты'


def get_mask_account(account_number_1: int) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера"""
    account_number = str(account_number_1)
    if len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return 'Неверный номер счета'


if __name__ == "__main__":
    #print(get_mask_card_number(1234567898765411))
    #print(get_mask_account(24681357984629753155))
    print(get_mask_card_number(''))