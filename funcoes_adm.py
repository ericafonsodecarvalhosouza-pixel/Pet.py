import funcoes_auxiliares as faux

def cadastrar_usuário(usuarios):
    login = input('Digite o seu E-mail: ')
    while (not faux.verificar_email(login)) or (not faux.copia_login(usuarios, login)):
        login = input('Digite seu E-mail, novamente: ')
        
    senha = input('Digite a sua senha (Mínimo 8 caracteres): ')
    while (not faux.verificar_senha(senha)) or (not faux.copia_senha(usuarios, senha)):
        senha = input('Digite sua sennha novamente: ')
    
    usuarios.append([login, senha])
    
def cadastrar_admin(adm):
    login = input('Digite o seu e-mail para cadastro: ')
    while (not faux.verificar_email(login)) or (not faux.copia_login_adm(adm, login)):
       login = input('Digite o seu e-mail para cadastro: ')
       
    senha = input('Digite sua senha para cadastro: ')
    while (not faux.verificar_senha(senha)) or (not faux.copia_senha_adm(adm, senha)):
         senha = input('Digite sua senha para cadastro: ')
        
    id_verify = (input('Crie o seu ID de verificação para cadastro, contendo apenas números: '))
    while (not faux.verificar_id_adm(id_verify)) or (not faux.copia_id(adm, id_verify)):
        id_verify = (input('Digite o seu ID de verificação: '))
        
    adm.append([login, senha, id_verify])