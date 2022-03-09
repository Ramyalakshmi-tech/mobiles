import sqlite3
connection=sqlite3.connect("mobile.db")

listofTables=connection.execute("SELECT name from sqlite_master WHERE type='table' AND name='SMARTPHONES'").fetchall()

if listofTables!=[]:
    print("Table already exists")
else:
    connection.execute('''CREATE TABLE SMARTPHONES(
    SERIALNUM INTEGER,
    BRAND TEXT,
    MODELNAME TEXT,
    MF_YEAR INTEGER,
    MF_MONTH TEXT,
    PRICES INTEGER);
    ''')



while True:
    print("choose the option")
    print("1.Add mobileName")
    print("2.view all")
    print("3.search")
    print("4.update")
    print("5.delete")
    print("6.Exit!!")


    choice=int(input("Enter your choice: "))
    if(choice==1):
       print("selected for adding")
       getserial = input("Enter serial number")
       getBrand = input("Enter Brand name")
       getModelName = input("Enter model name")
       getmfyr = input("Enter manfacturing year")
       getmfmonth = input("Enter manufacturing month ")

       connection.execute("INSERT INTO SMARTPHONES(SERIALNUM,BRAND,MODELNAME,MF_YEAR,MF_MONTH,PRICES)\VALUES("+getserial+",'"+getBrand+"','"+getModelName+"',"+getmfyr+",'"+getmfmonth+"')")
       connection.commit()
       print("Inserted successfully")
    elif choice==2:
       print("for viewing")
       result = connection.execute("SELECT * FROM SMARTPHONES")
       for i in result:
            print("serialnum", i[0])
            print("brand", i[1])
            print("modelname", i[2])
            print("mfyear", i[3])
            print("mfmonth", i[4])
            print("prices",i[5])
    elif choice==3:
        print("for searching")
        getserial = input("Enter serialnumber to be searched")
        result = connection.execute("SELECT * FROM SMARTPHONES WHERE NAME=" + getserial)
        for i in result:
            print("brand", i[1])
            print("modelname", i[2])
            print("mfyear", i[3])
            print("mfmonth", i[4])
            print("prices", i[5])

    elif choice==4:
        print("for updating")
        getserial= input("Enter serialnum to be updated?")
        getBrand = input("Enter Brand")
        getModelName = input("Enter modelname")
        getmfyr = input("Enter manufacturing year")
        getmfmonth = input("Enter manufacturing month")
        getPrices = input("Enter Prices")

        connection.execute("UPDATE SMARTPHONES\
                           SET BRAND='" + getBrand + "',MODELNAME='" + getModelName + "',MF_YEAR=" + getmfyr+ ", MF_MONTH='" + getmfmonth + "',PRICES=" + getPrices + "\
                           WHERE SERIALNUM=" + getserial)
        print("updated successfully")
    elif choice==5:
        print("for deleting")
        getserial = input("Enter serial number to be deleted")
        result = connection.execute("DELETE FROM SMARTPHONES WHERE SERIALNUM=" + getserial)
        print("deleted succesfully")
    elif choice==6:
        break
    else:
        print("invalid")


