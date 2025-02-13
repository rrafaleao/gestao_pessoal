from models.database import GerenciadorBancoDados
from controllers.base import GerenciadorJanelas
import tkinter as tk
import logging

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestão de Pessoal")
        self.root.geometry("800x600")

        try:
            self.db_manager = GerenciadorBancoDados()
            self.gerenciador = GerenciadorJanelas(self.root)

        except Exception as e:
            logging.error(f"Erro na inicialização: {e}")
    
    def conexao_banco(self):
        self.db_manager.conectar()

if __name__ == "__main__":
    app = MainApp()
    app.conexao_banco()

    