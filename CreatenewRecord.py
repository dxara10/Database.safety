import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Criar um novo registro de forma segura
sql = "INSERT INTO tabela (coluna1, coluna2) VALUES (%s, %s)"
valores = ("valor1", "valor2")

cursor.execute(sql, valores)

conexao.commit()

print(cursor.rowcount, "registro(s) inserido(s) com segurança.")

conexao.close()
