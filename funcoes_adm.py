import funcoes_auxiliares as faux

def cadastrar_usuário(usuarios):
    login = input('Digite o seu E-mail: ').lower()
    while (not faux.verificar_email(login)) or (not faux.copia_login(usuarios, login)):
        login = input('Digite seu E-mail, novamente: ').lower()
        
    senha = input('Digite a sua senha (Mínimo 8 caracteres): ').lower()
    while (not faux.verificar_senha(senha)) or (not faux.copia_senha(usuarios, senha)):
        senha = input('Digite sua sennha novamente: ').lower()
        
    type = "cliente"
    
    usuarios.append([login, senha, type])
    
def cadastrar_admin(adm):
    login = input('Digite o seu e-mail para cadastro: ').lower()
    while (not faux.verificar_email(login)) or (not faux.copia_login_adm(adm, login)):
       login = input('Digite o seu e-mail para cadastro: ').lower()
       
    senha = input('Digite sua senha para cadastro: ').lower()
    while (not faux.verificar_senha(senha)) or (not faux.copia_senha_adm(adm, senha)):
         senha = input('Digite sua senha para cadastro: ').lower()
        
    id_verify = (input('Crie o seu ID de verificação para cadastro, contendo apenas números: ')).lower()
    while (not faux.verificar_id_adm(id_verify)) or (not faux.copia_id(adm, id_verify)):
        id_verify = (input('Digite o seu ID de verificação: ')).lower()
        
    type = "admin"
    
    adm.append([login, senha, id_verify, type])
    
def login_usuario(usuarios):
    login_ver = input('Digite o seu e-mail de cadastro: ')
    senha_ver = input('Digite sua senha: ')
    for us in usuarios:
        if us[0] == login_ver and us[1] == senha_ver:
            print('Logado com sucesso. Bem vindo ao PetSertão!')
            return True
        
def login_adm(adm):
    login_ver = input('Digite o seu e-mail de cadastro: ')
    id_ver = input('Digite seu id de verificação: ')
    for us in adm:
        if us[0] == login_ver and us[2] == id_ver:
            return True