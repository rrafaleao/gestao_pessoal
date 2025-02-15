import tkinter as tk
from tkinter import ttk

class ListagemFuncionariosView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.criar_tabela()
        self.atualizar_tabela()  # Atualiza a tabela ao iniciar

    def criar_tabela(self):
        """Cria a tabela para exibir os funcionários."""
        colunas = ("ID", "Nome", "CPF", "Cargo", "Departamento", "Email", "Data de Contratação", "Status")
        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")
        
        # Define os cabeçalhos das colunas
        for coluna in colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=100)  # Define a largura das colunas
        
        self.tabela.pack(fill="both", expand=True)

        # Botão para atualizar a lista de funcionários
        btn_atualizar = tk.Button(self, text="Atualizar", command=self.atualizar_tabela)
        btn_atualizar.pack(pady=10)

    def atualizar_tabela(self):
        """Atualiza a tabela com os funcionários cadastrados."""
        # Limpa a tabela
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        
        # Busca os funcionários no banco de dados
        funcionarios = self.controller.buscar_todos_funcionarios()
        
        # Preenche a tabela com os dados
        for funcionario in funcionarios:
            # Converte o status booleano para "Ativo" ou "Inativo"
            status = "Ativo" if funcionario["ativo"] else "Inativo"
            # Insere os dados na tabela
            self.tabela.insert("", "end", values=(
                funcionario["id"],           # ID
                funcionario["nome"],         # Nome
                funcionario["cpf"],          # CPF
                funcionario["cargo"],        # Cargo
                funcionario["departamento"], # Departamento
                funcionario["email"],        # Email
                funcionario["data_contratacao"],  # Data de Contratação
                status                       # Status
            ))