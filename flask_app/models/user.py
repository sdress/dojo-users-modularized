# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
db = 'users_schema'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # create method
    # class method to save our friend to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(db).query_db( query, data )
    
    # read_all method
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(db).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    # read_one method
    @classmethod
    def get_user_info(cls, data):
        query = "SELECT * FROM users WHERE id = %(id_num)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # update method
    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name = %(new_fname)s, last_name = %(new_lname)s, email = %(new_email)s WHERE id = %(id_num)s"
        return connectToMySQL(db).query_db(query, data)

    # destroy method
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id_num)s;"
        return connectToMySQL(db).query_db(query, data)
