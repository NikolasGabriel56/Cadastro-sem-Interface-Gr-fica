import os
import platform
import mysql.connector

dados_conexao = {"user":"root", "password":"9164", "host":"127.0.0.1", "database":"agenda"}

def limpar_tela():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def sair():
    print("Valeu, brigado")
    os.exit(0)

def mensagem_menu_principal():
    limpar_tela()
    print("**************************************************")
    print("*        BEM-VINDO AO SISTEMA DE CADASTRO        *")
    print("*------------------------------------------------*")
    print("*       ESCOLHA UMA DAS OPÇÕES DISPONÍVEIS       *")
    print("*           1 - CADASTRAR UM CONTATO             *")
    print("*           2 - ALTERAR UM CONTATO               *")
    print("*           3 - LISTAR CONTATOS                  *")
    print("*           4 - EXPORTAR CONTATOS                *")
    print("*           5 - DELETAR CONTATOS                 *")
    print("*           0 - SAIR DO SISTEMA                  *")
    print("**************************************************")

def mensagem_menu_alterar():
    limpar_tela()
    print("**************************************************")
    print("*         ALTERANDO UM CONTATO EXISTENTE         *")
    print("*------------------------------------------------*")
    print("*    ESCOLHA A OPÇÃO PARA LOCALIZAR O CONTATO    *")
    print("*           1 - ID                               *")
    print("*           2 - NOME                             *")
    print("*           3 - TELEFONE                         *")
    print("*           4 - CELULAR                          *")
    print("*           0 - MENU PRINCIPAL                   *")
    print("**************************************************")

def mensagem_menu_deletar():
    limpar_tela()
    print("**************************************************")
    print("*         DELETANDO UM CONTATO EXISTENTE         *")
    print("*------------------------------------------------*")
    print("*    ESCOLHA A OPÇÃO PARA LOCALIZAR O CONTATO    *")
    print("*           1 - ID                               *")
    print("*           2 - NOME                             *")
    print("*           3 - TELEFONE                         *")
    print("*           4 - CELULAR                          *")
    print("*           0 - MENU PRINCIPAL                   *")
    print("**************************************************")

def mensagem_cadastrar():
    limpar_tela()
    print("***************************************************")
    print("*           CADASTRANDO UM NOVO CONTATO           *")
    print("***************************************************")

def menu_principal():
    try:
        mensagem_menu_principal()
        opcao = input ("Digita um número aí meu nobre: ")
        acoes_menu_principal[opcao]()
    except:
        print('')
        input('Ta doidao? Tem essa opção não truta \n Aperta a tecla qualquer e go back ')
        menu_principal()

def cadastrar():
    mensagem_cadastrar()
    nome = input ("Informe o vulgo (obrigatório): ")
    telefone = input ("Informe o tel phone (obrigatório): ")
    celular = input ("Informe o celular, sem mimi, vc sabe que também é (obrigatório): ")

    if nome and telefone and celular:
        confirma = input(f'Tem certeza brow? {nome} (S/N): ')
        if confirma.upper() == "S":
            try:
                 contato = []
                 contato.append(nome)
                 contato.append(telefone)
                 contato.append(celular)
                 conexao = mysql.connector.connect(**dados_conexao)
                 cursor = conexao.cursor()
                 comando_sql = "insert into contatos (nome, telefone, celular) values (%s, %s, %s)"
                 cursor.execute(comando_sql, contato)
                 conexao.commit()
                 cursor.close()
                 conexao.close()
                 input("Deu bom \nAperta a tecla qualquer e go back")
            except Exception as erro:
                input(f"Erro no cadastro: {erro} \nAperta a tecla qualquer e go back: ") 
        else:
            input("Cadastro cancelado \nAperta a tecla qualquer e go back: ")
    else: 
        input("É tudo obrigatório malucao \nAperta a tecla qualquer e go back: ")
    
    menu_principal()

def alterar():
    mensagem_menu_alterar()
    opcao = input("Informe a opção desejada: ")
    try:
        acoes_menu_alterar[opcao]()
    except:
        input("Opção inválida.\nPressione uma tecla para voltar...")
        alterar()


