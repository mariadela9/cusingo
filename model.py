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

    c.execute('CREATE TABLE IF NOT EXISTS users ('
              'userID text NOT NULL UNIQUE,'
              'name text NOT NULL,'
              'pword text NOT NULL, '
              'PRIMARY KEY(userID) )')

    c.execute('CREATE TABLE IF NOT EXISTS kitchens ('
              'kitchenID text NOT NULL UNIQUE,'
              'name text NOT NULL,'
              'status text NOT NULL,'
              'address text NOT NULL)')

    c.execute('CREATE TABLE IF NOT EXISTS customers ('
              'email text NOT NULL UNIQUE, '
              'address text NOT NULL, '
              'FOREIGN KEY (email) REFERENCES users(userID) )')

    c.execute('CREATE TABLE IF NOT EXISTS  drivers ('
              'driverID text NOT NULL UNIQUE, '
              'pay int, '
              'hours int, '
              'FOREIGN KEY (driverID) REFERENCES users(userID) )')

    c.execute('CREATE TABLE IF NOT EXISTS  chefs ('
              'chefID text NOT NULL UNIQUE, '
              'pay int, '
              'hours int, '
              'FOREIGN KEY (chefID) REFERENCES users(userID) )')

    c.execute('CREATE TABLE IF NOT EXISTS  cars('
              'carID text NOT NULL UNIQUE, '
              'model text NOT NULL, '
              'make text NOT NULL, '
              'year int NOT NULL, '
              'FOREIGN KEY (carID) REFERENCES drivers(driverID) )')

    c.execute('CREATE TABLE IF NOT EXISTS  cars('
              'carID text NOT NULL UNIQUE, '
              'model text NOT NULL, '
              'hours int, '
              'FOREIGN KEY (chefID) REFERENCES users(userID) )')

    c.execute('CREATE TABLE IF NOT EXISTS foodOrder('
              'orderID integer PRIMARY KEY autoincrement, '
              'totalPrice double NOT NULL,'
              'status text NOT NULL,'
              'dateTime DATETIME NOT NULL DEFAULT(GETDATE()) ) ')


    c.execute('CREATE TABLE IF NOT EXISTS drinks('
              'drinkID int NOT NULL, '
              'price double NOT NULL, '
              'name text NOT NULL, '
              'FOREIGN KEY(drinkID) REFERENCES foodOrder(orderID) )')

    c.execute('CREATE TABLE IF NOT EXISTS plates('
              'plateID int NOT NULL, '
              'price double NOT NULL, '
              'name text NOT NULL,'
              'category text NOT NULL,'
              'FOREIGN KEY(plateID) REFERENCES foodOrder(orderID) )')

    c.execute('CREATE TABLE IF NOT EXISTS schedules('
              'kitchenID text NOT NULL, '
              'chefID text NOT NULL, '
              'time text NOT NULL) ')

    c.execute('CREATE TABLE IF NOT EXISTS drives ('
              'driverID text NOT NULL, '
              'carID text NOT NULL )' )

    c.execute('CREATE TABLE IF NOT EXISTS delivers('
              'driverID text NOT NULL, '
              'orderID int NOT NULL )')

    c.execute('CREATE TABLE IF NOT EXISTS pays ('
              'email text NOT NULL, '
              'orderID int NOT NULL )')

    c.execute('CREATE TABLE IF NOT EXISTS makes('
              'chefID text NOT NULL,'
              'orderID int NOT NULL )')

    c.execute('CREATE TABLE IF NOT EXISTS post ('
              'id integer primary key autoincrement, '
              'title text, '
              'content text, '
              'author text)')

    c.execute('CREATE TABLE IF NOT EXISTS comment ('
              'id integer primary key autoincrement, '
              'title text, '
              'content text, '
              'author text, '
              'post_id int)')

    c.execute('insert into kitchens(kitchenID, name, status, address) values("testKitchen", "wildcat", "available", "some address")')


    conn.commit()


def set_new(userID, name, pword):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (userID, name, pword)
    c.execute("select userID from users where userID = ?", [userID])
    user = c.fetchall()
    if user == []:
        c.execute("insert into users(userID, name, pword) values(?, ?, ?)", data)
        conn.commit()
        return True
    else:
        return False

def set_customer(email, address):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (email, address)
    c.execute("select email from customers where email = ?", [email])
    user = c.fetchall()
    print(user)
    if user == []:
        c.execute("insert into customers(email, address) values(?, ?)", data)
        conn.commit()
        return True
    else:
        return False

def set_driver(driverID, pay, hours):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (driverID, pay, hours)
    c.execute("select driverID from drivers where driverID = ?", [driverID])
    user = c.fetchall()
    if user == []:
        c.execute("insert into drivers(driverID, pay, hours) values(?, ?, ?)", data)
        conn.commit()
        return True
    else:
        return False

