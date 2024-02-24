import sqlite3
from typing import Any


class Connection:
    """Класс подключения к базе данных."""

    def __init__(self):
        """Конструктор класса."""
        self.connection = sqlite3.connect("database/books.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            """
                        CREATE TABLE IF NOT EXISTS users (
                            userID INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            balance REAL DEFAULT 0,
                            chatID INTEGER UNIQUE
                        )
                    """
            )

        self.cursor.execute(
            """
                        CREATE TABLE IF NOT EXISTS selected_books (
                            selectionID INTEGER PRIMARY KEY AUTOINCREMENT,
                            userID INTEGER,
                            bookName TEXT,
                            bookAuthor TEXT,
                            bookGenre TEXT,
                            bookCount INTEGER,
                            bookPrice REAL,
                            bookVendor TEXT,
                            FOREIGN KEY (userID) REFERENCES users(userID)
                        )
                    """
            )

        self.connection.commit()

    def add_user(self, user_id: int, username, chat_id) -> None:
        """Добавить пользователя в базу."""
        self.cursor.execute(
            "INSERT OR IGNORE INTO users (userID, username, chatID) VALUES (?, ?, ?)",
            (user_id, username, chat_id,)
            )
        self.connection.commit()

    def update_balance(self, sum, user_id) -> None:
        """Обновить баланс пользователя."""
        self.cursor.execute(
            "UPDATE users SET balance = balance + ? WHERE userID = ?", (sum, user_id)
            )
        self.connection.commit()

    def get_balance(self, user_id) -> Any:
        """Получить баланс пользователя."""
        balance = self.cursor.execute(
            "SELECT balance FROM users WHERE userID = ?", (user_id,)
            )
        return balance.fetchone()[0]

    def get_whole_price(self, userID) -> int:
        """Получить полную цену корзины."""
        prices = self.cursor.execute(
            "SELECT bookPrice FROM selected_books WHERE userID = ?", (userID,)
            )
        final_price = 0
        for price in prices.fetchall():
            final_price += price[0]

        return final_price

    def pay_whole_price(self, user_id, final_price) -> None:
        """Оплата всей стоимости корзины."""
        self.cursor.execute(
            "UPDATE users SET balance = balance - ? WHERE userID = ?",
            (final_price, user_id,)
            )
        self.cursor.execute("DELETE FROM selected_books WHERE userID = ?", (user_id,))
        self.connection.cursor()

    def __del__(self):
        """Закрытие базы данных."""
        self.connection.close()
