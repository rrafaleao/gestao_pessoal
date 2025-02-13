from controllers.base import GerenciadorJanelas
from controllers.funcionario_controller import FuncionarioController
from views.funcionario_view import FuncionarioView
from models.funcionario_model import FuncionarioModel
from models.database import GerenciadorBancoDados
import tkinter as tk

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestão de Pessoal")
        self.root.geometry("800x600")

        # Inicializa o gerenciador de banco de dados e conecta
        self.db_manager = GerenciadorBancoDados()
        self.db_manager.conectar()  # Conecta ao banco de dados

        # Inicializa o gerenciador de janelas
        self.gerenciador = GerenciadorJanelas(self.root)

        # Inicializa o Model e o Controller
        self.model = FuncionarioModel(self.db_manager)  # Passa o gerenciador de banco de dados
        self.view = FuncionarioView(self.gerenciador.container, None)
        self.controller = FuncionarioController(self.view, self.model)

        # Conecta a View ao Controller
        self.view.controller = self.controller

        # Adiciona a tela de funcionários ao gerenciador
        self.gerenciador.adicionar_frame("FuncionarioView", self.view)

        # Mostra a tela de funcionários
        self.gerenciador.mostrar_frame("FuncionarioView")

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()