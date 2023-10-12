from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def get_search_choice_keyboard() -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Название', callback_data='book_name')
    buttons.button(text='Автор', callback_data='book_author')
    buttons.button(text='Жанр', callback_data='book_genre')
    buttons.button(text='Артикул', callback_data='book_vendor')
    return buttons.as_markup()


def get_title_book_keyboard() -> InlineKeyboardMarkup:
    buttons = InlineKeyboardBuilder()
    buttons.button(text='>>>', callback_data='next')
    buttons.button(text='<<<', callback_data='back')
    return buttons.as_markup()