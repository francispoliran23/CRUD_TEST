import mysql.connector
import json
from flask import make_response
class model_connect():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost", user="root", password="poliran", database="crud_handson")
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Established")
        
        except:
            print("Connection not Established")

    def user_getall(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
       
         return make_response({"Product_details":result}, 200)
        
        else:
            return make_response({"Message": "No data Found"}, 204)

    
    def user_add_model(self, data):
        self.cur.execute(f"INSERT INTO users(name, price, description, category) VALUES('{data['name']}', '{data['price']}', '{data['description']}', '{data['category']}')")
        return make_response({"Message": "adding data sucessfully"}, 201)
    
    def user_update_model(self, data):
       self.cur.execute(f"UPDATE  users SET name='{data['name']}', price='{data['price']}', description='{data['description']}', category='{data['category']}' WHERE id= {data['id']}")
       if self.cur.rowcount>0:
          return make_response({"Message": "Updating data sucessfully"}, 202)
       else:
           return make_response({"Message": "Nothing to Update"}, 304) 
       

    def user_delete_model(self, id):
       self.cur.execute(f"DELETE FROM users WHERE id={id}")
       if self.cur.rowcount>0:
          return make_response({"Message": "Deleting Successfully"}, 202)
       else:
           return make_response({"Message": "Nothing to Delete"}, 304)
       
    def user_search_model(self, criteria):
        
        query = (f"SELECT * FROM users WHERE name LIKE '%{criteria}%' OR description LIKE '%{criteria}%' OR category LIKE '%{criteria}%' OR id LIKE '%{criteria}%'")
        self.cur.execute(query)
        result = self.cur.fetchall()
        if len(result) > 0:
            return make_response({"Search_results": result}, 200)
        else:
            return make_response({"Message": "No matching records found"}, 404)
        

