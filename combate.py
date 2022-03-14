def combate_iniciado():
    arquivo = open('Jogador.txt','r')
    conteudo = arquivo.readlines()
    q=j=0
    jogadores =[]
    jogador = []
    for i in conteudo:
        if '*' not in i:
            jogador = i.replace('[','')
            jogador = jogador.replace(']','')
            jogador = jogador.replace('\n','')
            jogador = jogador.split(',')
            print(jogador)
        for j in range(8):
                if j != 0:
                    print(j)
                    jogador[j] = int(jogador[j])
                else:
                    print(jogador)
                    print(j)
                    jogador[j] = jogador[j].replace('"','').replace("'\'",'').replace("'",'')
        jogadores.append(jogador)
    arquivo.close()

    arquivo = open('Monstros.txt','r')
    conteudo = arquivo.readlines()
    q=j=0
    monstros =[]
    for i in conteudo:
        if '*' not in i:
            monstro = i.replace('[','')
            monstro = monstro.replace(']','')
            monstro = monstro.replace('\n','')
            monstro = monstro.split(',')
        for j in range(9):
                if j != 0:
                    monstro[j] = int(monstro[j])
                else:
                    monstro[j] = monstro[j].replace('"','').replace("'\'",'').replace("'",'')
        monstros.append(monstro)
    arquivo.close()
    while True:
        print('Os Jogadores disponiveis são:')
        j = 0
        for i in jogadores:
            print(f'{[j]}-{i[0]}')
            j += 1
        jog = int(input('Entre com o numero: '))
        jogador = jogadores[jog]
        print(f'O jogador {jogador[0]} foi selecionado')
        print('Os monstros disponiveis são: ')
        j = 0
        for i in monstros:
            print(f'{[j]}-{i[0]}')
            j += 1
        m = int(input('entre com o numero: '))
        monstro = monstros[m]
        print(f'O monstro {monstro[0]} Selecionado')
        a = int(input('Selecione ação deseja realizar \n[0]-Atacar\n[1]-Aproximar ou Afastar\n[2]-Dialogar\nOpção: '))
        if a == 0:
            x = jogador[2]
            y = monstro[3]
        elif a == 1:
            x = jogador[3]
            y = monstro[4]
        elif a == 2:
            x = jogador[7]
            y = monstro[8]
        print(f'Você precisar tirar {15-x+y} no d20')
        c = input('Deseja continuar o combate [s/n]:').upper()
        if c == 'N':
            break
    print('Foi um belo combate, descanse guerreiro')