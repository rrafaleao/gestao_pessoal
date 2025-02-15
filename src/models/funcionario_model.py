class FuncionarioModel:
    def __init__(self, db_manager):
        """
        Inicializa o Model.
        :param db_manager: Instância do GerenciadorBancoDados.
        """
        self.db = db_manager

    def buscar_por_cpf(self, cpf):
        query = "SELECT * FROM Funcionarios WHERE cpf = %s"
        return self.db.executar_consulta(query, (cpf,))

    def cadastrar(self, nome, cpf, cargo, departamento, email, data_contratacao):
        query = """
        INSERT INTO Funcionarios (nome, cpf, cargo, departamento, email, data_contratacao)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (nome, cpf, cargo, departamento, email, data_contratacao)
        self.db.executar_comando(query, valores)

    def excluir_por_cpf(self, cpf):
        query = "DELETE FROM Funcionarios WHERE cpf = %s"
        self.db.executar_comando(query, (cpf,))

    def atualizar_status_por_cpf(self, cpf, ativo=True):
        query = "UPDATE Funcionarios SET ativo = %s WHERE cpf = %s"
        self.db.executar_comando(query, (ativo, cpf))

    def buscar_todos_funcionarios(self):
        """Busca todos os funcionários cadastrados."""
        query = "SELECT * FROM Funcionarios"
        return self.db.executar_consulta(query)