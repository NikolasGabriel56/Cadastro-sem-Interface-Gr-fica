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
        acoes_menu_alterar[opcao] ()
    except:
        input("Opção inválida.\nPressione uma tecla e go back... ")
        alterar()

def pesquisar_id(id=""):
    try:
        if not id:
            id= input("Informe o id do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where id = {id} "
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute (comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()
        alterar_contato(contato)

    except Exception as erro:
        print("Ocorreu um erro na busca por id", erro)
        input("Pressione uma tecla para voltar... ")
        alterar()

def pesquisar_nome():
    try:
        nome= input("Informe o nome do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where nome like '%{nome}%' limit 1"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute (comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']}, telefone: {contato['telefone']}, celular: {contato['celular']}")

        pesquisar_id(contato['id'])

    except Exception as erro:
        print("Ocorreu um erro na busca por id", erro)
        input("Pressione uma tecla para voltar... ")
        alterar()

def pesquisar_telefone():
    try:
        telefone= input("Informe o telefone do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where telefone = {telefone}"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute (comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']}, telefone: {contato['telefone']}, celular: {contato['celular']}")

        pesquisar_id(contato['id'])

    except Exception as erro:
        print("Ocorreu um erro na busca por id", erro)
        input("Pressione uma tecla para voltar... ")
        alterar()

def pesquisar_celular():
    try:
        celular= input("Informe o celular do contato: ")
        comando_sql = f"select id, nome, telefone, celular from contatos where celular = {celular}"
        conexao = mysql.connector.connect(**dados_conexao)
        cursor = conexao.cursor()
        cursor.execute (comando_sql)
        contato = []
        for id, nome, telefone, celular in cursor:
            contato = {"id": id, "nome": nome, "telefone": telefone, "celular": celular}
        cursor.close()
        conexao.close()

        if contato:
            print(f"Contato localizado: id: {contato['id']}, nome: {contato['nome']}, telefone: {contato['telefone']}, celular: {contato['celular']}")

        pesquisar_id(contato['id'])

    except Exception as erro:
        print("Ocorreu um erro na busca por id", erro)
        input("Pressione uma tecla para voltar... ")
        alterar()

def alterar_contato(contato):
    nome =input(f"Informe o nome do contato ({contato['nome']}): ") or contato['nome']
    telefone = input(f"Informe o telefone do contato ({contato['telefone']}): ") or contato['telefone']
    celular = input(f"Informe o celular do contato ({contato['celular']}): ") or contato['celular']

    confirma = input(f"Confirma alteração do contato {nome}? (S/N): ")
    if confirma.upper() == "S":
        try:
            comando_sql = f"update contatos set nome = '{nome}', telefone = '{telefone}', celular = '{celular}' where id = {contato['id']} "
            conexao = mysql.connector.connect(**dados_conexao)
            cursor = conexao.cursor()
            cursor.execute(comando_sql)
            conexao.commit()
            cursor.close()
            conexao.close()
            input('Contato alterado com sucesso\n Pressione uma tecla para voltar...')
        except:
            input("Ocorreu um erro na alteração\n Pressione uma tecla para voltar... ")
    else:
        input("Alteração cancelada\n Pressione uma tecla para voltar...")
    alterar()



acoes_menu_principal = {
    '1': cadastrar,
    '2': alterar,
    # '3': listar,
    # '4': exportar,
    '0': sair,
}

acoes_menu_alterar = {
    '1' : pesquisar_id,
    '2' : pesquisar_nome,
    '3' : pesquisar_telefone,
    '4' : pesquisar_celular,
    '0' : menu_principal
}

if __name__ == "__main__":
    menu_principal()
