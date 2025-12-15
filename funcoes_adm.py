import funcoes_auxiliares as faux
from datetime import datetime
import cv2


#----------------------------------------------CADASTRO DE USUÁRIO------------------------------

def cadastrar_usuário(usuarios):
    nome = input('Digite o seu nome: ')
    while not faux.nome(nome):
        nome = input('Digite o seu nome: ')
    
    login = input('Digite o seu E-mail: ').lower()
    while (not faux.verificar_email(login)) or (not faux.copia_login(usuarios, login)):
        login = input('Digite seu E-mail, novamente: ').lower()
        
    senha = input('Digite a sua senha (Mínimo 8 caracteres): ').lower()
    while (not faux.verificar_senha(senha)) or (not faux.copia_senha(usuarios, senha)):
        senha = input('Digite sua sennha novamente: ').lower()
        
    tipo = "cliente"
    
    usuarios.append({
        'nome': nome,
        'email': login,
        'senha': senha,
        'tipo': tipo
    })
    
def cadastrar_admin(adm):
    nome = input('Digite o seu nome: ')
    while not faux.nome(nome):
        nome = input('Digite o seu nome: ')
    
    login = input('Digite o seu e-mail para cadastro: ').lower()
    while (not faux.verificar_email(login)) or (not faux.copia_login_adm(adm, login)):
       login = input('Digite o seu e-mail para cadastro: ').lower()
       
    senha = input('Digite sua senha para cadastro: ').lower()
    while (not faux.verificar_senha(senha)) or (not faux.copia_senha_adm(adm, senha)):
         senha = input('Digite sua senha para cadastro: ').lower()
        
    id_verify = (input('Crie o seu ID de verificação para cadastro, contendo apenas números: ')).lower()
    while (not faux.verificar_id_adm(id_verify)) or (not faux.copia_id(adm, id_verify)):
        id_verify = (input('Digite o seu ID de verificação: ')).lower()
        
    tipo = "admin"
    
    adm.append({
        'nome': nome,
        'email': login,
        'senha': senha,
        'id': id_verify,
        'tipo': tipo
        })
    
def cadastrar(usuarios, adm):
    tipo_cadastro = input('Deseja cadastrar-se como usuário[1] ou administrador[2]: ')
    while not faux.ver_tipo(tipo_cadastro):
        tipo_cadastro = input('Deseja cadastrar-se como usuário[1] ou administrador[2]: ')
    
    if tipo_cadastro == '1':
        cadastrar_usuário(usuarios)
        print('Cadastro realizado com sucesso!')
        
    elif tipo_cadastro == '2':
        cadastrar_admin(adm)
        print('Cadastro realizado com sucesso!')
    
#-----------------------------LOGIN DE USUÁRIO-----------------------------------------------
    
def login_cliente(usuarios):
    login_ver = input('Digite o seu e-mail de cadastro: ')
    senha_ver = input('Digite sua senha: ')
    for us in usuarios:
        if us['email'] == login_ver and us['senha'] == senha_ver:
            nome = us['nome']
            tirar_foto(nome)
            return True
        
    return False

def login_adm(adm):
    login = input('Digite o seu e-mail de cadastro: ')
    id_verify = input('Digite seu id de verificação: ')
    
    for i in adm:
        if login == i['email'] and id_verify == i['id']:
            nome = i['nome']
            tirar_foto(nome)
            return True
        
    return False

def tirar_foto(nome):
    pessoa = nome.replace(' ', '_')
    data = datetime.now().strftime("%d_%m_%Y")
    nome_arquivo = f'UltimoAcesso_{pessoa}_{data}.jpg'
    
    camera = cv2.VideoCapture(0)
    
    ret, frame = camera.read()
    
    if ret:
        cv2.imwrite(nome_arquivo, frame)
        
    camera.release()
        
    
#--------------------------IMPORTAR USUÁRIOS-------------------------------------------------

