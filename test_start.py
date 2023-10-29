# tests/test_main.py
import pytest

from test_message import test_message
from handlers import start


# Создаем mock-объекты для Bot и Dispatcher
class MockBot:
    async def start(self, *args, **kwargs):
        pass


class MockDispatcher:
    def include_router(self, router):
        pass


@pytest.mark.asyncio
async def test_start():
    # Создаем mock-объекты для Bot и Dispatcher
    bot = MockBot()
    dispatcher = MockDispatcher()

    # Mock-объекты для функций, которые могут вызываться в вашей функции start()
    # Например, если ваши функции выполняют какие-то действия, здесь вы можете создать mock-функции,
    # которые будут имитировать их работу.
    start_message = test_message.replace('text=/get', 'text=/start')
    # Запускаем тестируемую функцию
    await start(start_message)

    # Добавьте здесь проверки для убедительности, что функция start() выполнила ожидаемые действия.

    # Пример: проверка, что mock-функции были вызваны с ожидаемыми аргументами
    # mock_function.assert_called_with(expected_argument)

    # Замените это на фактические проверки, которые соответствуют вашей логике.


# @pytest.mark.asyncio
# async def test_request():
#     bot = MockBot()

