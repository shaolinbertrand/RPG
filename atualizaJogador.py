arquivo = open('Jogador.txt','r')
conteudo = arquivo.readlines()
q=j=0
jogador = [[],[]]
nomes = []
for i in conteudo:
    if '*' not in i:
        if 'Nome' in i:
            a = i.replace('Nome: ','')
            a = a.replace('\n','')
            nomes.append(a)
        jogador[j].append(i)
    else:
        q += 1
        if q == 2:
            j+=1
            q = 1
print('Qual jogador você deseja atualizar? ')
print(nomes)
o = int(input('opção: '))
print(f'Você selecionou o {jogador[o]}')