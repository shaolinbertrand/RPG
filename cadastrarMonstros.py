def cadastra_monstro():
    arquivo = open('Monstros.txt','r')
    conteudo = arquivo.readlines()
    #monsto = [nome,nivel,força,agilidade,velocidade,defesa,vida,poder,inteligencia,oculto,[golpes]]
    golpe = []
    monstro = ['',0,0,0,0,0,0,0,0,0,golpe]
    monstro[0] = input('Digite o nome do monstro: ')
    monstro[1] = int(input('digite o nivel do monstro: '))
    monstro[2] = int(input('Digite a força do monstro: '))
    monstro[3] = int(input('Digite a agilidade do monstro: '))
    monstro[4] = int(input('Digite a velocidade do monstro: '))
    monstro[5] = int(input('Digite a defesa do monstro: '))
    monstro[6] = int(input('Digite a vida do monstro: '))
    monstro[7] = int(input('Digite o poder do monstro: '))
    monstro[8] = int(input('Digite a inteligencia do monstro: '))
    monstro[9] = int(input('Digite o poder de ocultação do monstro: '))
    q = int(input('Digite a quantidade de golpes do monstro: '))
    for i in range(q):
        a = input(f'entre com o nome do golpe {i}: ')
        golpe.append(a)
    conteudo.append('*'*20)
    conteudo.append(f'\n{monstro}\n')
    arquivo = open('Monstros.txt','w')
    arquivo.writelines(conteudo)
    arquivo.close()
    print(f'{monstro[0]} Cadastrado com Sucesso')