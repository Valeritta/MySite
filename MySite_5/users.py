import sqlite3
import os.path


class Users:
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    Roll=os.path.join(BASE_DIR, 'Users.db')
    def __init__(self):
        if os.path.isfile(self.Roll)==False:
            connect = sqlite3.connect(self.Roll)
            cursor = connect.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS 'USERS' (
                `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                `login` TEXT UNIQUE,
                `password` TEXT);
                """
            )
            connect.commit()
            connect.close()

    def reg(self, form):
        """Функция регистрирует пользователя, для этого прередайте сюда форму c
        login и password"""
        connect = sqlite3.connect(self.Roll)
        cursor = connect.cursor()
        execute = cursor.execute("""SELECT `login` FROM "USERS" WHERE `login` = (?);""",
        (form["name"], )).fetchone()

        if execute is not None:
            print("test 1")
            connect.close()
            return False
        else:
            print("test 2")
            cursor.execute("""INSERT INTO "USERS" (`login`, `password`)
            VALUES (?, ?);""", (form["name"], form["password"]))
            connect.commit()
        connect.close()
        return True

    def test(self, form):
        """Функция проверки данных (логин, пароль), для этого передайте в функицю,
        форму c login и password"""
        connect = sqlite3.connect(self.Roll)
        cursor = connect.cursor()
        execute = cursor.execute("""SELECT `password` FROM "account"
        WHERE `login` = (?);""", (form["name"],)).fetchone()

        if execute is not None:

            if execute[0] == form["password"]:
                # аворизовать
                result = 3
            else:
                # неправильный пароль
                result = 2
        else:
            # нет такого пользователя
            result = 1
        connect.close()
        return result   