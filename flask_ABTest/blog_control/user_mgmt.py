from flask_login import UserMixin
from db_model.mysql import conn_mysqldb
from typing import Any, Iterable

class User(UserMixin):

    def __init__(self, user_id, user_email, blog_id):
        self.id = id
        self.user_email = user_email
        self.blog_id = blog_id
    
    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id : str) -> Iterable[Any]:
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_ID = \"{}\"".format(user_id)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id = user[0], user_email = user[1], blog_id = user[2])
        return user 


    @staticmethod
    def find(user_email : str) -> Iterable[Any]:
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_info WHERE USER_EMAIL = \"{}\"".format(user_email)
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id = user[0], user_email = user[1], blog_id = user[2])
        return user

    @staticmethod
    def create(user_email : str, blog_id :str)-> Iterable[Any]:
        user = User.find(user_email)
        if not user:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ({}, {})".format(str(user_email), str(blog_id))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        
        return user


