from aiogram.fsm.state import State, StatesGroup


class SearchState(StatesGroup):
    """Класс для состояния поиска."""
    WAITING_FOR_SEARCH_QUERY = State()


class BuyBookState(StatesGroup):
    """Класс состояния покупки книги."""
    BOOK_INFO = State()
    SHOPPING_CART = State()


class ReplenishBalanceState(StatesGroup):
    """Класс состояния пополнения баланса."""
    WAIT_FOR_SUM = State()
