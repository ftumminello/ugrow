import pyodbc
from database import db

# connString = "Driver={PostgreSQL UNICODE};Server=108.16.16.181;Port=5432;Database=admin;Uid=admin;Pwd=admin;"
# conn = pyodbc.connect(connString)

# d = db()
# cur = conn.cursor()
# d.selectAll()
# cur.execute(d.query1)

d = db('admin', 'admin', 'admin')
# d.addUser(80
d.printTable('City')


# To Do: Create query class that builds out methods that will be useful
# Method list
# Create User Pass
# Check if user exists
# Modify tables
# Read Tablesh