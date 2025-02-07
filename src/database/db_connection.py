import mysql.connector
from mysql.connector import Error

class conectarBancoDados:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="gestao_pessoal"
            )
            print("Conexão ao banco de dados realizada com sucesso!")
            return self.conexao
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
