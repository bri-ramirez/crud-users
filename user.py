import datetime
from models import Model
from mysqlconnection import connectToMySQL

class User(Model):
    esquema = "users_schema"
    tabla = "users"

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = f"INSERT INTO {cls.tabla} ( first_name , last_name , email ) VALUES ( %(fname)s , %(lname)s , %(email)s );" 
        return connectToMySQL(cls.esquema).query_db( query, data )

    @classmethod
    def update(cls, data):
        query = f"UPDATE {cls.tabla} SET first_name =  %(fname)s, last_name= %(lname)s , email =  %(email)s, updated_at =  %(updated)s WHERE id =  %(id)s;"
        
        # agregamos un key nuevo al diccionario
        data.update({
            "updated": datetime.datetime.now()
        })
            
        return connectToMySQL(cls.esquema).query_db( query, data )