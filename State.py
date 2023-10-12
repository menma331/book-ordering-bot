from aiogram.fsm.state import State, StatesGroup


class SearchState(StatesGroup):
    WAITING_FOR_SEARCH_QUERY = State()
