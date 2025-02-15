from views.base import FormularioBase
import tkinter as tk
from tkinter import ttk, messagebox

class FuncionarioView(FormularioBase):
    def __init__(self, master, controller):
        campos = [
            {"label": "Nome", "tipo": "entry"},
            {"label": "CPF", "tipo": "entry"},
            {"label": "Cargo", "tipo": "entry"},
            {"label": "Departamento", "tipo": "combobox", "opcoes": ["TI", "RH", "Financeiro"]},
            {"label": "Email", "tipo": "entry"},
            {"label": "Data de Contratação", "tipo": "entry"}
        ]
        super().__init__(master, campos)
        self.controller = controller

        # Botões de ação
        self.btn_salvar = tk.Button(self, text="Salvar", command=self.salvar)
        self.btn_salvar.pack(pady=10)

        self.btn_buscar = tk.Button(self, text="Buscar por CPF", command=self.buscar)
        self.btn_buscar.pack(pady=10)

        self.btn_excluir = tk.Button(self, text="Excluir", command=self.excluir)
        self.btn_excluir.pack(pady=10)

        self.btn_atualizar_status = tk.Button(self, text="Ativar/Desativar", command=self.atualizar_status)
        self.btn_atualizar_status.pack(pady=10)

    def salvar(self):
        """Salva os dados do formulário."""
        valores = self.obter_valores()
        self.controller.salvar(valores)

    def buscar(self):
        """Busca um funcionário pelo CPF."""
        cpf = self.widgets["CPF"].get()  # Coleta o CPF do campo correspondente
        self.controller.buscar_por_cpf(cpf)  # Chama o método do Controller

    def excluir(self):
        """Exclui um funcionário."""
        cpf = self.widgets["CPF"].get()
        self.controller.excluir_por_cpf(cpf)

    def atualizar_status(self):
        """Atualiza o status do funcionário."""
        cpf = self.widgets["CPF"].get()
        self.controller.atualizar_status_por_cpf(cpf)

    def preencher_formulario(self, dados):
        """Preenche os campos do formulário com os dados do funcionário."""
        for campo, valor in dados.items():
            if campo in self.widgets:
                widget = self.widgets[campo]
                if isinstance(widget, tk.Entry) or isinstance(widget, ttk.Combobox):
                    widget.delete(0, tk.END)
                    widget.insert(0, valor)

    def mostrar_mensagem(self, titulo, mensagem):
        """Exibe uma mensagem na tela."""
        messagebox.showinfo(titulo, mensagem)