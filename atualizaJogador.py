def atualiza():
    arquivo = open('Jogador.txt','r')
    conteudo = arquivo.readlines()
    q=j=0
    jogadores =[]
    for i in conteudo:
        if '*' not in i:
            jogador = i.replace('[','')
            jogador = jogador.replace(']','')
            jogador = jogador.replace('\n','')
            jogador = jogador.split(',')
        for j in range(9):
                if j != 0:
                    jogador[j] = int(jogador[j])
                else:
                    jogador[j] = jogador[j].replace('"','').replace("'\'",'').replace("'",'')
        jogadores.append(jogador)
    print(f'foram detectados {len(jogadores)} jogadores \nSelecione qual jogador deseja atualizar')
    i = 0
    for jogador in jogadores:
        print(f'[{i}]-{jogador[0]}')
        i+=1
    o = int(input('Digite o numero do Jogador: '))
    a = int(input('Selecione o atributo que deseja alterar \n[1]-Força\n[2]-Agilidade\n[3]-Velocidade\n[4]-Defesa\n[5]-Vida\n[6]-Poder\n[7]-Inteligencia\n[8]-Oculto\nAtributo: '))
    if a == 1:
        jogadores[o][a] = int(input(f'Digite o no novo valor para FORÇA do jogador {jogadores[o][0]}: '))
    elif a == 2:
        jogadores[o][a] = int(input(f'Digite o no novo valor para AGILIDADE do jogador {jogadores[o][0]}: '))
    elif a == 3:
        jogadores[o][a] = int(input(f'Digite o no novo valor para VELOCIDADE do jogador {jogadores[o][0]}: '))
    elif a == 4:
        jogadores[o][a] = int(input(f'Digite o no novo valor para DEFESA do jogador {jogadores[o][0]}: '))
    elif a == 5:
        jogadores[o][a] = int(input(f'Digite o no novo valor para VIDA do jogador {jogadores[o][0]}: '))
    elif a == 6:
        jogadores[o][a] = int(input(f'Digite o no novo valor para PODER do jogador {jogadores[o][0]}: '))
    elif a == 7:
        jogadores[o][a] = int(input(f'Digite o no novo valor para INTELIGENCIA do jogador {jogadores[o][0]}: '))
    elif a == 8:
        jogadores[o][a] = int(input(f'Digite o no novo valor para OCULTO do jogador {jogadores[o][0]}: '))
    conteudo = []
    for j in jogadores:
        conteudo.append('*'*20)
        conteudo.append(f'\n{j}\n')
    arquivo = open('Jogador.txt','w')
    arquivo.writelines(conteudo)
    arquivo.close()
    print('atualização realizada com sucesso')