#!flask/bin/python
# _*_ coding: utf-8 _*_
from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

#MySQL configurations

#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'danic0'
#app.config['MYSQL_DATABASE_DB'] = 'gobierno'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'

app.config.from_object('config')
mysql.init_app(app)

uuaa = [
    {
        'id':1,
        'acronym': u'DCFP',
        'title': u'Gobierno de apps',
        'description': u'Gobierno de uuaa en BBVA España'
    },
    {
        'id':2,
        'acronym': u'PICC',
        'title': u'Net BBVA',
        'description': u'UUAA fake de pruebas'
    }
]


@app.route('/gobierno/api/v1.0/uuaa', methods=['GET'])
def get_uuaas():
    return jsonify({'uuaa' :uuaa})


@app.route('/gobierno/api/v2.0/uuaa', methods=['GET'])
def get_uuaass_v2():
    cur = mysql.connect().cursor()
    cur.execute('''select * from gobierno.uuaa''')
    r = [dict((cur.description[i][0], value)
            for i, value in enumerate (row)) for row in cur.fetchall()]
    return jsonify({'uuaas' : r})


if __name__ == '__main__':
  app.run(debug=True)
