import mysql.connector
from mysql.connector import Error

def inserir_fabricantes (nome, descricao):
    try:
        conexao = mysql.connector.connect (
                host= "localhost",
                database = 'bds_fabricantes',
                user = "root",
                password = "Wgo0516")
        

        if conexao.is_connected() :
            cursor = conexao.cursor()
            sql = "INSERT INTO fabricantes (nome,descricao) VALUES (%s, %s)"
            values = (nome, descricao)
            cursor.execute(sql, values)
            conexao.commit()
            print("dados inserirdos com sucesso")

    except Error as e :
        print("Erro ao inserir dados", e)
    
    finally:
        # Fechar cursor e conexão
        if conexao.is_connected():
            cursor.close()
            conexao.close()
