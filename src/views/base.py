import tkinter as tk
from tkinter import ttk, messagebox

class FormularioBase(tk.Frame):
    def __init__(self, master, campos):
        super().__init__(master)
        self.campos = campos
        self.widgets = {}
        self.criar_formulario()

    def criar_formulario(self):
        """Cria os campos do formulário com base na lista de configurações."""
        for campo in self.campos:
            label = tk.Label(self, text=campo["label"])
            label.pack()

            if campo["tipo"] == "entry":
                widget = tk.Entry(self)
            elif campo["tipo"] == "combobox":
                widget = ttk.Combobox(self, values=campo.get("opcoes", []))
            else:
                raise ValueError(f"Tipo de campo não suportado: {campo['tipo']}")

            widget.pack()
            self.widgets[campo["label"]] = widget

    def validar(self):
        """Método abstrato para validação dos campos."""
        raise NotImplementedError("Subclasses devem implementar o método validar().")

    def obter_valores(self):
        """Retorna os valores dos campos em um dicionário."""
        valores = {}
        for campo in self.campos:
            label = campo["label"]
            widget = self.widgets[label]
            if isinstance(widget, ttk.Combobox):
                valores[label] = widget.get()
            else:
                valores[label] = widget.get()
        return valores

class FormularioFuncionario(FormularioBase):
    def __init__(self, master):
        campos = [
            {"label": "nome", "tipo": "entry"},
            {"label": "cpf", "tipo": "entry", "validacao": "cpf"},
            {"label": "departamento", "tipo": "combobox", "opcoes": ["TI", "RH", "Financeiro"]},
            {"label": "email", "tipo": "entry"},
            {"label": "data_contratacao", "tipo": "entry"}
        ]
        super().__init__(master, campos)

    def validar(self):
        """Implementação específica de validação para o formulário de funcionários."""
        valores = self.obter_valores()

        # Validação do CPF (exemplo simples)
        if "CPF" in valores and len(valores["CPF"]) != 11:
            messagebox.showerror("Erro de Validação", "CPF deve ter 11 dígitos.")
            return False

        # Validação do email (exemplo simples)
        if "Email" in valores and "@" not in valores["Email"]:
            messagebox.showerror("Erro de Validação", "Email inválido.")
            return False

        return True