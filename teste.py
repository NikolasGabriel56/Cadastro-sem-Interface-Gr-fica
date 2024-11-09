import mysql.connector
from mysql.connector import Error

con = mysql.connector.connect(user='root',password='9164', host='127.0.0.1',database='agenda')
cursor = con.cursor()

# ---------------------------------- Inserção ----------------------------------

# inserir = "insert into contatos (nome, telefone, celular) values ('Lordee', '(31)1234-5678', '(31)9876-5432')"
# cursor.execute(inserir)
# con.commit()
# con.close()

# ---------------------------------- Update ----------------------------------

# atualizar_contato = ("update contatos set nome = %s, telefone = %s, celular = %s where id = 4" )
# dados = ('Cingulere', '(31)9687-5841', '(45)8758-6854')
# cursor.execute(atualizar_contato, dados)
# con.commit()
# con.close()

# ---------------------------------- Delete ----------------------------------
# remover_contato = ("delete from contatos where id = 5")
# cursor.execute(remover_contato)
# con.commit()
# con.close()

# ---------------------------------- Select ----------------------------------

# sql = "select nome, telefone, celular from contatos where nome like 'M%' "
# cursor.execute(sql)
# for (nome, telefone, celular) in cursor:
#     print(f'Nome: {nome}, Telefone: {telefone}, Celular: {celular}')
# cursor.close()
# con.close()

# ---------------------------------- select ----------------------------------

sql = "select nome, telefone, celular from contatos"
cursor.execute(sql)

for (nome, telefone, celular) in cursor:
    print(f'Nome: {nome}, Telefone: {telefone}, Celular: {celular}')

cursor.close()
con.close()