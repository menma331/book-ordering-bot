import sqlite3


class Connection:
    def __init__(self):
        self.connection = sqlite3.connect("D:\PythonProjects\kursovaya_Sysa_Roman_4\database\\books.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userID INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                chat_id INTEGER UNIQUE
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
                FOREIGN KEY (userID) REFERENCES users(userID), 
                UNIQUE (userID, bookName)
            )
        """)
        self.connection.commit()

    def add_user(self, user_id: int, username, chat_id) -> None:
        self.cursor.execute("INSERT INTO users (user_id, username, chat_id) VALUES (?, ?, ?)",
                            (user_id, username, chat_id,))

    def execute(self, query: str, args: tuple) -> None:
        self.cursor.execute(query, args)
        self.connection.commit()

    def fetch_one(self):
        return self.cursor.fetchone()

    def __del__(self):
        self.connection.close()
