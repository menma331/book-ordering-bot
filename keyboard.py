from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def get_search_choice_keyboard() -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()

    buttons.button(text='Название', callback_data='book_name')
    buttons.button(text='Автор', callback_data='book_author')
    # buttons.button(text='Жанр', callback_data='book_genre') Если придумаю как отображать клаву красиво - сделаю
    buttons.button(text='Артикул', callback_data='book_vendor')

    return buttons.as_markup()


def get_title_book_keyboard() -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()

    buttons.button(text='>>>', callback_data='next')
    buttons.button(text='<<<', callback_data='back')

    return buttons.as_markup()


def get_count_book_keyboard(book_vendor) -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()
    buttons.button(text='-1', callback_data=f'minus:{book_vendor}')
    buttons.button(text='Подтвердить', callback_data=f'confirm:{book_vendor}')
    buttons.button(text='+1', callback_data=f'plus:{book_vendor}')

    buttons.button(text='-5', callback_data=f'minus5:{book_vendor}')
    buttons.button(text='+5', callback_data=f'plus5:{book_vendor}')

    buttons.adjust(3)
    return buttons.as_markup()


def get_buy_book_keyboard(book_vendor=None) -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Забронировать', callback_data=f'request_for_count:{book_vendor}')
    return buttons.as_markup()


def get_delete_keyboard(vendor) -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Убрать из корзины', callback_data=f'remove:{vendor}')
    return buttons.as_markup()


def get_pagination_keyboard(*buttons, page_number, max_page) -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()
    buttons.button(text='<<<', callback_data=f'back_to:{page_number}')
    buttons.button(text=f'Страница {max_page}', callback_data='')
    buttons.button(text='>>>', callback_data=f'next_to:{page_number}')

    buttons.adjust(1)
    return buttons.as_markup()
