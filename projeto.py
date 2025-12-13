import funcoes_adm as admin

adm = [
    {'nome': 'Eric', 'email': 'ericafonso@gmail.com', 'senha': 'erico12345', 'id': '12345678901', 'tipo': 'admin'}
]

usuarios = []

produtos = [
    {'nome': 'SHAMPOO', 'valor': 12.0, 'estoque': 50},
    {'nome': 'PERFUME', 'valor': 25.0, 'estoque': 100},
    {'nome': 'RACAO PEDIGREE', 'valor': 40.0, 'estoque': 75}
]

servicos = [
    {'nome': 'BANHO', 'valor': 30.0, 'horarios': [['13:00', 'disponivel'], ['11:00', 'disponível']]},
    {'nome': 'SPA', 'valor': 100.0, 'horarios': [['15:00', 'disponivel']]},
    {'nome': 'AULA DE ADESTRAMENTO', 'valor': 1200.0, 'horarios': [['19:00', 'disponivel'], ['12:00', 'disponível']]}
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
            logado = admin.login_usuario(usuarios)
            if logado:
                print('Bem-vindo(a) ao PetSertão!')
                break
            else:
                print('Não encontramos o seu login.')

        carrinho = []  
        agendamentos = []

        escolha_cliente = 99999

        while escolha_cliente != 0:
            print('----------- MENU CLIENTE -----------')
            print('1. Comprar produto')
            print('2. Agendar serviço')
            print('3. Ver carrinho')
            print('4. Ver meus agendamentos')
            print('0. Sair da área do cliente')

            escolha_cliente = int(input('Digite a opção desejada: '))

                
            if escolha_cliente == 1:
                while True:
                    if len(produtos) == 0:
                        print('Nenhum produto disponível no momento.')
                        break
                    else:
                        print('--- PRODUTOS DISPONÍVEIS ---')
                        for i in range(len(produtos)):
                            print(f'{i}. {produtos[i][0]} - R$ {produtos[i][1]} - Estoque: {produtos[i][2]}')

                        indice = int(input('Digite o índice do produto que deseja comprar: '))
                        while indice < 0 and indice > len(produtos):
                            print('Índice inválido.')
                            indice = int(input('Digite o índice do produto que deseja comprar: '))

                        qtd = int(input('Quantas unidades deseja comprar? '))
                        while qtd <= 0 and qtd > produtos[indice][2]:
                            print('Quantidade inválida ou quantidade maior que o estoque disponível!')
                            qtd = int(input('Quantas unidades deseja comprar? '))

                        total = produtos[indice][1] * qtd
                        carrinho.append([produtos[indice][0], qtd, total])
                        produtos[indice][2] -= qtd
                        print(f'{qtd} unidades de {produtos[indice][0]} adicionados ao carrinho. Total: R${total}')

                        escolha = input('Deseja continuar comprando? Sim[S] ou Não[N]: ').upper()
                        while escolha != 'S' and escolha != 'N':
                            print('Opção inválida!. Tente novamente.')
                            escolha = input('Deseja continuar comprando? Sim[S] ou Não[N]: ').upper()
                        if escolha == 'N':
                            break
            
            elif escolha_cliente == 2:
                if len(servicos) == 0:
                    print('Nenhum serviço disponível no momento.')
                else:
                    print('--- SERVIÇOS DISPONÍVEIS ---')
                    for i in range(len(servicos)):
                        print(f'{i}. {servicos[i][0]} - R$ {servicos[i][1]}')

                    indice_serv = int(input('Digite o índice do serviço que deseja agendar: '))
                    while indice_serv < 0 or indice_serv >= len(servicos):
                        print('Índice inválido.')
                        indice_serv = int(input('Digite o índice do serviço que deseja agendar: '))

                    print('Horários disponíveis:')
                    disponiveis = []
                    for i in range(len(servicos[indice_serv][2])):
                        h = servicos[indice_serv][2][i]
                        if h[1] == 'disponível':
                                print(f'{i} - {h[0]}:00')
                                disponiveis.append(i)

                        if not disponiveis:
                            print('Nenhum horário disponível.')
                        else:
                            indice_hora = int(input('Escolha o índice do horário desejado: '))
                            if indice_hora in disponiveis:
                                servicos[indice_serv][2][indice_hora][1] = 'reservado'
                                agendamentos.append([servicos[indice_serv][0], servicos[indice_serv][2][indice_hora][0]])
                                print('Serviço agendado com sucesso!')
                            else:
                                print('Horário inválido ou indisponível.')

            elif escolha_cliente == 3:
                if len(carrinho) == 0:
                    print('Carrinho vazio.')
                else:
                    print('--- ITENS NO SEU CARRINHO ---')
                    total_compra = 0
                    for item in carrinho:
                        print(f'{item[1]} unidades de {item[0]} - Total: R${item[2]}')
                        total_compra += item[2]
                    print(f'Valor total da compra: R${total_compra}')
                    finalizar = input('Deseja finalizar a compra? Sim[S] ou Não[N]: ').upper()
                    while finalizar != 'S' and finalizar != 'N':
                        print('Opção inválida! Tente novamente.')
                        finalizar = input('Deseja finalizar a compra? [Sim[S] ou Não[N]: ').upper()
                    if finalizar == 'S':
                        print('Compra finalizada com sucesso! Obrigado por comprar no PetSertão')
                        carrinho.clear()

            elif escolha_cliente == 4:
                if len(agendamentos) == 0:
                    print('Nenhum agendamento realizado.')
                else:
                    print('--- MEUS AGENDAMENTOS ---')
                    for a in agendamentos:
                        print(f'Serviço: {a[0]} - Horário: {a[1]}:00')


            elif escolha_cliente == 0:
                continue

            else:
                print('Opção inválida.')