import tkinter as tk

class GerenciadorJanelas:
    def __init__(self, root):
        self.root = root
        self.frames = {}  # Dicionário para armazenar os frames
        self.container = tk.Frame(self.root)  # Container para os frames
        self.container.pack(fill="both", expand=True)

    def adicionar_frame(self, nome, frame_class):
        """
        Adiciona um frame ao gerenciador.
        :param nome: Nome único para o frame.
        :param frame_class: Classe do frame ou instância do frame.
        """
        if isinstance(frame_class, type):  # Se for uma classe
            self.frames[nome] = frame_class(self.container)
        else:  # Se for uma instância
            self.frames[nome] = frame_class
        self.frames[nome].grid(row=0, column=0, sticky="nsew")

    def mostrar_frame(self, nome):
        """
        Mostra o frame especificado.
        :param nome: Nome do frame a ser mostrado.
        """
        frame = self.frames.get(nome)
        if frame:
            frame.tkraise()  # Traz o frame para o topo