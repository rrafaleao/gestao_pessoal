from database.db_connection import conectarBancoDados

def main():
    gerenciador = conectarBancoDados(host="localhost", user="root", password="", database="gestão_pessoal")
    gerenciador.conectar()

if __name__ == "__main__":
    main()

    