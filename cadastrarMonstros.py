arquivo = open('Monstros.txt','r')
conteudo = arquivo.readlines()
golpe = []
nome = input('Digite o nome do monstro: ')
nivel = int(input('digite o nivel do monstro: '))
forca = int(input('Digite a força do monstro: '))
agilidade = int(input('Digite a agilidade do monstro: '))
velocidade = int(input('Digite a velocidade do monstro: '))
defesa = int(input('Digite a defesa do monstro: '))
vida = int(input('Digite a vida do monstro: '))
poder = int(input('Digite o poder do monstro: '))
inteligencia = int(input('Digite a inteligencia do monstro: '))
oculto = int(input('Digite o poder de ocultação do monstro: '))
q = int(input('Digite a quantidade de golpes do monstro: '))
for i in range(q):
    a = input(f'entre com o nome do golpe {i} ')
    golpe.append(a)
conteudo.append('*'*20)
conteudo.append(f'\nNome: {nome}\nNível: {nivel}\nForça: {forca}\nAgilidade: {agilidade}\nVelocidade: {velocidade}\nDefesa: {defesa}\nVida: {vida}\nPoder: {poder}\nInteligencia: {inteligencia}\nOculto: {oculto}\nGolpes: {golpe}\n')
arquivo = open('Monstros.txt','w')
arquivo.writelines(conteudo)
arquivo.close()
print(f'{nome} Cadastrado com Sucesso')