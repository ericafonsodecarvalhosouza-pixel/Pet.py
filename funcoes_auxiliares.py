def verificar_email(login):
    simbolos = "',:;{ }[]() "
    
    if login == "":
        print('E-mail vazio.')
        return False
    
    if "@" not in login:
        print('E-mail sem "@".')
        return False
    
    if 'gmail' not in login and 'hotmail' not in login and 'outlook' not in login:
        print('O seu E-mail não apresenta os domínios aceitos[gmail, hotmail, outlook]')
        return False
    
    if '.com' not in login:
        print('O seu E-mail está faltando ".com".')
        return False
    
    for s in simbolos:
        if s in login:
            print('Texto contém algum símbolo que não é permitido em e-mails')
            return False
    
    return True

def verificar_senha(senha):
    simbolos = "',:;{ }[]() "
    for s in simbolos:
        if s in senha:
            print('Símbolos nao são aceitos em senhas para cadastro no petshop.')
            return False
    
    if senha == "":
        print('Senha vazia.')
        return False

    if len(senha) < 8:
        print('Digite uma senha com um mínimo de 8 caracteres.')
        return False
    
    return True

def verificar_id_adm(id_verify):
    simbolos = "',:;{ }[]() "
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for s in simbolos:
        if s in id_verify:
            print('Símbolos nao são aceitos no id de verificação para cadastro no petshop.')
            return False
    
    for letras in abc:
        if letras in id_verify:
            print('Id não pode conter letras, apenas números.')
            return False
    
    if id_verify == "":
        print('Id de verificação vazio.')
        return False

    if len(id_verify) < 10:
        print('Digite um id de verificação com um mínimo de 8 caracteres.')
        return False
    
    return True
    
def copia_login(usuarios, login):
    for i in usuarios:
        if login == i['email']:
            print('Esse e-mail já foi cadastrado.')
            return False
    
    return True
            
def copia_senha(usuarios, senha):
    for i in usuarios:
        if senha == i['senha']:
            print('Essa senha já foi cadastrada.')
            return False
        
    return True

def copia_login_adm(adm, login):
    for i in adm:
        if login == i['email']:
            print('Esse e-mail já foi cadastrado.')
            return False
    
    return True

def copia_senha_adm(adm, senha):
    for i in adm:
        if senha == i['senha']:
            print('Essa senha já foi cadastrada.')
            return False
        
    return True

def copia_id(adm, id_verify):
    for i in adm:
        if id_verify == i['id']:
            print('Esse id já foi cadastrado.')
            return False
        
    return True

def opc_ver(opcao):
    escolhas_menu = [1, 2, 3, 4, 5]
    if opcao not in escolhas_menu:
        return False
    
    return True

def ver_tipo(tipo_cadastro):
    simbolos = "',:;{ }[]() "
    for s in simbolos:
        if s in tipo_cadastro:
            print('O tipo não possui simbolos.')
            return False
    if tipo_cadastro == '':
        print('Sem informação, espaço vazio.')
        return False
    
    return True

def op_escolha(opcao):
    opcoes = [1, 2, 3, 4, 5, 6, 7, 0]
    if opcao not in opcoes:
        print('Digite uma opção válida.')
        return False
        
    return True

def vazio(busca):
    if busca == '':
        print('Espaço vazio. Digite uma informação válida.')
        return False
    
    return True

def nome(nome):
    simbolos = "',:;{ }[]() - _ = +  / * "
    num = ['1','2','3','4','5','6','7','8','9','0']
    
    if simbolos in nome:
        print('Nome não contém símbolos')
        return False
    
    if nome == '':
        print('Nome vazio')
        return False
    
    for n in num:
        if n in nome:
            print('Nome não contém números.')
            return False
        
    return True

def hora(hora):
    simbolos = "',:;{ }[]() - _ = +  / * "
    abc = 'abcdefghijklmnopqrstuvwxyz'
    
    if simbolos in hora:
        print('Hora não contém símbolos')
        return False
    
    if hora == '':
        print('Horário vazio')
        return False
    

    if abc in hora:
        print('Hora não contém letras.')
        return False
        
    return True

def procura(procura):
    num = ['1','2','3','4','5','6','7','8','9','0']
    if procura == '':
        print('Valor vazio.')
        return False
    
    for n in num:
        if n in procura:
            print('Nome não possui numerais.')
            return False
        
    
    return True

def item(item):
    num = ['1','2','3','4','5','6','7','8','9','0']
    if item == '':
        print('Valor vazio.')
        return False
    
    for n in num:
        if n in item:
            print('Nome não possui numerais.')
            return False
        
    
    return True

def item(service):
    num = ['1','2','3','4','5','6','7','8','9','0']
    if service == '':
        print('Valor vazio.')
        return False
    
    for n in num:
        if n in service:
            print('Nome não possui numerais.')
            return False
        
    
    return True

def indice(indice, produtos):
    if len(produtos) < indice:
        print('Indice digitado menor que o presente na lista.')
        return False
    
    if len(produtos) < indice:
        print('Indice digitado maior que o presente na lista.')
        return False
    
    if indice < 0:
        print('Digite um indice maior ou igual a zero.')
        return False
    
    
    return True

def indice(indice, servicos):
    if len(servicos) < indice:
        print('Indice digitado menor que o presente na lista.')
        return False
    
    if len(servicos) < indice:
        print('Indice digitado maior que o presente na lista.')
        return False
    
    if indice < 0:
        print('Digite um indice maior ou igual a zero.')
        return False
    
    
    return True

def cupom_igual(nome_cupom, cupons):
    for cupom in cupons:
        if cupons['cupom'] == nome_cupom:
            print('Cupom já existente.')
            return False
        
    return True

def indice(indice, cupons):
    if len(cupons) < indice:
        print('Indice digitado menor que o presente na lista.')
        return False
    
    if len(cupons) < indice:
        print('Indice digitado maior que o presente na lista.')
        return False
    
    if indice < 0:
        print('Digite um indice maior ou igual a zero.')
        return False
    
    
    return True
