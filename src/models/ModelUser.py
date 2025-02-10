from .entities.User import User

class ModelUser():

    @classmethod
    def login(cls,mysql,user):
        try: 
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM users WHERE email = %s', (user.email,))
            datos = cur.fetchone()
            cur.close()

            if datos:
                id = datos[0]
                username = datos[1]
                email = datos[2]
                password = User.check_password(datos[3], user.password)
                
                user = User(id,username, email, password)
                
                return user
            else:
                return None
            
        except Exception as e:
            raise Exception(e)
    @classmethod
    def get_by_id(cls,mysql, id):
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT id, username, email FROM users WHERE id = %s', (id,))
            datos = cur.fetchone()
            cur.close()

            if datos:
                id = datos[0]
                username = datos[1]
                email = datos[2]

                logger_user = User(id,username,email,None)
                return logger_user
            
            else:
                return None
            
        except Exception as e:
            raise Exception(e)
        
    @classmethod
    def register(cls,mysql,user):
        try:
            hashed_password = User.generar_password(user.password)
            print(hashed_password)
            cur = cur = mysql.connection.cursor()
            cur.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)', (user.username, user.email, hashed_password))
            mysql.connection.commit()
            cur.close()

        except Exception as e:
            raise Exception(e)