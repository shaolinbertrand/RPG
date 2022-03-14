from cadastrarJogador import cadastra_jogador
from cadastrarMonstros import cadastra_monstro
from atualizaJogador import atualiza
from combate import combate_iniciado
while True:
    print('Bem vindo ao RPG selecione a opção desenjada')
    print('[0] - Cadastrar Novo Jogador\n[1] - Atualizar Jogador\n[2] - Cadastrar Novo Monstro\n[3] Iniciar Combate\n[4]-Sair do sistema')
    o = int(input('Entre com o numero da opção desejada: '))
    if o == 0:
        cadastra_jogador()
    elif o == 1:
        cadastra_monstro()
    elif o == 2:
        atualiza()
    elif o == 3:
        combate_iniciado()
    elif o == 4:
        break
    else:
        print('Opção invalida')