def importar_cadastros_adm(adm):
    arquivo = open('Administradores.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        if len(linha) > 0:
            
            linha = linha.split(' - ') 
            igual = False
            for admin in adm:
                if linha[0] == admin['nome'] and linha[1] == admin['email'] and linha[2] == admin['senha']:
                    igual = True
                    break
            
            if igual:
                continue
                
            nome = linha[0]
            login = linha[1]
            senha = linha[2]
            id_verify = linha[3]
            tipo = linha[4]
            
            adm.append({
            'nome': nome,
            'email': login,
            'senha': senha,
            'id': id_verify,
            'tipo': tipo
            })
        
    arquivo.close()
    
def importar_cadastros_usuário(usuarios):
    arquivo = open('Usuários.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        if len(linha) > 0:
            
            linha = linha.split(' - ')
            igual = False
            for pessoas in usuarios:
                if linha[0] == pessoas['nome'] and linha[1] == pessoas['email'] and linha[2] == pessoas['senha']:
                    igual = True
                    break
            
            if igual:
                continue
            
            nome = linha[0]
            login = linha[1]
            senha = linha[2]
            tipo = linha[3]
            
            usuarios.append({
            'nome': nome,
            'email': login,
            'senha': senha,
            'tipo': tipo
            })
        
    arquivo.close()
    
def importar_backup_para_lista(adm, usuarios):
    importar_cadastros_adm(adm)
    
    importar_cadastros_usuário(usuarios)
    print('Arquivos de cadastro de ADMIN e CLIENTE importados de volta para a lista com sucesso!')

#-----------------------------BACKUP DE USUARIO---------------------------------------------

def fazer_backup_adm(adm):
    arquivo = open('Administradores.txt', 'w')
    for admin in adm:
        arquivo.write(f"{admin['nome']} - {admin['email']} - {admin['senha']} - {admin['id']} - {admin['tipo']}\n")
        
    arquivo.close()

def fazer_backup_usuario(usuarios):
    arquivo = open('Usuários.txt', 'w')
    for usuario in usuarios:
        arquivo.write(f"{usuario['nome']} - {usuario['email']} - {usuario['senha']} - {usuario['tipo']}\n")
        
    arquivo.close()

def fazer_backup_para_arquivo(adm, usuarios):
    fazer_backup_adm(adm)
    
    fazer_backup_usuario(usuarios)
    print('Backup para arquivo feito com sucesso!')


#----------------------------------------------MENUS DE OPERAÇÕES---------------------------

def mostra_menu():
    print('--------------- MENU ---------------')
    print('1. Cadastrar Usuário')
    print('2. Importar backup de cadastro')
    print('3. Fazer backup de cadastros')
    print('4. Gerenciar produtos e serviços')
    print('5. Comprar produtos e agendar serviços')
    print('0. Sair')
    
    opcao = int(input('Digite a opçâo desejada: '))
    while not faux.opc_ver(opcao):
        opcao = int(input('Digite a opçâo desejada: '))
    return opcao

def operacoes_menu_admin():
    print('----------- MENU DE OPERAÇÕES -----------')
    print('1. Cadastrar novo serviço/produto')
    print('2. Importar backup para lista')
    print('3. Fazer backup de produtos e serviços')
    print('4. Buscar/Atualizar/Remover')
    print('5. Analise de estoque')
    print('6. Criar cupons de desconto')
    print('7. Alterar/Remover cupons de desconto')
    print('0. Voltar a menu anterior')

    opcao = int(input('Digite a opção desejada: '))
    while not faux.op_escolha(opcao):
        opcao = int(input('Digite a opção desejada: '))
    return opcao

def opercacoes_menu_cliente():
    print('----------- MENU CLIENTE -----------')
    print('1. Comprar produto')
    print('2. Agendar serviço')
    print('3. Ver carrinho')
    print('4. Ver meus agendamentos')
    print('5. Salvar carrinho de compras e agenda de serviços')
    print('6. Restaurar carrinho de compras e agenda de serviços')
    print('0. Sair da área do cliente')
    
    opcao = int(input('Digite a opção desejada: '))
    while not faux.op_escolha(opcao):
        opcao = int(input('Digite a opção desejada: '))
    return opcao
#----------------------------------------CADASTRO DE PRODUTO/SERVIÇO------------------------

def produto(produtos, estoque_inicial):
    nome = input('Digite o nome do produto: ').upper()
    while nome == '':
        nome = input('Nome vazio. Digite o nome novamente: ').upper()
        
    preco = float(input('Digite o valor do produto: '))
    while preco <= 0 and preco == '':
        preco = float(input('Erro. Digite o valor do produto novamente: '))
        
    quantidade = int(input('Digite a quantidade presente em estoque: '))
    while quantidade <= 0:
        quantidade = int(input('Erro, valor inválido. Digite a quantidade presente em estoque: '))

    estoque_inicial.append({
        'produto': nome,
        'estoque': quantidade
    })

    produtos.append({
        'nome': nome,
        'valor': preco,
        'estoque': quantidade
    })

def servico(servicos):
    nome = input('Digite o nome do serviço: ').upper()
    while nome == '':
        nome = input('Nome vazio. Digite o nome novamente: ').upper()
        
    preco = float(input('Digite o valor do serviço: '))
    while preco <= 0 and preco == '':
        preco = float(input('Erro. Digite o valor do serviço novamente: '))
        
    qntd = int(input('Digite a quantidade de horários disponíveis para esse serviço: '))
    horas = []
    for i in range(qntd):
        hora = input(f'Digite o {1+i}º horário[formato: 00:00]: ')
        while not faux.hora(hora):
            hora = input(f'Digite o {1+i}º horário[formato: 00:00]: ')
        situação = 'disponivel'
        
        horas.append([hora, situação])
        
    servicos.append({
        'nome': nome,
        'valor': preco,
        'horarios': horas
    })

def cadastra_produto_servico(servicos, estoque_inicial, produtos):
    cadastrar = int(input('Deseja cadastrar produto[1] ou serviço[2]: '))
    while cadastrar != 1 and cadastrar != 2:
        print('Opção inválida.')
        cadastrar = int(input('Deseja cadastrar produto[1] ou serviço[2]: '))
        
    if cadastrar == 1:
        produto(produtos, estoque_inicial)
        print('Produto cadastrado com sucesso!')
        
    elif cadastrar == 2:
        servico(servicos)
        print('Serviço cadastrado com sucesso!')

#-----------------------------BACKUP PRODUTOS/SERVICOS---------------------------------------

def backup_produto(produtos):
    arquivo = open('Produtos.txt', 'w')
    for produto in produtos:
        arquivo.write(f'{produto['nome']} : {produto['valor']} - {produto['estoque']}\n')
    
    arquivo.close()
    
def backup_servico(servicos):
    arquivo = open('Servicos e horarios.txt', 'w')
    for servico in servicos:
        for i in range(len(servico['horarios'])):
            arquivo.write(f'{servico['nome']} - {servico['valor']} - {servico['horarios'][i][0]} - {servico['horarios'][i][1]}\n')
    
    arquivo.close()
    
def backup_estoque(estoque_inicial):
    arquivo = open('Estoque Inicial.txt', 'w')
    for item in estoque_inicial:
        arquivo.write(f'{item['produto']} : {item['estoque']}\n')
    arquivo.close()

def backup_cupom(cupons):
    arquivo = open('Cupom.txt', 'w')
    for cupom in cupons:
        arquivo.write(f'{cupom['cupom']} : {cupom['desconto']}\n')
    
    arquivo.close()

def backup_produto_servico(produtos, servicos, estoque_inicial, cupons):

    backup_produto(produtos)
    backup_estoque(estoque_inicial)
    print('Backup de produtos feito com sucesso!')
    
    backup_servico(servicos)
    print('Backup de serviços feit com sucesso!')
    
    backup_cupom(cupons)
    print('Backup de cupons feito com sucesso!')

# ------------------------- IMPORTAR PRODUTOS/SERVIÇOS--------------------------------------

def importar_produto(produtos):
    arquivo = open('Produtos.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        linha = linha.replace(' : ', ' - ')
        if len(linha) > 0:
            
            linha = linha.split(' - ')
            igual = False
            for produto in produtos:
                if linha[0] == produto['nome'] and float(linha[1]) == produto['valor'] and int(linha[2]) == produto['estoque']:
                    igual = True
                    break
                
            if igual:
                continue
            
            nome = linha[0]
            preco = float(linha[1])
            quantidade = int(linha[2])
            
            produtos.append({
                'nome': nome,
                'valor': preco,
                'estoque': quantidade
            })
    arquivo.close()

def importar_estoque(estoque_inicial):
    arquivo = open('Estoque Inicial.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        linha = linha.replace(' : ', ' - ')
        if len(linha) > 0:
            
            linha = linha.split(' - ')
            igual = False
            for produtos in estoque_inicial:
                if linha[0] == produtos['produto'] and linha[1] == produtos['estoque']:
                    igual = True
                    break
            
            if igual:
                continue
            
            nome = linha[0]
            quantidade = int(linha[1])
            
            estoque_inicial.append({
                'produto': nome,
                'estoque': quantidade
            })
            
    arquivo.close()
    
def importar_servicos(servicos):
    arquivo = open('Servicos e Horarios.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        if len(linha) > 0:
            
            linha = linha.split(' - ')
            igual = False
            for servico in servicos:
                if linha[0] == servico['nome'] and float(linha[1]) == servico['valor']:
                    igual = True
                    break
            
            if igual:
                continue
            
            horas = []
            nome = linha[0]
            preco = float(linha[1])
            hora = linha[2]
            situacao = linha[3]
            
            horas.append([hora, situacao])
            
            servicos.append({
                'nome': nome,
                'valor': preco,
                'horarios': horas
            })
            
    arquivo.close()
    
def importar_cupons(cupons):
    arquivo = open('Cupom.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        if len(linha) > 0:
            linha = linha.split(' : ')
            igual = False
            for cupom in cupons:
                if linha[0] == cupom['cupom'] and int(linha[1]) == cupom['desconto']:
                    igual = True
                    break
            
            if igual:
                continue
            
            nome_cupom = linha[0]
            desconto = int(linha[1])
            
            cupons.append({
                'cupom': nome_cupom,
                'desconto': desconto
            })
    
def importar_produto_servico(produtos, servicos, estoque_inicial, cupons):
    importar_produto(produtos)
    
    importar_estoque(estoque_inicial)
    
    importar_cupons(cupons)
    
    importar_servicos(servicos)
    print('Produtos e serviços armazenados com sucesso!')
    
#---------------------------BUSCA----------------------------------------------------------

def busca_produto(produtos):
    procura = input('Digite o nome do produto que procuras: ').upper()
    while not faux.procura(procura):
        procura = input('Digite o nome do produto que procuras: ').upper()
    if len(produtos) > 0:
        for produto in produtos:
            if produto['nome'] == procura:
                print(f'{produto['nome']} | Valor: {produto['valor']}0 R$ | Estoque: {produto['estoque']}')
    else:
        print('Nenhum produto cadastrado.')
                
def busca_servico(servicos):
    procura = input('Digite o nome do serviço que procuras: ').upper()
    while not faux.procura(procura):
        procura = input('Digite o nome do serviço que procuras: ').upper()
    
    if len(servicos) > 0:
        for servico in servicos:
            if servico['nome'] == procura:
                print(servico['nome'])
                print(f'Valor: {servico['valor']}')
                print(f'Horários:')
                for horario in servico['horarios']:
                    print(f'{horario[0]} horas | Situação: {horario[1]}')
    else:
        print('Nenhum serviço cadastrado.')
    
def busca_produto_servico(produtos, servicos):
    buscar = int(input('Deseja buscar produto[1] ou serviço[2]: '))
    while buscar != 1 and buscar != 2:
        print('Opção inválida.')
        buscar = int(input('Deseja buscar produto[1] ou serviço[2]: '))
    
    if buscar == 1:
        busca_produto(produtos)
        
    elif buscar == 2:
        busca_servico(servicos)

#----------------------ATUALIZAR-----------------------------------------------------------

def atualizar_produto(produtos):
    print('Produtos:')
    for produto in produtos:
        print(f'{produto['nome']} | Valor: {produto['valor']}0 R$ | Estoque: {produto['estoque']}')
    
    item = input('Digite o nome do produto que deseja alterar: ').upper()
    while not faux.item(item):
        item = input('Digite o nome do produto que deseja alterar: ').upper()
    for produto in produtos:
        if produto['nome'] == item:
            
            alterar = int(input('Deseja alterar nome[1], valor[2], estoque[3]: '))
            while alterar != 1 and alterar != 2 and alterar != 3:
                print('Opções fora das ofertadas.')
                alterar = int(input('Deseja alterar nome[1], valor[2], estoque[3]: '))
            
            if alterar == 1:
                novo_nome = input('Digite o novo nome: ').upper()
                while novo_nome == '':
                    print('Valor vazio')
                    novo_nome = input('Digite o novo nome: ').upper()
                
                produto['nome'] = novo_nome
                print('Nome alterado com sucesso!')
            
            elif alterar == 2:
                novo_valor = float(input('Digite o novo valor do produto: '))
                while novo_valor <= 0:
                    print('Valor zero ou negativo.')
                    novo_valor = float(input('Digite o novo valor do produto: '))
                
                produto['valor'] = novo_valor
                print('Valor alterado com sucesso!')
            
            elif alterar == 3:
                nova_quantidade = int(input('Digite a nova quantidade de unidades do produto no estoque: '))
                while nova_quantidade < 0:
                    print('Valor negativo.')
                    nova_quantidade = int(input('Digite a nova quantidade de unidades do produto no estoque: '))
                
                produto['estoque'] = nova_quantidade
                print('Estoque alterado com sucesso!')
                
def atualizar_servico(servicos):
    print('Serviços:')
    for servico in servicos:
        print(f'{servico['nome']} - Valor:{servico['valor']}')
        print('Horários:')
        for horario in servico['horarios']:
            print(f'{horario[0]} horas - {horario[1]}')
    
    service = input('Digite o nome do serviço que deseja alterar: ').upper()
    while not faux.item(service):
        service = input('Digite o nome do produto que deseja alterar: ').upper()
    
    for servico in servicos:
        if servico['nome'] == service:
            
            alterar = int(input('Deseja alterar nome[1], valor[2], horarios[3]: '))
            while alterar != 1 and alterar != 2 and alterar != 3:
                print('Opções fora das ofertadas.')
                alterar = int(input('Deseja alterar nome[1], valor[2], horarios[3]: '))
                
            if alterar == 1:
                novo_nome = input('Digite o novo nome: ').upper()
                while novo_nome == '':
                    print('Valor vazio')
                    novo_nome = input('Digite o novo nome: ').upper()
                
                servico['nome'] = novo_nome
                print('Nome do serviço alterado com sucesso!')
            
            elif alterar == 2:
                novo_valor = float(input('Digite o novo valor do produto: '))
                while novo_valor <= 0:
                    print('Valor zero ou negativo.')
                    novo_valor = float(input('Digite o novo valor do produto: '))
                
                servico['valor'] = novo_valor
                print('Valor alterado com sucesso!')
            
            elif alterar == 3:
                for horario in servico['horarios']:
                    print(f'Hora: {horario[0]}')
                hora = input('Digite a hora que deseja alterar[formato 00:00]: ')
                for horario in servico['horarios']:
                    if horario[0] == hora:
                        novo_horario = input('Digite o novo horário[formato 00:00]: ')
                        
                        horario[0] = novo_horario
                        print('Horario alterado com sucesso!')
                        
def atualizar_produto_servico(produtos, servicos):
    atualizar = int(input('Deseja atualizar produto[1] ou serviço[2]: '))
    while atualizar != 1 and atualizar != 2:
        print('Opção inválida.')
        atualizar = int(input('Deseja atualizar produto[1] ou serviço[2]: '))
    
    if atualizar == 1:
        atualizar_produto(produtos)
        
    elif atualizar == 2:
        atualizar_servico(servicos)
    
#---------------------------REMOVER-------------------------------------------------------

def remover_produto(produtos, estoque_inicial):
    print('Produtos cadastrados:')
    for i in range(len(produtos)):
        print(f'{i} - {produtos[i]}')
    
    indice = int(input('Digite o índice do produto que deseja remover: '))
    while not faux.indice(indice, produtos):
        indice = int(input('Digite o índice do produto que deseja remover: '))
    
    produtos.pop(indice)
    estoque_inicial.pop(indice)
    print('Produto removido com sucesso!')
    
def remover_servico(servicos):
    print('serviços cadastrados:')
    for i in range(len(servicos)):
        print(f'{i} - {servicos[i]['nome']}')
    
    indice = int(input('Digite o índice do produto que deseja remover: '))
    while not faux.indice(indice, servicos):
        indice = int(input('Digite o índice do produto que deseja remover: '))
        
    servicos.pop(indice)
    print('Serviço removido com sucesso!')
    
def remover_produto_servico(produtos, servicos, estoque_inicial):
    remover = int(input('Deseja atualizar produto[1] ou serviço[2]: '))
    while remover != 1 and remover != 2:
        print('Opção inválida.')
        remover = int(input('Deseja atualizar produto[1] ou serviço[2]: '))
    
    if remover == 1:
        remover_produto(produtos, estoque_inicial)
        
    elif remover == 2:
        remover_servico(servicos)

#-------------------------ANALISE DE ESTOQUE----------------------------------------------         
        
def analise_de_estoque(produtos, estoque_inicial):
    for p in range(len(produtos)):
        estoque_atual = produtos[p]['estoque']
        estoque_original = estoque_inicial[p]['estoque']
        
        produto_vendido = estoque_original - estoque_atual
        
        print(f'Produto: {produtos[p]['nome']}')
        print(f'Estoque Inicial: {estoque_original}')
        print(f'Estoque_atual: {estoque_atual}')
        
        print(f'Total vendido: {produto_vendido} unidades')
        
#-----------------------CRIAR/ATUALIZAR/REMOVER CUMPO-----------------------------------

def criar_cupom(cupons):
    nome_cupom = input('Digite o nome do cupom que deseja criar[Seja Criativo!]: ').upper()
    while not faux.cupom_igual(nome_cupom, cupons):
        nome_cupom = input('Digite o nome do cupom que deseja criar[Seja Criativo!]: ').upper()
    
    desconto = int(input('Digite o valor do desconto que o cupom irá oferecer: '))
    while desconto <= 0 or desconto >= 100:
        print('Valor de desconto inválido.')
        desconto = int(input('Digite o valor do desconto que o cupom irá oferecer: '))
        
    cupons.append({
        'cupom': nome_cupom,
        'desconto': desconto
    })
    print('Cupom criado com sucesso!')
    
def atualizar_cupom(cupons):
    print('Cupons cadastrados:')
    for cupom in cupons:
        print(f'{cupom['cupom']} - {cupom['desconto']}%')
    
    cupom_alterar = input('Digite o nome do cupom que deseja alterar: ').upper()
    for cupom in cupons:
        if cupom['cupom'] == cupom_alterar:
            
            alterar = int(input('Deseja alterar nome[1] ou valor do desconto[2]: '))
            while alterar != 1 and alterar != 2:
                alterar = int(input('Deseja alterar nome[1] ou valor do desconto[2]: '))
            
            if alterar == 1:
                novo_nome = input('Digite o novo nome do cupom: ').upper()
                while novo_nome == '':
                    print('Valor vazio')
                    novo_nome = input('Digite o novo nome: ').upper()
                
                cupom['cupom'] = novo_nome
                print('Nome alterado com sucesso!')
                
            
            if alterar == 2:
                novo_valor = int(input('Digite o novo valor do seu cupom: '))
                while novo_valor <= 0 or novo_valor >= 100:
                    print('Valor de desconto inválido.')
                    novo_valor = float(input('Digite o novo valor do produto: '))
                
                cupom['desconto'] = novo_valor
                print('Valor alterado com sucesso!')
                
def remover_cupom(cupons):
    print('Cupons cadastrados:')
    for i in range(len(cupons)):
        print(f'{i} - {cupons[i]['cupom']}')
    
    indice = int(input('Digite o índice do produto que deseja remover: '))
    while not faux.indice(indice, cupons):
        indice = int(input('Digite o índice do produto que deseja remover: '))
    
    cupons.pop(indice)
    print('Cupom removido com sucesso!')
    
#--------------------------COMPRAR PRODUTO/SERVIÇO----------------------------------------

def comprar_produto(produtos, carrinho):
    if len(produtos) == 0:
        print('Nenhum produto disponível.')
        return

    print('--- PRODUTOS ---')
    i = 0
    for p in produtos:
        print(f'{i} - {p["nome"]} | R$ {p["valor"]} | Estoque: {p["estoque"]}')
        i += 1

    indice = int(input('Digite o índice do produto: '))
    while indice < 0 or indice >= len(produtos):
        print('Índice inválido.')
        indice = int(input('Digite o índice do produto: '))

    qtd = int(input('Quantidade desejada: '))
    while qtd <= 0 or qtd > produtos[indice]['estoque']:
        print('Quantidade inválida.')
        qtd = int(input('Quantidade desejada: '))

    total = qtd * produtos[indice]['valor']
    carrinho.append({
        'nome': produtos[indice]['nome'],
        'quantidade': qtd,
        'total': total
    })

    produtos[indice]['estoque'] -= qtd
    print('Produto adicionado ao carrinho.')
    
def agendar_servico(servicos, agendamentos):
    if len(servicos) == 0:
        print('Nenhum serviço disponível.')
        return
    
    print('--- SERVIÇOS ---')
    i = 0
    for s in servicos:
        print(f'{i} - {s["nome"]} | R$ {s["valor"]}')
        i += 1

    indice = int(input('Digite o índice do serviço: '))
    while indice < 0 or indice >= len(servicos):
        print('Índice inválido.')
        indice = int(input('Digite o índice do serviço: '))
    
    horarios = servicos[indice]['horarios']
    disponiveis = []

    print('Horários disponíveis:')
    j = 0
    for h in horarios:
        if h[1] == 'disponivel':
            print(f'{j} - {h[0]}')
            disponiveis.append(j)
        j += 1

    if len(disponiveis) == 0:
        print('Nenhum horário disponível.')
        return

    escolha = int(input('Escolha o horário: '))
    if escolha not in disponiveis:
        print('Horário inválido.')
        return

    horarios[escolha][1] = 'reservado'
    agendamentos.append({
        'servico': servicos[indice]['nome'],
        'hora': horarios[escolha][0]
    })

    print('Serviço agendado com sucesso!')

#--------------------------VER CARRINHO/AGENDA-------------------------------------------

def ver_carrinho(carrinho, cupons):
    if len(carrinho) == 0:
            print('Carrinho vazio.')
    else:
        total = 0
        for c in carrinho:
            print(f"{c['quantidade']}x {c['nome']} - R$ {c['total']}")
            total += c['total']
        print(f'Total da compra: R$ {total}')
        usar_cupom = input('Você possui cupom de desconto? [S/N]: ').upper()

        if usar_cupom == 'S':
            nome_cupom = input('Digite o nome do cupom: ').upper()
            cupom_encontrado = False

            for cupom in cupons:
                if cupom['cupom'] == nome_cupom:
                    desconto = cupom['desconto']
                    valor_desconto = total * desconto / 100
                    total = total - valor_desconto

                    print(f'Cupom aplicado: {desconto}% de desconto')
                    print(f'Valor do desconto: R$ {valor_desconto}')
                    print(f'Valor final do produto com desconto: R$ {total}')
                    cupom_encontrado = True
                    break

            if not cupom_encontrado:
                print('Cupom inválido ou inexistente.')
                
        finalizar = input('Finalizar compra? [S/N]: ').upper()
        if finalizar == 'S':
            carrinho.clear()
            print('Compra finalizada.')
            
            
def ver_servicos(agendamentos):
    if len(agendamentos) == 0:
        print('Nenhum agendamento.')
    else:
        for a in agendamentos:
            print(f"{a['servico']} às {a['hora']}")

#--------------------------SALVAR CARRINHO/AGENDA------------------------------------------

def salvar_carrinho_txt(carrinho):
    arquivo = open('compras_cliente.txt', 'w')
    
    for c in carrinho:
        arquivo.write(f"{c['nome']} - {c['quantidade']} unidades - R$ {c['total']}\n")
        
    arquivo.close()

def salvar_agenda_txt(agendamentos):
    arquivo = open('agendamentos_cliente.txt', 'w')
    
    for a in agendamentos:
        
        arquivo.write(f"{a['servico']} - {a['hora']}\n")
    arquivo.close()

def salvar_compras_agendamentos(carrinho, agendamentos):
    salvar_carrinho_txt(carrinho)
    salvar_agenda_txt(agendamentos)

    print('Produtos e serviços agendandos salvos para comprar quando quiser!')
    print('Ao retornar para comprar, antes de finalizar sua compra ou ver serviços, restaure seu carrinho e agenda usando a opção 6!')
    
#--------------------------------IMPORTAR CARRINHO/AGENDA--------------------------------------

def importar_carrinho(carrinho):
    arquivo = open('Compras_cliente.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        linha = linha.replace('unidades ', '')
        linha = linha.replace('R$ ', '')
        if len(linha) > 0:
            
            linha = linha.split(' - ')
            igual = False
            for produto in carrinho:
                if linha[0] == produto['nome'] and int(linha[1]) == produto['quantidade'] and float(linha[3]) == produto['total']:
                    igual = True
                    break
            
            if igual:
                continue
            
            nome = linha[0]
            quantidade = int(linha[1])
            total = float(linha[2])
            
            carrinho.append({
            'nome': nome,
            'quantidade': quantidade,
            'total': total
        })
    
    arquivo.close()
            
def importar_agenda(agendamentos):
    arquivo = open('agendamentos_cliente.txt', 'r')
    linhas = arquivo.readlines()
    
    for linha in linhas:
        linha = linha.replace('\n', '')
        if len(linha) > 0:
            
            linha = linha.split(' - ')
            igual = False
            for servico in agendamentos:
                if linha[0] == servico['servico'] and linha[1] == servico['hora']:
                    igual = True
                    break
                
            if igual:
                continue
            
            servico = linha[0]
            hora = linha[1]
            agendamentos.append({
            'servico': servico,
            'hora': hora
        })
    
    arquivo.close()
    
def importar_agenda_carrinho(carrinho, agendamentos):
    importar_carrinho(carrinho)
    
    importar_agenda(agendamentos)
    
    print('Seu carrinho e agenda foram restaurados.')
    print('Caso adicione mais produtos e agende mais serviços, utilize a opção 5 para salvar todos os seus produtos e não perca nada!')