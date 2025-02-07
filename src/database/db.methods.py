from database.db_connection import get_db_connection

class DBOperations:
    def __init__(self):
        self.connection = get_db_connection()

    def create_user(self, name, email):
        """Insere um novo usuário no banco de dados."""
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(query, (name, email))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return False

    def get_all_users(self):
        """Retorna todos os usuários do banco de dados."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM users"
            cursor.execute(query)
            users = cursor.fetchall()
            cursor.close()
            return users
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            return []

    def get_user_by_id(self, user_id):
        """Retorna um usuário específico pelo ID."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            return user
        except Exception as e:
            print(f"Erro ao buscar usuário por ID: {e}")
            return None

    def update_user(self, user_id, name, email):
        """Atualiza os dados de um usuário existente."""
        try:
            cursor = self.connection.cursor()
            query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
            cursor.execute(query, (name, email, user_id))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            return False

    def delete_user(self, user_id):
        """Remove um usuário do banco de dados."""
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            return False

    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()