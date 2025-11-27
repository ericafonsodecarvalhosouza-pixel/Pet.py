def verificar_email_usuário(login):
    if "@" not in login:
        print('E-mail sem "@".')
        return False
    
    if 'gmail' not in login and 'hotmail' not in login and 'outlook' not in login:
        print('O seu E-mail não apresenta os domínios aceitos[gmail, hotmail, outlook]')
        return False
    
    if '.com' not in login:
        print('O seu E-mail está faltando ".com".')
        return False
    
    return True

def verificar_senha_usuário(senha):
    if len(senha) < 8:
        print('Digite uma senha com um mínimo de 8 caracteres.')
        return False
    
    return True



def verificar_email_adm(login_adm):
    if "@" not in login_adm:
        print('E-mail sem "@".')
        return False
    
    if 'gmail' not in login_adm and 'hotmail' not in login_adm and 'outlook' not in login_adm:
        print('O seu E-mail não apresenta os domínios aceitos[gmail, hotmail, outlook]')
        return False
    
    if '.com' not in login_adm:
        print('O seu E-mail está faltando ".com".')
        return False
    
    return True