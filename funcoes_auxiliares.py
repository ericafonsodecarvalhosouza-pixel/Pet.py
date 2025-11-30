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
        if login == i[0]:
            print('Esse e-mail já foi cadastrado.')
            return False
    
    return True
            
def copia_senha(usuarios, senha):
    for i in usuarios:
        if senha == i[1]:
            print('Essa senha já foi cadastrada.')
            return False
        
    return True

def copia_login_adm(adm, login):
    for i in adm:
        if login == i[0]:
            print('Esse e-mail já foi cadastrado.')
            return False
    
    return True

def copia_senha_adm(adm, senha):
    for i in adm:
        if senha == i[1]:
            print('Essa senha já foi cadastrada.')
            return False
        
    return True

def copia_id(adm, id_verify):
    for i in adm:
        if id_verify == i[2]:
            print('Esse id já foi cadastrado.')
            return False
        
    return True