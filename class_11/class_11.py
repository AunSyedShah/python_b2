import pyodbc


# step 1: create a connection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-JORPJ44;'
                      'Database=testphase;'
                      'Trusted_Connection=yes;')

# step 2: create a cursor
cursor = conn.cursor()

# step 3: execute a query
data = cursor.execute('SELECT * FROM dbo.testphase_vehicle')

for row in data:
    print(row)

