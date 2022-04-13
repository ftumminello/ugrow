import pyodbc

class db():
    def __init__(self, user, pw, database):
        driver = r"{PostgreSQL UNICODE}"
        connString = f"Driver={driver};Server=70.16.131.61;Port=5432;Database={database};Uid={user};Pwd={pw};"
        self.cnxn = pyodbc.connect(connString)
        self.cursor = self.cnxn.cursor()
    
    def addUser(self, serial):
        q = f"INSERT INTO ugrow_env (water_level) VALUES ({serial})"
        self.cursor.execute(q)
        self.cnxn.commit()

    def createTable(self):

        q1 = """
        CREATE TABLE City(
        city_name varchar(128) not null,
        country_name varchar(128) not null,
        isCapital char(3) not null,
        check (isCapital in ('yes', 'no')),
        population int not null,
        primary key(city_name, country_name),
        foreign key (country_name) references Country(country_name));
        """

        q2 = "INSERT INTO City VALUES ('New York, NY', 'US', 'no', '8000000');"
        q3 = "INSERT INTO City VALUES ('Washington, DC', 'US', 'yes', '600000');"
        q4 = "INSERT INTO City VALUES ('Philadelphia, PA', 'US', 'no', '1500000');"
        q5 = "INSERT INTO City VALUES ('Ottawa', 'Canada', 'yes', '800000');"
        q6 = "INSERT INTO City VALUES ('Toronto', 'Canada', 'no', '2500000');"
        q7 = "INSERT INTO City VALUES ('Berlin', 'Germany', 'yes', '3500000');"
        q8 = "INSERT INTO City VALUES ('Hamburg', 'Germany', 'no', '2000000');"
        q9 = "INSERT INTO City VALUES ('Bonn', 'Germany', 'no', '300000');"
        q10 = "INSERT INTO City VALUES ('Paris', 'France', 'yes', '2000000');"
        q11 = "INSERT INTO City VALUES ('Lyon', 'France', 'no', '700000');"
        q12 = "INSERT INTO City VALUES ('Bamako', 'Mali', 'yes', '2000000');"
        q13 = "INSERT INTO City VALUES ('Timbuktu', 'Mali', 'no', '50000');"
        q14 = "INSERT INTO City VALUES ('Mopti', 'Mali', 'no', '100000');"     
        self.cursor.execute(q1)
        self.cursor.execute(q2)
        self.cursor.execute(q3)
        self.cursor.execute(q4)
        self.cursor.execute(q5)
        self.cursor.execute(q6)
        self.cursor.execute(q7)
        self.cursor.execute(q8)
        self.cursor.execute(q9)
        self.cursor.execute(q10)
        self.cursor.execute(q11)
        self.cursor.execute(q12)
        self.cursor.execute(q13)
        self.cursor.execute(q14)
        self.cnxn.commit()

    def printTable(self, table):
        q = f"SELECT * FROM {table}"
        self.cursor.execute(q)
        for d in self.cursor.description:
            print(d[0], end=" ")
        print("")
        for row in self.cursor:
            print(row)
    
    def writeTableToFile(self, table, outFile):
        q = f"SELECT * FROM {table}"
        self.cursor.execute(q)
