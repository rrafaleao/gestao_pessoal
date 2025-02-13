import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class GerenciadorBancoDados:
    def __init__(self):
        self.connection = None

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                database='gestao_pessoal'
            )
            print("Conexão com o banco de dados estabelecida")
            return self.connection
        except Error as e:
            messagebox.showerror("Erro de Conexão", f"Falha ao conectar ao banco de dados: {e}")
            return None

    def executar_consulta(self, query, params=None):
        """Executa uma consulta SELECT e retorna uma lista de dicionários."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Error as e:
            messagebox.showerror("Erro na Consulta", f"Falha ao executar consulta: {e}")
            return []

    def executar_comando(self, query, params=None):
        """Executa um comando INSERT/UPDATE/DELETE com commit automático."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            cursor.close()
            return True
        except Error as e:
            messagebox.showerror("Erro no Comando", f"Falha ao executar comando: {e}")
            return False

    def iniciar_transacao(self):
        """Inicia uma nova transação."""
        try:
            self.connection.start_transaction()
            return True
        except Error as e:
            messagebox.showerror("Erro na Transação", f"Falha ao iniciar transação: {e}")
            return False

    def confirmar_transacao(self):
        """Confirma (commit) a transação atual."""
        try:
            self.connection.commit()
            return True
        except Error as e:
            messagebox.showerror("Erro na Transação", f"Falha ao confirmar transação: {e}")
            return False

    def reverter_transacao(self):
        """Reverte (rollback) a transação atual."""
        try:
            self.connection.rollback()
            return True
        except Error as e:
            messagebox.showerror("Erro na Transação", f"Falha ao reverter transação: {e}")
            return False

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()