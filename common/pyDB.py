import pymysql


class DateBaseHandle():



    def __init__(self,host,port,user,passwd,db):


        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.datebase = pymysql.connect()


    def insertDB(self,sql):
        self.cursor = self.db.cursor()


        try:

            self.cursor.execute(sql)
            self.db.commit

        except:

            self.db.roolback()





