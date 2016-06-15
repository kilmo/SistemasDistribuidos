import bottle
import pymongo
import imcApi as c
from sys import argv

def main():
    conn = pymssql.connect(server='grupo04dbserver.database.windows.net', user='sqllog', password='Qweasd123!@#', database='grupo04db')  
    cursor = conn.cursor()
    bottle.debug(True)

    @bottle.route("/post_individuo", method='POST')
    def post_individuo():
        return c.post_individuo(cursor)

    @bottle.route('/list_all')
    def list_all():
        return c.list_all(cursor)


    # bottle.run(host = 'localhost', port=8082)

    bottle.run(host = '0.0.0.0', port=argv[1], server='gunicorn')

if __name__ == '__main__':
    main()