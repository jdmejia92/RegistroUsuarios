from src.database.db import get_connection
from .entities.User import User


class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cur:
                cur.execute(
                    "SELECT id, email, password FROM users ORDER BY email ASC")
                resultset = cur.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise ex

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cur:
                cur.execute(
                    "SELECT id, email, password FROM users WHERE id = %s", (id,))
                row = cur.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise ex

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cur:
                cur.execute("INSERT INTO users (id, email, password) VALUES (%s, %s, %s)",
                            (user.id, user.email, user.password))
                affected_rows = cur.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex

    @classmethod
    def get_user_email(self, email):
        try:
            connection = get_connection()

            with connection.cursor() as cur:
                cur.execute(
                    "SELECT id, email, password FROM users WHERE email = %s", (email,))
                row = cur.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise ex

    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (user.id,))
                affected_rows = cur.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cur:
                cur.execute("UPDATE users SET email = %s, password = %s WHERE id = %s",
                            (user.email, user.password, user.id))
                affected_rows = cur.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise ex
