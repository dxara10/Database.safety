import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Ler dados de forma segura
sql = "SELECT * FROM tabela WHERE coluna = %s"
valores = ("valor_a_ser_lido",)

cursor.execute(sql, valores)

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

conexao.close()
