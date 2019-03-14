import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-7VR714F;"
                      "Database=AdventureWorks2017;"
                      "Trusted_Connection=yes;")

cursor = cnxn.cursor()
