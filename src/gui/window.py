import tkinter as tk
from controllers.user_controller import UserController

class MainWindow(tk.Tk):
    def __init__(self, db_connection):
        super().__init__()
        self.db_connection = db_connection
        self.user_controller = UserController(db_connection)
        self.title("Gestão Pessoal")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Adicione widgets e lógica aqui
        label = tk.Label(self, text="Bem-vindo à Gestão Pessoal")
        label.pack(pady=20)
