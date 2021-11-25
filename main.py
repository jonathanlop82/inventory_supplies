import db
import MySQLdb

def run():
    try:
        connection = MySQLdb.connect(db.HOST, db.USER, db.PASSWORD, db.DATABASE, db.PORT)
        cursor = connection.cursor()

    except MySQLdb.Error as error:
        print(error)


if __name__ == '__main__':
    run()