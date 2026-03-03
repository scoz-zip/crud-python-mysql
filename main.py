import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sua_senha",
    database="crud_python"
)

cursor = conexao.cursor()

def inserir_usuario(nome, email):
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    cursor.execute(sql, (nome, email))
    conexao.commit()

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    for usuario in cursor.fetchall():
        print(usuario)

def atualizar_usuario(id, nome):
    sql = "UPDATE usuarios SET nome = %s WHERE id = %s"
    cursor.execute(sql, (nome, id))
    conexao.commit()

def deletar_usuario(id):
    sql = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(sql, (id,))
    conexao.commit()

# Teste simples
inserir_usuario("Lucas", "lucas@email.com")
listar_usuarios()
