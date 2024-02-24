from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def get_search_choice_keyboard() -> InlineKeyboardMarkup:
    """Получить inline клавиатуру с выбором категории поиска."""
    buttons = InlineKeyboardBuilder()

    buttons.button(text='Название', callback_data='book_name')
    buttons.button(text='Автор', callback_data='book_author')
    # buttons.button(text='Жанр', callback_data='book_genre') Если придумаю как отображать клаву красиво - сделаю
    buttons.button(text='Артикул', callback_data='book_vendor')

    return buttons.as_markup()


def get_count_book_keyboard(book_vendor) -> InlineKeyboardMarkup:
    """Получить inline клавиатуру с выбором количества книг."""
    buttons = InlineKeyboardBuilder()
    buttons.button(text='-1', callback_data=f'minus:{book_vendor}')
    buttons.button(text='Подтвердить', callback_data=f'confirm:{book_vendor}')
    buttons.button(text='+1', callback_data=f'plus:{book_vendor}')

    buttons.button(text='-5', callback_data=f'minus5:{book_vendor}')
    buttons.button(text='+5', callback_data=f'plus5:{book_vendor}')

    buttons.adjust(3)
    return buttons.as_markup()


def get_buy_book_keyboard(book_vendor=None) -> InlineKeyboardMarkup:
    """Получить inline клавиатуру с кнопкой 'Забронировать'."""
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Забронировать', callback_data=f'request_for_count:{book_vendor}')
    return buttons.as_markup()


def get_delete_keyboard(vendor) -> InlineKeyboardMarkup:
    """Получить inline клавиатуру с кнопкой 'Убрать из корзины'."""
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Убрать из корзины', callback_data=f'remove:{vendor}')
    return buttons.as_markup()


def get_balance_keyboard() -> InlineKeyboardMarkup:
    """Получить inline клавиатуру с кнопкой 'Пополнить'."""
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Пополнить', callback_data='replenish')
    return buttons.as_markup()


def get_pay_for_books_keyboard() -> InlineKeyboardMarkup:
    """Получить inline клавиатуру с кнопкой 'Оплатить'."""
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Оплатить', callback_data='pay')
    return buttons.as_markup()
