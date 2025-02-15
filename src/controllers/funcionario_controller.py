from models.funcionario_model import FuncionarioModel

class FuncionarioController:
    def __init__(self, view, model):
        """
        Inicializa o Controller.
        :param view: Instância da View (FuncionarioView).
        :param model: Instância do Model (FuncionarioModel).
        """
        self.view = view
        self.model = model

    def salvar(self, dados):
        """Salva os dados do funcionário no banco de dados."""
        try:
            # Mapeamento dos campos do formulário para os campos do banco de dados
            mapeamento_campos = {
                "nome": "nome",
                "cpf": "cpf",
                "cargo": "cargo",
                "departamento": "departamento",
                "email": "email",
                "data de contratação": "data_contratacao"  # Mapeia para o campo no banco de dados
            }

            # Normaliza os nomes das chaves para minúsculo e aplica o mapeamento
            dados_normalizados = {
                mapeamento_campos[chave.lower()]: valor 
                for chave, valor in dados.items() 
                if chave.lower() in mapeamento_campos
            }

            # Chama o método cadastrar do model com os dados normalizados
            self.model.cadastrar(**dados_normalizados)
            self.view.mostrar_mensagem("Sucesso", "Funcionário salvo com sucesso!")
        except Exception as e:
            self.view.mostrar_mensagem("Erro", f"Falha ao salvar funcionário: {e}")

    def buscar_por_cpf(self, cpf):
        """Busca um funcionário pelo CPF."""
        try:
            resultado = self.model.buscar_por_cpf(cpf)
            if resultado:
                return resultado[0]  # Retorna o primeiro resultado (se houver)
            else:
                self.view.mostrar_mensagem("Erro", "Funcionário não encontrado.")
                return None
        except Exception as e:
            self.view.mostrar_mensagem("Erro", f"Falha ao buscar funcionário: {e}")
            return None
    
    def buscar_todos_funcionarios(self):
        """Busca todos os funcionários cadastrados."""
        try:
            return self.model.buscar_todos_funcionarios()
        except Exception as e:
            self.view.mostrar_mensagem("Erro", f"Falha ao buscar funcionários: {e}")
            return []