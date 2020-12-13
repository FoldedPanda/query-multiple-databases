import pyodbc 

class DbConnection:
  def __init__(self, server, username, password):
    self.server = server
    self.database = ''
    self.databases = []
    self.username = username
    self.password = password

dbCon = DbConnection('serverName', 'userName', 'password')
dbCon.databases = [
    'dbName1'
    'dbName2'
    ]
sql = """

-- sql to run goes here

"""
for db in dbCon.databases:
    print(db)
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+dbCon.server+';DATABASE='+db+';UID='+dbCon.username+';PWD='+ dbCon.password)
    cursor = cnxn.cursor()
    cursor.execute(sql) 
    # cnxn.commit()  #uncomment this line when you're ready to run your script
                      
