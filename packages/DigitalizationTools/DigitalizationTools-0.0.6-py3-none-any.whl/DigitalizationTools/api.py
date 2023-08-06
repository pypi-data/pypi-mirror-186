import sqlite3
import secrets
import pandas as pd
from datetime import datetime
from beartype import beartype
from typing import Optional, Union

'''
    -: database file includes different tables
    -: database table includes different rows
'''

class database_file:
    
    @beartype
    def __init__(self, db_location:str):
        self.db_location = db_location
    
    def get_table(self):
        try:
            conn = sqlite3.connect(self.db_location)
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cur.fetchall()
            columnsName = [i[0] for i in cur.description]
            conn.commit()
            conn.close()
            df_tables = pd.DataFrame(tables, columns=columnsName)
            return df_tables
        except sqlite3.Error as err:
            return err
    
class database_table(database_file):
    
    @beartype
    def __init__(self, db_location: str, table_name:str):
        super().__init__(db_location)
        self.table_name  = table_name
    
    @beartype
    def create_table(self, keys:list, datatype:list):
        try:
            conn = sqlite3.connect(self.db_location)
            cur = conn.cursor()
            # create table
            create_table_sql = "CREATE TABLE IF NOT EXISTS {} ".format(self.table_name)
            keys_datatype = [f"{keys[i]} {datatype[i]}," for i in range(len(keys))]
            create_table_sql = create_table_sql + \
                                "({} id text, date text);".format("".join(keys_datatype))
            cur.execute(create_table_sql)
            conn.commit()
            conn.close()
            self.keys = keys
            self.datatype = datatype
            return True
        except sqlite3.Error as err:
            return err
    
    @beartype
    def insert_rows(self, insert_data:list, with_id:Optional[bool]=False):
        try:
            conn = sqlite3.connect(self.db_location)
            cur  = conn.cursor()        
            sql = "SELECT * FROM {};".format(self.table_name)
            cur.execute(sql)
            keys = [i[0] for i in cur.description][0:-2]
            
            # insert data
            qs = ",".join(["?" for _ in range(len(keys)+2)])
            insert = """INSERT INTO {} ({},id,date) 
                    VALUES ({})""".format(self.table_name, ",".join(keys), qs)

            # check if id is specified
            if with_id: # true
                insert_data.append(str(datetime.now())[0:19])
            else: # false, no id specified
                insert_data.append(secrets.token_hex(16))
                insert_data.append(str(datetime.now())[0:19])
            cur.execute(insert, tuple(insert_data))
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as err:
            return err
    
    def get_all(self):
        try:
            conn = sqlite3.connect(self.db_location)
            cur = conn.cursor()
            sql = "SELECT * FROM {};".format(self.table_name)
            cur.execute(sql)
            # get all rows
            rows = cur.fetchall()
            # keys
            columnsName = [i[0] for i in cur.description]
            conn.commit()
            conn.close()
            return pd.DataFrame(rows, columns=columnsName)
        except sqlite3.Error as err:
            return err
    
    def get_all_ids(self):
        try:
            df = self.get_all()
            all_ids = df["id"].to_list()
            return all_ids
        except sqlite3.Error as err:
            return err


    @beartype
    def get_one(self, id:str):
        try:
            con = sqlite3.connect(self.db_location)
            cur = con.cursor()
            sql_select = "SELECT * FROM {} WHERE id=?".format(self.table_name)
            cur.execute(sql_select, (id,))
            rows = cur.fetchone()
            columnsName = [i[0] for i in cur.description]
            con.commit()
            con.close()
            return pd.DataFrame([rows], columns=columnsName)
        except sqlite3.Error as err:
            return err
    
    @beartype
    def delete_rows(self, ids:list):
        try:
            for _id in ids:
                con = sqlite3.connect(self.db_location)
                cur = con.cursor()
                sql_delete = 'DELETE FROM {} WHERE id=?'.format(self.table_name)
                cur.execute(sql_delete, (_id,))  
                con.commit()
                con.close()
            return True
        except sqlite3.Error as err:
            return err
    
    def delete_table(self):
        try:
            conn = sqlite3.connect(self.db_location)
            cur  = conn.cursor()
            sql = "DROP TABLE {}".format(self.table_name)
            cur.execute(sql)
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as err:
            return err

    @beartype
    def update_row(self, id:str, update_data:list):
        try:
            all_ids = self.get_all_ids()
            if id in all_ids:
                # delete
                self.delete_rows(ids=[id])
                # insert
                update_data.append(id)
                self.insert_rows(insert_data=update_data, with_id=True)
                return True
            else:
                return "no id matching."
        except sqlite3.Error as err:
            return err