def pesquisar_id(id=""):
    try:
        if not id:
            id = input("Informe o id do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where id = {id}"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        alterar_contato(contato)
    except Exception as err:
        print("Ocorreu erro na busca por id! ", err)
        input("Pressione uma tecla para voltar...")
        alterar()

def pesquisar_nome():
    try:
        nome = input("Informe o nome do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where nome like '%{nome}%'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']},"
                  f"telefone: {contato['telefone']}, celular: {contato['celular']}")
            pesquisar_id(contato['id'])
    except Exception as err:
        print("Ocorreu erro na busca por nome! ", err)
        input("Pressione uma tecla para voltar...")
        alterar()

def pesquisar_telefone():
    try:
        telefone = input("Informe o telefone do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where telefone like '%{telefone}%'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']},"
                  f"telefone: {contato['telefone']}, celular: {contato['celular']}")
            pesquisar_id(contato['id'])
    except Exception as err:
        print("Ocorreu erro na busca por telefone! ", err)
        input("Pressione uma tecla para voltar...")
        alterar()

def pesquisar_celular():
    try:
        celular = input("Informe o celular do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where celular like '%{celular}%'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']},"
                  f"telefone: {contato['telefone']}, celular: {contato['celular']}")
            pesquisar_id(contato['id'])
    except Exception as err:
        print("Ocorreu erro na busca por celular! ", err)
        input("Pressione uma tecla para voltar...")
        alterar()

def alterar_contato(contato):
    nome = input(f"Informe o nome do contato ({contato['nome']}): ") or contato['nome']
    telefone = input(f"Informe o telefone do contato ({contato['telefone']}): ") or contato['telefone']
    celular = input(f"Informe o celular do contato ({contato['celular']}): ") or contato['celular']

    confirma = input(f"Confirma alteração do contato: {nome}? (S/N): ")
    if confirma.upper() == "S":
        try:
            comando_sql = f"update contatos set nome = '{nome}', telefone = '{telefone}'," \
                          f"celular = '{celular}' where id = {contato['id']}"
            conexao = mysql.connector.connect(**dados_conexao)
            cursor = conexao.cursor()
            cursor.execute(comando_sql)
            conexao.commit()
            cursor.close()
            conexao.close()
            input("Contato alterado com sucesso!\nPressione uma tecla para voltar...")
        except:
            input("Ocorreu um erro na alteração.\nPressione uma tecla para voltar...")
    else:
        input("Alteração cancelada.\nPressione uma tecla para voltar...")
    alterar()

def listar():
    try:
        comando = "select id, nome, telefone, celular from contatos order by id asc"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando)
        print("**************************************************")
        for id, nome, telefone, celular in cursor:
            print(f"Id: {id}")
            print(f"Nome: {nome}")
            print(f"Telefone: {telefone}")
            print(f"Celular: {celular}")
            print("**************************************************")

        cursor.close()
        conexao.close()
        input("Pressione uma tecla para voltar ao menu principal...")
    except:
        print("Ocorreu erro no listar.")
    menu_principal()

def exportar():
    try:
        nome_arquivo = input("Informe o nome do arquivo: ") + ".txt"

        comando = "select id, nome, telefone, celular from contatos order by id asc"
        contatos = []
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()

        cursor.execute(comando)
        for id, nome, telefone, celular in cursor:
            contatos.append({"id": id, "nome": nome, "telefone": telefone, "celular": celular})

        cursor.close()
        conexao.close()

        arquivo = open(nome_arquivo, "w", encoding="utf-8")

        for contato in contatos:
            registro = []
            registro.append(f"{contato['id']};{contato['nome']};{contato['telefone']};{contato['celular']}\n\n")
            arquivo.writelines(registro)

        arquivo.close()
        print("Exportação realizada.")
        input("Pressione uma tecla para voltar ao menu principal...")
        menu_principal()
    except Exception as err:
        print("Correu erro na função exportar! ", err)
        input("Pressione uma tecla para voltar ao menu principal...")
        
def deletar():
    
    mensagem_menu_deletar()
    opcao = input("Informe a opção desejada: ")
    try:
       acoes_menu_deletar[opcao]()
    except:
        input("Opção inválida.\nPressione uma tecla para voltar...")
        deletar()
        
def deletar_contato(contato):
    confirma = input(f"Confirma exclusão do contato: {contato['nome']}? (S/N): ")
    
    if confirma.upper() == "S":
        try:
            comando_sql = f"delete from contatos where id = {contato['id']}"
            conexao = mysql.connector.connect(**dados_conexao)
            cursor = conexao.cursor()
            cursor.execute(comando_sql)
            conexao.commit()
            cursor.close()
            conexao.close()
            input("Contato deletado com sucesso com sucesso!\nPressione uma tecla para voltar...")
        except:
            input("Ocorreu um erro na exclusão.\nPressione uma tecla para voltar...")
    else:
        input("Exclusão cancelada.\nPressione uma tecla para voltar...")
    deletar()
    
def deletar_id(id=""):
    try:
        if not id:
            id = input("Informe o id do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where id = {id}"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        deletar_contato(contato)
    except Exception as err:
        print("Ocorreu erro na busca por id! ", err)
        input("Pressione uma tecla para voltar...")
        deletar()

def deletar_nome():
    try:
        nome = input("Informe o nome do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where nome like '%{nome}%'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']},"
                  f"telefone: {contato['telefone']}, celular: {contato['celular']}")
            deletar_id(contato['id'])
    except Exception as err:
        print("Ocorreu erro na busca por nome! ", err)
        input("Pressione uma tecla para voltar...")
        deletar()

def deletar_telefone():
    try:
        telefone = input("Informe o telefone do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where telefone like '%{telefone}%'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']},"
                  f"telefone: {contato['telefone']}, celular: {contato['celular']}")
            deletar_id(contato['id'])
    except Exception as err:
        print("Ocorreu erro na busca por telefone! ", err)
        input("Pressione uma tecla para voltar...")
        deletar()
        
def deletar_celular():
    try:
        celular = input("Informe o celular do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where celular like '%{celular}%'"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']},"
                  f"telefone: {contato['telefone']}, celular: {contato['celular']}")
            deletar_id(contato['id'])
    except Exception as err:
        print("Ocorreu erro na busca por celular! ", err)
        input("Pressione uma tecla para voltar...")
        deletar()
    
acoes_menu_principal = {
    '1': cadastrar,
    '2': alterar,
    '3': listar,
    '4': exportar,
    '5': deletar,
    '0': sair,
}

acoes_menu_alterar = {
    '1': pesquisar_id,
    '2': pesquisar_nome,
    '3': pesquisar_telefone,
    '4': pesquisar_celular,
    '0': menu_principal
}

acoes_menu_deletar = {
    '1': deletar_id,
    '2': deletar_nome,
    '3': deletar_telefone,
    '4': deletar_celular,
    '0': menu_principal
}

if __name__ == "__main__":
    menu_principal()
