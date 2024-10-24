import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()

# Consulta parametrizada
sql = "SELECT * FROM tabela WHERE coluna = %s"
valores = ("valor_parametrizado",)

cursor.execute(sql, valores)

resultados = cursor.fetchall()

for resultado in resultados:
    print(resultado)

conexao.close()
