from controllers.base import GerenciadorJanelas
from controllers.funcionario_controller import FuncionarioController
from views.criarFuncionario import FuncionarioView
from views.listagemFuncionario import ListagemFuncionariosView
from models.funcionario_model import FuncionarioModel
from models.database import GerenciadorBancoDados
import tkinter as tk

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestão de Pessoal")
        self.root.geometry("800x600")  # Define o tamanho da janela principal

        # Inicializa o gerenciador de banco de dados e conecta
        self.db_manager = GerenciadorBancoDados()
        self.db_manager.conectar()

        # Inicializa o gerenciador de janelas
        self.gerenciador = GerenciadorJanelas(self.root)

        # Inicializa o Model e o Controller
        self.model = FuncionarioModel(self.db_manager)
        self.controller = FuncionarioController(None, self.model)

        # Cria as telas
        self.view_listagem = ListagemFuncionariosView(self.gerenciador.container, self.controller)
        self.view_adicionar = FuncionarioView(self.gerenciador.container, self.controller)

        # Conecta as views ao Controller
        self.view_listagem.controller = self.controller
        self.view_adicionar.controller = self.controller

        # Adiciona as telas ao gerenciador
        self.gerenciador.adicionar_frame("ListagemFuncionarios", self.view_listagem)
        self.gerenciador.adicionar_frame("AdicionarFuncionario", self.view_adicionar)

        # Mostra a tela de listagem inicialmente
        self.gerenciador.mostrar_frame("ListagemFuncionarios")

if __name__ == "__main__":
    app = MainApp()
    app.root.mainloop()