def set_chef(chefID, pay, hours):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (chefID, pay, hours)
    c.execute("select chefID from chefs where chefID = ?", [chefID])
    user = c.fetchall()
    if user == []:
        c.execute("insert into chefs(chefID, pay, hours) values(?, ?, ?)", data)
        conn.commit()
        return True
    else:
        return False

def set_car(carID, model, make, year):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (carID, model, make, year)
    c.execute("select carID from cars where carID = ?", [carID])
    user = c.fetchall()
    if user == []:
        c.execute("insert into cars(carID, model, make, year) values(?, ?, ?, ?)", data)
        conn.commit()
        return True
    else:
        return False

def set_foodOrder(foodType, total):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (foodType, total)
    c.execute("select orderID from foodOrders where orderID = ?", [orderID])
    user = c.fetchall()
    if user == []:
        c.execute("insert into foodOrders(type, total) values(?, ?)", data)
        conn.commit()
        return True
    else:
        return False

def set_drink(order, price, name):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (order, price, name)
    c.execute("select order from drinks where order = ?", [order])
    user = c.fetchall()
    if user == []:
        c.execute("insert into drinks(order, price, name) values(?, ?, ?) ", data)
        conn.commit()
        return True
    else:
        return False

def set_plate(order, price, name):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (order, price, name)
    c.execute("select order from foodPlates where order = ?", [order])
    user = c.fetchall()
    if user == []:
        c.execute("insert into foodPlates(order, price, name) values(?, ?, ?) ", data)
        conn.commit()
        return True
    else:
        return False


def set_schedule(kitchenID, chefID, time):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (kitchenID, chefID, time)
    print(chefID)
    c.execute("select kitchenID, chefID, time from schedules where kitchenID = ? and chefID = ? and time = ? ", data)
    user = c.fetchall()
    print(user)
    if user == []:
        c.execute("insert into schedules(kitchenID, chefID, time) values(?, ?, ?) ", data)
        conn.commit()
        print("inserted")
        return True
    else:
        return False


def set_drive(driverID, carID):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (driverID, carID)
    c.execute("select driverID, carID from drives where driverID = ? and carID = ? ", data)
    user = c.fetchall()
    if user == []:
        c.execute("insert into schedules(driverID, carID) values(?, ?) ", data)
        conn.commit()
        return True
    else:
        return False

def set_deliver(driverID, orderID):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (driverID, orderID)
    c.execute("select driverID, orderID from delivers where driverID = ? and orderID = ? ", data)
    user = c.fetchall()
    if user == []:
        c.execute("insert into delivers(driverID, orderID) values(?, ?) ", data)
        conn.commit()
        return True
    else:
        return False

def set_pay(email, orderID):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (email, orderID)
    c.execute("select email, orderID from pays where email = ? and orderID = ? ", data)
    user = c.fetchall()
    if user == []:
        c.execute("insert into pays(email, orderID) values(?, ?) ", data)
        conn.commit()
        return True
    else:
        return False

def set_make(chefID, orderID):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (chefID, orderID)
    c.execute("select chefID, orderID from makes where chefID = ? and orderID = ? ", data)
    user = c.fetchall()
    if user == []:
        c.execute("insert into makes(chefID, orderID) values(?, ?) ", data)
        conn.commit()
        return True
    else:
        return False


def check_user(username, password):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = (username, password)
    c.execute("select userID, pword from users where userID = ?", [username])
    check = c.fetchall()
    if check == []:
        return False
    else:
        check = check[0]
        if data == check:
            return True
        else:
            return False


def check_chef(email):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = email
    c.execute("select chefID from chefs where chefID = ?", [email])
    check = c.fetchall()
    if check is None:
        return False
    return True


def check_driver(email):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    data = email
    c.execute("select driverID from drivers where driverID = ?", [email])
    check = c.fetchall()
    if check is None:
        return False
    return True


def check_customer(email):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("select email from customers where email = ?", [email])
    check = c.fetchall()
    if check is None:
        return False
    return True


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
    c.execute("select * from customers")
    list = c.fetchall()
    return list


def make_list_of_dict():
    connect()
    ml = []
    for i in main_page():
        dict = {'title': i[0]}
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


def get_kitchens():
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("select * from kitchens where status = 'available'")
    return c.fetchall()


def update_kitchen(kid):
    connect()
    conn = sqlite3.connect("blog.db")
    c = conn.cursor()
    c.execute("update kitchens set status = 'unavailable' where kitchenID = ?", kid)
    conn.commit()


def get_plates():
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("select * from plates")
    return c.fetchall()


def get_drinks():
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("select * from drinks")
    return c.fetchall()

def get_drink_total(order_id):
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor()
    c.execute("select price from drinks where orderID = ?", order_id)
    ds =  c.fetchall()
    total = 0
    for d in ds:
        total += int(d)
    return total

def get_total():
    connect()
    conn = sqlite3.connect('blog.db')
    c = conn.cursor(order_id)
    c.execute("select price from plates where orderID = ?", order_id)
    ds =  c.fetchall()
    total = get_drink_total()
    for d in ds:
        total += int(d)
    return total
