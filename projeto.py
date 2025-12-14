import funcoes_adm as admin

adm = [
    {'nome': 'Eric', 'email': 'ericafonso@gmail.com', 'senha': 'erico12345', 'id': '12345678901', 'tipo': 'admin'}
]

usuarios = [
    {'nome': 'Joaquim', 'email': 'jurupeba@gmail.com', 'senha': 'pebinha123', 'tipo': 'cliente'}
]

produtos = [
    {'nome': 'SHAMPOO', 'valor': 12.0, 'estoque': 50},
    {'nome': 'PERFUME', 'valor': 25.0, 'estoque': 100},
    {'nome': 'RACAO PEDIGREE', 'valor': 40.0, 'estoque': 75}
]

servicos = [
    {'nome': 'BANHO', 'valor': 30.0, 'horarios': [['13:00', 'disponivel'], ['11:00', 'disponivel']]},
    {'nome': 'SPA', 'valor': 100.0, 'horarios': [['15:00', 'disponivel']]},
    {'nome': 'AULA DE ADESTRAMENTO', 'valor': 1200.0, 'horarios': [['19:00', 'disponivel'], ['12:00', 'disponivel']]}
]

cupons = [
    {'cupom': 'NAVALHA001', 'desconto': 30},
    {'cupom': 'TIRATIRA100', 'desconto': 20},
    {'cupom': 'FELIZNATAL', 'desconto': 60},
    {'cupom': 'BLACKFRIDAY', 'desconto': 80}
]

estoque_inicial = [
    {'produto': 'SHAMPOO', 'estoque': 50},
    {'produto': 'PERFUME', 'estoque': 100},
    {'produto': 'RACAO PEDIGREE', 'estoque': 75}
]

opc = 90000
print('BEM VINDO AO PETSERTÃO - O MELHOR SERVIÇO DE ATENDIMENTO A ANIMAIS DA REGIÃO!!!!!')
while opc != 0:
    opc = admin.mostra_menu()

    if opc == 1:
        admin.cadastrar(usuarios, adm)
    
    elif opc == 2:
        admin.importar_backup_para_lista(adm, usuarios)
    
    elif opc == 3:
        admin.fazer_backup_para_arquivo(adm, usuarios)
    
    elif opc == 4:
        print('--- ÁREA DO ADMIN ---')
        while True:
            logado = admin.login_adm(adm)

            if logado:
                print('Entrando no menu de operações...')
                break
            
            else:
                print('Usuário não encontrado. Tente novamente.')
        
        while True:
            escolha_adm = admin.operacoes_menu_admin()
                
            if escolha_adm == 1:
                admin.cadastra_produto_servico(servicos, estoque_inicial, produtos)

            elif escolha_adm == 2:
                admin.importar_produto_servico(produtos, servicos, estoque_inicial)

            elif escolha_adm == 3:
                admin.backup_produto_servico(produtos, servicos, estoque_inicial, cupons)

            elif escolha_adm == 4:
                while True:
                    escolha = int(input('Deseja buscar[1] / atualizar[2] / remover[3] / voltar[0]: '))
                    while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 0:
                        print('Opção fora das oferecidas.')
                        escolha = int(input('Deseja buscar[1]/atualizar[2]/remover[3]: '))
                        
                    if escolha == 1:
                        admin.busca_produto_servico(produtos, servicos)
                        
                    elif escolha == 2:
                        admin.atualizar_produto_servico(produtos, servicos)
                        
                    elif escolha == 3:
                        admin.remover_produto_servico(produtos, servicos, estoque_inicial)
                        
                    elif escolha == 0:
                        print('Voltando ao menu anterior..')
                        break
                    
            elif escolha_adm == 5:
                admin.analise_de_estoque(produtos, estoque_inicial)
                
            elif escolha_adm == 6:
                admin.criar_cupom(cupons)
            
            elif escolha_adm == 7:
                while True:
                    escolha = int(input('Deseja atualizar[1] / remover[2] / voltar[0]: '))
                    while escolha != 1 and escolha != 2 and escolha != 0:
                        print('Opção fora das oferecidas.')
                        escolha = int(input('Deseja atualizar[1] / remover[2] / voltar[0]: '))
                        
                    if escolha == 1:
                        admin.atualizar_cupom(cupons)
                        
                    elif escolha == 2:
                        admin.remover_cupom(cupons)
                           
    elif opc == 5:
        print('--- ÁREA DO CLIENTE ---')
        while True:
            logado = admin.login_cliente(usuarios)
            if logado:
                print('Bem-vindo(a) ao PetSertão!')
                break
            else:
                print('Não encontramos o seu login.')

        carrinho = []  
        agendamentos = []

        while True:
            escolha_cliente = admin.opercacoes_menu_cliente()
            
            if escolha_cliente == 1:
                admin.comprar_produto(produtos, carrinho)
            
            elif escolha_cliente == 2:
                admin.agendar_servico(servicos, agendamentos)
                
            elif escolha_cliente == 3:
                admin.ver_carrinho(carrinho, cupons)
                
            elif escolha_cliente == 4:
                admin.ver_servicos(agendamentos)
            
            elif escolha_cliente == 5:
                admin.salvar_compras_agendamentos(carrinho, agendamentos)
                
            elif escolha_cliente == 6:
                admin.importar_agenda_carrinho(carrinho, agendamentos)
                
            elif escolha_cliente == 0:
                print('Voltando ao menu anterior..')
                break