def cadastra_jogador():
    arquivo = open('Jogador.txt','r')
    conteudo = arquivo.readlines()
    # jogador = [nome,força,agilidade,velocidade,defesa,vida,poder,inteligencia,oculto]
    jogador = ['',0,0,0,0,0,0,0,0]
    jogador[0]= str(input('Digite o nome do Jogador: '))
    jogador[1] = int(input('Digite a força do Jogador: '))
    jogador[2] = int(input('Digite a agilidade do Jogador: '))
    jogador[3] = int(input('Digite a velocidade do Jogador: '))
    jogador[4] = int(input('Digite a defesa do Jogador: '))
    jogador[5]= int(input('Digite a vida do Jogador: '))
    jogador[6] = int(input('Digite o poder do Jogador: '))
    jogador[7]= int(input('Digite a inteligencia do Jogador: '))
    oculto = input('Digite o nome do atributo especifico do jogador: ')
    jogador[8] = int(input(f'Digite o valor de {oculto}: '))
    conteudo.append('*'*20)
    conteudo.append(f'\n{jogador}\n')
    arquivo = open('Jogador.txt','w')
    arquivo.writelines(conteudo)
    arquivo.close()
    print(f'{jogador[0]} Cadastrado com Sucesso')