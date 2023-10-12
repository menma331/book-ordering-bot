import sqlite3


class Connection:
    def __init__(self):
        self.connection = sqlite3.connect("database/books.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userID INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                chatID INTEGER UNIQUE
            )
        """)

        self.cursor.execute("""
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
        """)

        self.connection.commit()

    def add_user(self, user_id: int, username, chat_id) -> None:
        self.cursor.execute("INSERT OR IGNORE INTO users (userID, username, chatID) VALUES (?, ?, ?)",
                            (user_id, username, chat_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
