from aiogram.fsm.state import State, StatesGroup


class SearchState(StatesGroup):
    WAITING_FOR_SEARCH_QUERY = State()


class BuyBookState(StatesGroup):
    BOOK_INFO = State()
    SHOPPING_CART = State()
