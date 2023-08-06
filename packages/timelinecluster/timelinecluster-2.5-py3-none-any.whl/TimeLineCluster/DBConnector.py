import psycopg2
from psycopg2 import pool
import pandas as pd
class ConnectDB:
    conn = None
    flag_return_data = None
    def __init__(self,host , database , user , password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.text_error = ""

    def connect_to_db(self, minConnection, maxConnection):
        try:
            self.conn = psycopg2.pool.SimpleConnectionPool(minConnection, maxConnection, user=self.user,
                                                         password=self.password,
                                                         host=self.host,
                                                         database=self.database)

            if (self.conn):
                self.text_error = ""
                print("Connection pool created successfully")

            # ps_connection = self.conn.getconn()
            # if (ps_connection):
            #     print("successfully recived connection from connection pool ")
            #     ps_cursor = ps_connection.cursor()
            #     ps_cursor.execute("insert into test123 (id,name) values(1,'testabc')")
            #     ps_connection.commit()
            #     ps_cursor.close()

            #     # Use this method to release the connection object and send back to connection pool
            #     self.conn.putconn(ps_connection)
            #     print("Put away a PostgreSQL connection")

            return self.conn
        except Exception as error: 
            print("Could not connect to database", self.database)
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            self.text_error = "Oops! An exception has occured : " + str(error) + " Exception TYPE : " + str(type(error))
            if self.conn:
                self.conn.closeall
                print("PostgreSQL connection pool is closed 1")
            self.conn = False
            return False
        # finally:
        #     # closing database connection.
        #     # use closeall() method to close all the active connection if you want to turn of the application
        #     if self.conn:
        #         self.conn.closeall
        #     print("PostgreSQL connection pool is closed 2")

    def queryRead(self, sql):
        try:
            ps_connection = self.conn.getconn()
            if (ps_connection):
                # print("successfully recived connection from connection pool ")
                data = pd.read_sql(sql , ps_connection)
                ps_connection.close()
                # Use this method to release the connection object and send back to connection pool
                self.conn.putconn(ps_connection)
                # print("Put away a PostgreSQL connection")
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            self.closeAllConnection("queryRead")
            self.conn = self.connect_to_db(1,1)
            ps_connection = self.conn.getconn()
            if (ps_connection):
                data = pd.read_sql(sql , ps_connection)
                ps_connection.close()
                self.conn.putconn(ps_connection)
                print("Re connect !!")
        finally:
            # closing database connection.
            # use closeall() method to close all the active connection if you want to turn of the application
            if self.conn:
                self.conn.closeall
        return data

    def queryExecute(self, sql, param, flag_return):
        try:
            ps_connection = self.conn.getconn()
            if (ps_connection):
                print("successfully recived connection from connection pool ")
                ps_cursor = ps_connection.cursor()
                if(param == None):
                    ps_cursor.execute(sql)
                else:
                    ps_cursor.execute(sql, param)
                data = ps_cursor   
                if(flag_return == "fetchall"):
                    self.flag_return_data = ps_cursor.fetchall()   
                if(flag_return == "fetchone"):
                    self.flag_return_data = ps_cursor.fetchone()            
                ps_connection.commit()
                ps_cursor.close()
                self.conn.putconn(ps_connection) 
        except Exception as error:
            print ("Oops! An exception has occured:", error)
            print ("Exception TYPE:", type(error))
            self.closeAllConnection("queryExecute")
            self.conn = self.connect_to_db(1,1)
            ps_connection = self.conn.getconn()
            if (ps_connection):
                print("successfully recived connection from connection pool ")
                ps_cursor = ps_connection.cursor()
                if(param == None):
                    ps_cursor.execute(sql)
                else:
                    ps_cursor.execute(sql, param)
                data = ps_cursor   
                if(flag_return == "fetchall"):
                    self.flag_return_data = ps_cursor.fetchall()   
                if(flag_return == "fetchone"):
                    self.flag_return_data = ps_cursor.fetchone()          
                ps_connection.commit()
                ps_cursor.close()
                self.conn.putconn(ps_connection)
                print("Re connect !!")
        finally:
            # closing database connection.
            # use closeall() method to close all the active connection if you want to turn of the application
            if self.conn:
                self.conn.closeall
        return data

    def closeAllConnection(self, text):
        if self.conn:
            self.conn.closeall
            # print("PostgreSQL connection pool is closed (" + text + ")")

    def disconnect(self, db_type):
        if(self.conn != False or self.conn != None):
            self.conn.close()
            print("Disconnect database " + db_type)