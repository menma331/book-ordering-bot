from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Connection import Connection
from State import SearchState
from keyboard import get_search_choice_keyboard

router = Router()
states = SearchState()
db = Connection()


@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer('Привет')


@router.message(F.text == '/request')
async def search(message: Message, state: FSMContext):
    await message.answer(text='Введите поисковый запрос.\nВ дальнейшем вы сможете выбрать тип поиска')
    await state.set_state(states.WAITING_FOR_SEARCH_QUERY)


@router.message(states.WAITING_FOR_SEARCH_QUERY)
async def choice_search_category(message: Message, state: FSMContext):
    await message.answer('Выберите категорию поиска', reply_markup=get_search_choice_keyboard())
    await state.update_data(search_request=message.text)


@router.callback_query(F.data == 'book_name')
async def search_by_title(callback: CallbackQuery, state: FSMContext):
    search_query = await state.get_data()
    book = db.cursor.execute(
        "SELECT bookName, authorBook, bookGenre, bookPrice, bookCount, bookVendor FROM books WHERE bookName = (?)",
        (search_query['search_request'],)).fetchone()

    if book is None:
        await callback.message.answer(text=f'Книги c названием {search_query["search_request"]} в магазине нет.')
    else:
        title = book[0]
        author = book[1]
        genre = book[2]
        price = book[3]
        count = book[4]
        vendor = book[5]
        await callback.message.answer(
            text=f'Книга с названием "{title}" найдена.\n{author}\nЦена: {price}\nОстаток на складе: {count}'
                 f'\nАртикул: `{vendor}`',
            parse_mode="MARKDOWN")


@router.callback_query(F.data == 'book_name')
async def search_by_title(callback: CallbackQuery, state: FSMContext):
    search_query = await state.get_data()
    book = db.cursor.execute(
        "SELECT bookName, authorBook, bookGenre, bookPrice, bookCount, bookVendor FROM books WHERE bookName = (?)",
        (search_query['search_request'],)).fetchone()

    if book is None:
        await callback.message.answer(text=f'Книги c названием {search_query["search_request"]} в магазине нет.')
    else:
        title = book[0]
        author = book[1]
        genre = book[2]
        price = book[3]
        count = book[4]
        vendor = book[5]
        await callback.message.answer(
            text=f'Книга с названием "{title}" найдена.\n{author}\nЦена: {price}\nОстаток на складе: {count}'
                 f'\nАртикул: `{vendor}`',
            parse_mode="MARKDOWN")


@router.callback_query(F.data == 'book_author')  # не сделано
async def search_by_title(callback: CallbackQuery, state: FSMContext):
    search_query = await state.get_data()
    book = db.cursor.execute(
        "SELECT bookName, authorBook, bookGenre, bookPrice, bookCount, bookVendor FROM books WHERE authorBook = (?)",
        (search_query['search_request'],)).fetchall()

    if book is None:
        await callback.message.answer(text=f'Книг автора {search_query["search_request"]} в магазине нет.')
    else:

        title = book[0]
        author = book[1]
        genre = book[2]
        price = book[3]
        count = book[4]
        vendor = book[5]
        await callback.message.answer(
            text=f'Книга с названием "{title}" найдена.\n{author}\nЦена: {price}\nОстаток на складе: {count}'
                 f'\nАртикул: `{vendor}`',
            parse_mode="MARKDOWN")


@router.callback_query(F.data == 'book_genre')  # Не сделано
async def search_by_title(callback: CallbackQuery, state: FSMContext):
    search_query = await state.get_data()
    book = db.cursor.execute(
        "SELECT bookName, authorBook, bookGenre, bookPrice, bookCount, bookVendor FROM books WHERE bookName = (?)",
        (search_query['search_request'],)).fetchone()

    if book is None:
        await callback.message.answer(text=f'Книги c названием {search_query["search_request"]} в магазине нет.')
    else:
        title = book[0]
        author = book[1]
        genre = book[2]
        price = book[3]
        count = book[4]
        vendor = book[5]
        await callback.message.answer(
            text=f'Книга с названием "{title}" найдена.\n{author}\nЦена: {price}\nОстаток на складе: {count}'
                 f'\nАртикул: `{vendor}`',
            parse_mode="MARKDOWN")


@router.callback_query(F.data == 'book_vendor')  # Не сделано
async def search_by_title(callback: CallbackQuery, state: FSMContext):
    search_query = await state.get_data()
    book = db.cursor.execute(
        "SELECT bookName, authorBook, bookGenre, bookPrice, bookCount, bookVendor FROM books WHERE bookVendor = (?)",
        (search_query['search_request'],)).fetchone()

    if book is None:
        await callback.message.answer(text=f'Книги c артикулом {search_query["search_request"]} в магазине нет.')
    else:
        title = book[0]
        author = book[1]
        genre = book[2]
        price = book[3]
        count = book[4]
        vendor = book[5]
        await callback.message.answer(
            text=f'Книга с названием "{title}" найдена.\n{author}\nЦена: {price}\nОстаток на складе: {count}'
                 f'\nАртикул: `{vendor}`',
            parse_mode="MARKDOWN")
