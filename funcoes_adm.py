import funcoes_auxiliares as faux

def cadastrar_usuário(usuarios):
    login = input('Digite o seu E-mail: ')
    while not faux.verificar_email_usuário(login):
        login = input('Digite seu E-mail, novamente: ')
        
    senha = input('Digite a sua senha (Mínimo 8 caracteres): ')
    while not faux.verificar_senha_usuário(senha):
        senha = input('Digite sua sennha novamente: ')
    
    usuarios.append([login, senha])