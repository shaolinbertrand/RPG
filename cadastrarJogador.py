arquivo = open('Jogador.txt','r')
conteudo = arquivo.readlines()
golpe = []
nome = input('Digite o nome do Jogador: ')
forca = int(input('Digite a força do Jogador: '))
agilidade = int(input('Digite a agilidade do Jogador: '))
velocidade = int(input('Digite a velocidade do Jogador: '))
defesa = int(input('Digite a defesa do Jogador: '))
vida = int(input('Digite a vida do Jogador: '))
poder = int(input('Digite o poder do Jogador: '))
inteligencia = int(input('Digite a inteligencia do Jogador: '))
oculto = input('Digite o nome do atributo especifico do jogador: ')
ov = int(input(f'Digite o valor de {oculto}: '))
conteudo.append('*'*20)
conteudo.append(f'\nNome: {nome}\nForça: {forca}\nAgilidade: {agilidade}\nVelocidade: {velocidade}\nDefesa: {defesa}\nVida: {vida}\nPoder: {poder}\nInteligencia: {inteligencia}\n{oculto}: {ov}\n')
arquivo = open('Jogador.txt','w')
arquivo.writelines(conteudo)
arquivo.close()
print(f'{nome} Cadastrado com Sucesso')