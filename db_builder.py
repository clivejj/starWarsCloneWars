import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#peeps = csv.DictReader("data/peeps.csv")
command = ""          #put SQL statement in this string

def createTable(tableName, fileName, dataType, db):
        table = "CREATE TABLE " + tableName + " ("
        reader = csv.DictReader(open(fileName))
        #print reader.list_dialects()
        
        #gather the fields
        listFields = []
        for row in reader:
                for key in row:
                        listFields.append(key)
                break
        #print listFields
        #build string to enter field in SQL code
        for counter in range(3):
                table += " " + listFields[counter] + " " + dataType[counter] + "," 
        table = table[:-1] #delete ending comma
        table += ");\n"
        #print table
        db.execute(table)
        
        #build string to enter values
        
        for row in reader:
                rtn = ""
                rtn += "INSERT INTO " + tableName + " VALUES ("
                for key in row:
                        rtn += " " + '"' + row[key] + '"' + ","
                rtn = rtn[:-1]
                rtn += ");\n"
                #print rtn
                c.execute(rtn)
        
createTable("peeps", "data/peeps.csv", ["INTEGER", "TEXT", "INTEGER"], c)
createTable("courses", "data/courses.csv", ["INTEGER", "TEXT", "INTEGER"], c)


db.commit() #save changes
db.close()  #close database