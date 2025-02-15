import mysql.connector
from mysql.connector import Error

class GerenciadorBancoDados:
    def __init__(self):
        self.conexao = None

    def conectar(self):
        """Conecta ao banco de dados MySQL."""
        try:
            self.conexao = mysql.connector.connect(
                host="localhost",
                user="root",  # Substitua pelo seu usuário do MySQL
                password="",  # Substitua pela sua senha do MySQL
                database="gestao_pessoal"
            )
            if self.conexao.is_connected():
                print("Conexão ao banco de dados estabelecida com sucesso!")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conexao = None

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
            print("Conexão ao banco de dados fechada.")

    def executar_consulta(self, query, params=None):
        """Executa uma consulta SELECT e retorna os resultados."""
        if not self.conexao or not self.conexao.is_connected():
            raise Exception("Conexão com o banco de dados não estabelecida.")

        cursor = self.conexao.cursor(dictionary=True)  # Retorna dicionários
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Erro ao executar consulta: {e}")
            return None
        finally:
            cursor.close()

    def executar_comando(self, query, params=None):
        """Executa um comando INSERT/UPDATE/DELETE."""
        if not self.conexao or not self.conexao.is_connected():
            raise Exception("Conexão com o banco de dados não estabelecida.")

        cursor = self.conexao.cursor()
        try:
            cursor.execute(query, params)
            self.conexao.commit()
            print("Comando executado com sucesso!")
        except Error as e:
            print(f"Erro ao executar comando: {e}")
            self.conexao.rollback()
        finally:
            cursor.close()