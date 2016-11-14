import sqlite3
import os


def connect():
    has_db = os.path.isfile('blog.db')
    conn = sqlite3.connect('blog.db')

    if not has_db:
        set_db()

    conn.row_factory = sqlite3.Row


def set_db():
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()

    c.execute('create table if not exists user ('
              'id integer primary key autoincrement, '
              'username text not null, '
              'password text not null, '
              'token text)')
    c.execute('create table if not exists post ('
              'id integer primary key autoincrement, '
              'title text, '
              'content text, '
              'author text)')
    c.execute('create table if not exists comment ('
              'id integer primary key autoincrement, '
              'title text, '
              'content text, '
              'author text, '
              'post_id int)')
    c.execute("insert into user (username, password) values ('admin', '123')")

    conn.commit()


def set_new(username, password):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (username, password)
    c.execute("select username from user where username = ?", [username])
    user = c.fetchall()
    if user == []:
        c.execute("insert into user (username, password) values(?, ?)", data)
        conn.commit()
        return True
    else:
        return False


def check_user(username, password):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (username, password)
    c.execute("select username, password from user where username = ?", [username])
    check = c.fetchall()
    if check == []:
        return False
    else:
        check = check[0]
        if data == check:
            return True
        else:
            return False


def create_post(title, content, author):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (title, content, author)
    c.execute("insert into post (title, content, author) values(?, ?, ?) ", data)
    conn.commit()
    c.execute("select id from post order by id desc limit 1")
    post_id = c.fetchall()[0]
    return post_id[0]


def main_page():
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("select title, content, author, id from post order by id desc limit 10")
    list = c.fetchall()
    return list


def make_list_of_dict():
    connect()
    ml = []
    for i in main_page():
        dict = {'title': i[0], 'content': i[1], 'author': i[2], 'id': i[3]}
        ml.append(dict)
    return ml


def post_information(id):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    id = int(id)
    c.execute("select title, content, author, id from post where id = ?", [id])
    information = c.fetchall()[0]
    dict_information = {'title': information[0], 'content': information[1], 'author': information[2], 'id': information[3]}
    return dict_information


def update_post(id, title, content):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    id = int(id)
    data_title = (title, id)
    data_content = (content, id)
    c.execute("update post set title = ? where id = ?", data_title)
    c.execute("update post set content = ? where id = ?", data_content)
    conn.commit()


def delete_post_id(id):
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    id = int(id)
    c.execute("delete from post where id = ?", [id])
    conn.commit()


def new_comment(title, content, author, post_id):
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    id = int(post_id)
    data = (title, content, author, id)
    c.execute("insert into comment (title, content, author, post_id) values(?,?,?,?)", data)
    conn.commit()
    c.execute("select id from comment where author = ? order by id desc limit 1", [author])
    comment_id = c.fetchall()[0][0]
    return comment_id


def comment_list(id):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("select id, title, content, author, post_id from comment where post_id = ? order by id", [id])
    list = c.fetchall()
    ml = []
    for i in list:
        dict = {'id': i[0], 'title': i[1], 'content': i[2], 'author': i[3], 'post_id': i[4]}
        ml.append(dict)
    return ml


def delete_comment(id):
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    id = int(id)
    c.execute("delete from comment where id = ?", [id])
    conn.commit()
