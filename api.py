from flask import Flask, make_response, request, jsonify
from flask_mysqldb import MySQL
import xml.etree.ElementTree as ET
import xmltodict
import functools


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "store"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

#code for authentication
def security(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        a = request.authorization
        if a and a.username == "clyde" and a.password == "10222000":
            return f(*args, **kwargs)
        return make_response(
            "Could not verify your login!",
            401,
            {"WWW-Authenticate": 'Basic realm="Login"'},
        )
    return decorated

mysql = MySQL(app)

@app.route("/")
@security
def hello_world():
    return "<p>Hello, World!</p>"


def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/tables", methods=["GET"])
def show_tables():
    return make_response(jsonify(data_fetch("show tables")), 200)

@app.route("/tables/<string:table>", methods=["GET"])
def select_table(table):
    return make_response(jsonify(data_fetch(f"select * from {table}")))

@app.route("/tables/<string:table>/<int:id>", methods=["GET"])
def select_table_id(table, id):
    return make_response(jsonify(data_fetch(f"select * from {table} where id='{id}'")))


@app.route("/tables/<string:table>/<int:id>", methods=["POST"])
def add_entries(table, id):
    cur = mysql.connection.cursor()
    info = request.get_json()

    if table == "customer":
        fname = info["fname"]
        lastname = info["lastname"]
        contact_num = info["contact_num"]
        address = info["address"]
        order_id = info["order_id"]
        query = "insert into customer values (%s, %s, %s ,%s, %s, %s)"
        cur.execute(query, (id, fname, lastname, contact_num, address, order_id ))
        mysql.connection.commit()

    elif table == "employee":
        firstname = info["firstname"]
        lastname = info["lastname"]
        age = info["age"]
        position = info["position"]
        query = "insert into employee values (%s, %s, %s, %s, %s)"
        cur.execute(query, (id, firstname, lastname, age, position))
        mysql.connection.commit()

    elif table == "orders":
        foods = info["foods"]
        beverages = info["beverages"]
        query = "insert into orders values (%s, %s, %s)"
        cur.execute(query, (id, foods, beverages))
        mysql.connection.commit()

    cur.close()
    return make_response(jsonify({"Message": "Successfully added"}))

@app.route("/tables/<string:table>/<int:id>", methods=["PUT"])
def update_entry(table, id):
    cur = mysql.connection.cursor()
    info = request.get_json()

    if table == "customer":
        fname = info["fname"]
        lastname = info["lastname"]
        contact_num = info["contact_num"]
        address = info["address"]
        order_id = info["order_id"]
        query = "UPDATE customer SET fname=%s, lastname=%s, contact_num=%s, address=%s, order_id=%s WHERE id=%s"
        cur.execute(query, (fname, lastname, contact_num, address, order_id, id))
        mysql.connection.commit()

    elif table == "employee":
        firstname = info["firstname"]
        lastname = info["lastname"]
        age = info["age"]
        position = info["position"]
        query = "UPDATE employee SET firstname=%s, lastname=%s, age=%s, position=%s WHERE id=%s"
        cur.execute(query, (firstname, lastname, age, position, id))
        mysql.connection.commit()

    elif table == "orders":
        foods = info["foods"]
        beverages = info["beverages"]
        query = "UPDATE orders SET foods=%s, beverages=%s WHERE id=%s"
        cur.execute(query, (foods, beverages, id))
        mysql.connection.commit()

    cur.close()
    return make_response(jsonify({"Message": "Successfully updated"}))


@app.route("/tables/<string:table>/<int:id>", methods=["DELETE"])
def delete_by_id(table, id):
    cur = mysql.connection.cursor()

    if table == "customer":
        query = "DELETE FROM customer WHERE id = %s"
        cur.execute(query, (id,))
        mysql.connection.commit()

    elif table == "employee":
        query = "DELETE FROM employee WHERE id = %s"
        cur.execute(query, (id,))
        mysql.connection.commit()

    elif table == "order":
        query = "DELETE FROM orders WHERE id = %s"
        cur.execute(query, (id,))
        mysql.connection.commit()

    cur.close()
    return make_response(jsonify({"Message": "Successfully deleted"}))

if __name__ == "__main__":
    app.run(debug=True)