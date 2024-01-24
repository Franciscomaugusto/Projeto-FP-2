#Francisco Augusto 99218
#Tipo abstrato de dados - posicao
#Construtores
def cria_posicao(col, lin):
    '''cria_posicao : str x str -> posicao
    Recebe duas strings como argumentos e devolve a posicao correspondente'''
    if col in ['a', 'b', 'c'] and lin in ['1', '2', '3']:
        pos = (col, lin)
        return pos
    raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(p):
    '''cria__copia_posicao : posicao -> posicao
    Recebe uma posicao como argumento e devolve uma copia dessa posicao'''
    nov_pos = (p[0], p[1])
    return nov_pos


#Seletores
def obter_pos_c(p):
    '''obter_pos_c : posicao -> str
    Recebe uma posicao como argumento e devolve uma string correspondente a coluna dessa posicao'''
    return p[0]


def obter_pos_l(p):
    '''obter_pos_l : posicao -> str
    Recebe uma posicao como argumento e devolve uma string correspondente a linha dessa posicao'''
    return p[1]


#Reconhecedor
def eh_posicao(p):
    '''eh_posicao : universal -> bool
    Devolve True se o seu argumento for um TAD posicao e False caso contrario'''
    if len(p) == 2 and type(p) == tuple and p[0] in ['a', 'b', 'c']\
     and p[1] in ['1', '2', '3']:
        return True
    return False


#Teste
def posicoes_iguais(p1, p2):
    '''cria_posicao : posicao x posicao -> str
    Recebe uma posicao como argumento e devolve uma string correspondente a coluna dessa posicao'''    
    if p1[0] == p2[0] and p1[1] == p2[1]:
        return True
    return False


#Transformador
def posicao_para_str(p):
    '''posicao_para_str : posicao -> str
    Recebe uma posicao como argumento e devolve a string que representa essa posicao'''
    return p[0]+p[1]


#Funcao de alto nivel associada a este Tipo de dados
def obter_posicoes_adjacentes(p):
    '''obter_posicoes_adjacentes : posicao -> tuplo de posicoes
    Recebe uma posicao como argumento e devolve um tuplo que contem todas as suas posicoes adjacentes, por ordem de leitura do tabuleiro'''    
    adjacentes = {cria_posicao('a', '1'): (cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('b', '2')),
                  cria_posicao('a', '2'): (cria_posicao('a', '1'), cria_posicao('b', '2'), cria_posicao('a', '3')),
                  cria_posicao('a', '3'): (cria_posicao('a', '2'), cria_posicao('b', '2'), cria_posicao('b', '3')),
                  cria_posicao('b', '1'): (cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('b', '2')),
                  cria_posicao('b', '2'): (cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'),
                  cria_posicao('a', '2'), cria_posicao('c', '2'), cria_posicao('a', '3'), cria_posicao('b', '3'),
                  cria_posicao('c', '3')), cria_posicao('b', '3'): (cria_posicao('b', '2'), cria_posicao('a', '3'),
                  cria_posicao('c', '3')), cria_posicao('c', '1'): (cria_posicao('b', '1'), cria_posicao('b', '2'),
                  cria_posicao('c', '2')), cria_posicao('c', '2'): (cria_posicao('c', '1'), cria_posicao('b', '2'),
                  cria_posicao('c', '3')), cria_posicao('c', '3'): (cria_posicao('b', '2'), cria_posicao('c', '2'),
                  cria_posicao('b', '3'))}
    return adjacentes[p]


#Tipo abstrato de dados - peca
#Construtores
def cria_peca(s):
    '''cria_peca : str -> peca
    Recebe uma string como argumento ('X', 'O', ou ' ') e devolve a peca correspondente'''    
    dic = {'X': 1, 'O': -1, ' ': 0}
    if s in dic:
        return dic[s]
    raise ValueError('cria_peca: argumento invalido')


def cria_copia_peca(s):
    '''cria_copia_peca : peca -> peca
    Recebe uma peca como argumento e devolve uma copia dessa peca'''    
    nov = s
    return nov


#Reconhecedor
def eh_peca(s):
    '''eh_peca : universal -> bool
    Recebe uma peca como argumento e devolve True caso o argumento seja um TAD peca'''    
    if s in [-1, 1, 0] and type(s) == int:
        return True
    return False


#Teste
def pecas_iguais(s1, s2):
    '''pecas_iguais : peca x peca -> bool
    Recebe duas peca como argumentos e devolve True caso as pecas sejam iguais'''    
    if s1 == s2 and eh_peca(s1) and eh_peca(s2):
        return True
    return False


#Transformador
def peca_para_str(s):
    '''cria_copia_peca : peca -> peca
    Recebe uma peca como argumento e devolve uma copia dessa peca'''    
    dic = {1: '[X]', -1: '[O]', 0: '[ ]'}
    if eh_peca(s):
        return dic[s]


#Funcao de alto nivel associada a este Tipo de dados
def peca_para_inteiro(s):
    '''peca_para_inteiro : peca -> N
    Recebe uma peca como argumento o valor o inteiro correspondente a essa peca (-1, 1, 0)'''    
    if eh_peca(s):
        if peca_para_str(s) == '[X]':
            return 1
        if peca_para_str(s) == '[O]':
            return -1
        if peca_para_str(s) == '[ ]':
            return 0


#Tipo abstrato de dados - tabuleiro
#Construtores
def cria_tabuleiro():
    '''cria_tabuleiro :  -> tabuleiro
    Devolve um tabuleiro do moinho, 3x3 totalmente vazio'''    
    return [cria_peca(' '), cria_peca(' '), cria_peca(' '), cria_peca(' '), cria_peca(' '), cria_peca(' '),
            cria_peca(' '), cria_peca(' '), cria_peca(' ')]


def cria_copia_tabuleiro(t):
    '''cria_copia_tabuleiro :  tabuleiro-> tabuleiro
    Recebe um tabuleiro como argumento e devolve uma copia desse tabuleiro'''
    nov_t = []
    for ind in range(0,9):
        nov_t = nov_t + [t[ind]]
    return nov_t


#Seletores
#Seletores - Funcao auxiliar
def pos_para_indice(pos):
    '''pos_para_indice :  pos -> N
    Recebe uma posicao como argumento e devolve o calor em inteiro (0-8) do indice dessa posicao'''    
    dic = {cria_posicao('a', '1'): 0, cria_posicao('b', '1'): 1, cria_posicao('c', '1'): 2, cria_posicao('a', '2'): 3,
           cria_posicao('b', '2'): 4, cria_posicao('c', '2'): 5, cria_posicao('a', '3'): 6, cria_posicao('b', '3'): 7,
           cria_posicao('c', '3'): 8}
    return dic[pos]


def obter_peca(tab, pos):
    '''obter_peca :  tabuleiro x posicao-> peca
    Recebe um tabuleiro e uma posicao como argumentos e retorna a peca que se encontra nessa posicao do tabuleiro'''    
    return tab[pos_para_indice(pos)]


def obter_vetor(tab, vet):
    '''obter_vetor :  tabuleiro x str-> tuplo de pecas
    Recebe um tabuleiro e uma string como argumento e devolve um tuplo com todas as pecas dessa linha ou coluna'''    
    if vet == 'a':
        return (tab[0], tab[3], tab[6])
    if vet == 'b':
        return (tab[1], tab[4], tab[7])
    if vet == 'c':
        return (tab[2], tab[5], tab[8])
    if vet == '1':
        return (tab[0], tab[1], tab[2])
    if vet == '2':
        return (tab[3], tab[4], tab[5])
    if vet == '3':
        return (tab[6], tab[7], tab[8])


#Modificadores
def coloca_peca(tab, pec, pos):
    '''coloca_peca :  tabuleiro x peca x posicao-> tabuleiro
    Recebe uma peca, uma posicao e um tabuleiro e devolve o tabuleiro apos se colocar a peca indicada na posicao do tabuleiro indicada'''    
    tab[pos_para_indice(pos)] = pec
    return tab


def remove_peca(tab, pos):
    '''remove_peca :  tabuleiro x posicao-> tabuleiro
    Recebe um tabuleiro e um posicao como argumentos e devolve o tabuleiro apos se remover a peca da posicao indicada'''    
    tab[pos_para_indice(pos)] = cria_peca(' ')
    return tab


def move_peca(tab, p1, p2):
    '''move_peca :  tabuleiro x posicao x posicao-> tabuleiro
    Recebe um tabuleiro e duas posicoes e devolve o tabuleiro apos se mover a peca da posicao p1 para a posicao p2 '''    
    pec = tab[pos_para_indice(p1)]
    tab[pos_para_indice(p1)] = cria_peca(' ')
    tab[pos_para_indice(p2)] = pec
    return tab


#Reconhecedores
def eh_tabuleiro(arg):
    '''eh_tabuleiro :  universal-> bool
    Recebe um argumento universal e devolve True se o argumento corresponder a um TAD tabuleiro'''    
    if type(arg) == list and len(arg) == 9:
        x = 0
        o = 0
        for index in range(0, 9):
            if not arg[index] in [-1, 1, 0]:
                return False
            if arg[index] == 1:
                x = x +1
            if arg[index] == -1:
                o = o +1
        if o >= x +2:
            return False
        if x >= o +2:
            return False     
        return True
    return False


def eh_posicao_livre(tab, pos):
    '''eh_posicao_livre :  tabuleiro x posicao-> bool 
    Recebe um tabuleiro e uma posicao como argumento e devolve True caso essa posicao desse tabuleiro se encontre livre'''    
    if tab[pos_para_indice(pos)] == cria_peca(' '):
        return True
    return False


#Teste
def tabuleiros_iguais(tab1, tab2):
    '''tabuleiros_iguais :  tabuleiro x tabuleiro-> bool
    Recebe dois tabuleiros como argumento e devolve True caso sejam iguais'''    
    if eh_tabuleiro(tab1) and eh_tabuleiro(tab2) and tab1 == tab2:
        return True
    return False


#Transformadores
def tabuleiro_para_str(tab):
    '''tabuleiro_para_str :  tabuleiro-> str
    Recebe um tabuleiro como argumento e devolve uma string que representa esse tabuleiro'''    
    stab = []
    for pec in range(0, len(tab)):
        stab = stab + [peca_para_str(tab[pec])]
    return '   a' + '   b' + '   c' + '\n' + '1 ' + stab[0] + '-' + stab[1] + '-'\
           + stab[2] + '\n' + '   | ' + '\\ ' + '|' + ' / ' + '|' + '\n' + '2 ' +\
           stab[3] + '-' + stab[4] + '-' + stab[5] + '\n' + '   | ' + '/ ' + '|' \
           + ' \\ ' + '|' + '\n' + '3 ' + stab[6] + '-' + stab[7] + '-' + stab[8]


def tuplo_para_tabuleiro(t):
    '''tuplo_para_tabuleiro :  tuplo-> tabuleiro
    Recebe um tuplo como argumento e devolve o tabuleiro que e representado por esse tuplo'''    
    return [t[0][0], t[0][1], t[0][2], t[1][0], t[1][1], t[1][2], t[2][0], t[2][1], t[2][2]]


#Funcoes de alto nivel associada a este Tipo de dados
def obter_ganhador(tab):
    '''obter_ganhador :  tabuleiro-> peca
    Recebe um tabuleiro como argumento e devolve a peca que representa o jogador vencedor devolvendo a peca vazia caso nao ha vencedor'''    
    for x in ['X', 'O']:
        pec = cria_peca(x)
        for lin in ['1', '2', '3']:
            if obter_peca(tab, cria_posicao('a', lin)) == obter_peca(tab, cria_posicao('b', lin)) == \
                    obter_peca(tab, cria_posicao('c', lin)) == pec:
                return pec
        for col in ['a', 'b', 'c']:
            if obter_peca(tab, cria_posicao(col, '1')) == obter_peca(tab, cria_posicao(col, '2')) == \
                    obter_peca(tab, cria_posicao(col, '3')) == pec:
                return pec
    return cria_peca(' ')


def obter_posicoes_livres(tab):
    '''obter_posicoes_livre :  tabuleiro-> tuplo de posicoes
    Recebe um tabuleiro como argumento e devolve um tuplo que contem todas as posicoes livres'''    
    return obter_posicoes_jogador(tab, cria_peca(' '))


def obter_posicoes_jogador(tab, pec):
    '''obter_posicoes_jogador :  tabuleiro x peca-> tuplo de posicoes
    Recebe um tabuleiro e uma peca como argumento e devolve um tuplo que contem todas as posicoes ocupadas pela peca'''    
    res = ()
    for lin in ['1', '2', '3']:
        for col in ['a', 'b', 'c']:
            if obter_peca(tab, cria_posicao(col, lin)) == pec:
                res = res + (cria_posicao(col, lin),)
    return res


#Funcoes adicionais
def obter_movimento_auto(tab, pec, strin):
    '''obter_movimento_auto :  tabuleiro x peca x string-> tuplo de posicoes
    Recebe uma tabuleiro uma peca e uma string e devolve um tuplo de posicoes que indicam qual a melhor jogada
    de colocacao/movimentacao para a peca no tabuleiro segundo o criterio indicado pela string'''    
    if len(obter_posicoes_livres(tab)) > 3:
        return posicao_colocacao(tab, pec)
    return auto(tab, pec, strin)    


def obter_movimento_manual(tab, pec):
    '''obter_movimento_manual :  tabuleiro x peca-> tuplo de posicoes
    Recebe um tabuleiro e uma peca como argumento e devolve o tuplo de posicoes da jogada indicada, manualmente, pelo jogador'''    
    col = ['a', 'b', 'c']
    lin = ['1', '2', '3']
    if len(obter_posicoes_livres(tab)) > 3:
        s = input('Turno do jogador. Escolha uma posicao: ')
        if len(s) == 2 and s[0] in col and s[1] in lin:
            if eh_posicao_livre(tab, cria_posicao(s[0], s[1])):
                return (cria_posicao(s[0], s[1]), )
        raise ValueError('obter_movimento_manual: escolha invalida')
    if len(obter_posicoes_livres(tab)) == 3:
        s = input('Turno do jogador. Escolha um movimento: ')
        if len(s) == 4 and s[0] in col and s[1] in lin and s[2] in col and s[3] in lin:
            if obter_peca(tab, cria_posicao(s[0], s[1])) == pec and eh_posicao_livre(tab, cria_posicao(s[2], s[3])):
                return (cria_posicao(s[0], s[1]), cria_posicao(s[2], s[3]))
            if cria_posicao(s[2],s[3]) == cria_posicao(s[0], s[1]):
                return (cria_posicao(s[0], s[1]), cria_posicao(s[0], s[1]))
        raise ValueError('obter_movimento_manual: escolha invalida')
    
    
#Funcoes auxiliares - obter_movimento_auto
def posicao_colocacao(tab, pec):
    '''posicao_colocacao :  tabuleiro x peca -> posicao
    Recebe um tabuleiro e uma peca como arguemento e indicada qual a melhor posicao para colocar a peca'''    
    dic = {cria_peca('X'): cria_peca('O'), cria_peca('O'): cria_peca('X')}
    adv = dic[pec]
    dic2 = {0: 'a', 1: 'b', 2: 'c'}
    for vet in ['a', 'b', 'c']:
        if type(verifica_vitoria(tab, pec, vet)) != bool:
            lin = verifica_vitoria(tab, pec, vet) + 1
            return (cria_posicao(vet, str(lin)),)
        if type(verifica_vitoria(tab, adv, vet)) != bool:
            lin = verifica_vitoria(tab, adv, vet) + 1
            return (cria_posicao(vet, str(lin)),)
    for vet in ['1', '2', '3']:
        if type(verifica_vitoria(tab, pec, vet)) != bool:
            col = dic2[verifica_vitoria(tab, pec, vet)]
            return (cria_posicao(col, vet),)
        if type(verifica_vitoria(tab, adv, vet)) != bool:
            col = dic2[verifica_vitoria(tab, adv, vet)]
            return (cria_posicao(col, vet),)
    if obter_peca(tab, cria_posicao('b', '2')) == cria_peca(' '):
        return(cria_posicao('b', '2'),)
    if type(verifica_cantos(tab)) != bool:
        return (verifica_cantos(tab),)
    return (verifica_laterais(tab),)


def auto(tab, pec, strin):
    '''auto :  tabuleiro x peca x string-> tuplo de posicoes
    Recebe um tabuleiro uma peca e uma string como argumento e devolve um tuplo de posicoes para a
    melhor movimentacao a fazer para a peca no tabuleiro segundo o criterio string'''    
    if strin == 'facil':
        return facil(tab, pec)
    if strin == 'normal':
        valor, seq_mov = minimax(tab, pec, 2, ())
        if valor != 0:
            return seq_mov
        return facil(tab, pec)
    if strin == 'dificil':
        valor, seq_mov = minimax(tab, pec, 6, ())
        if valor != 0:
            return seq_mov
        return facil(tab, pec)
    
    
#Posicao_colocacao - funcoes auxiliares
def verifica_cantos(tab):
    '''verifica_cantos :  tabuleiro-> posicao/bool
    Recebe um tabuleiro como argumento e devolve um canto, caso este se encontre livre,caso contrario retorna False'''    
    for pos in [cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('a', '3'), cria_posicao('c', '3')]:
        if obter_peca(tab, pos) == cria_peca(' '):
            return pos
    return False


def verifica_laterais(tab):
    '''verifica_laterais :  tabuleiro-> posicao
    Recebe um tabuleiro como argumento e devolve uma lateral livre'''    
    for pos in [cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('c', '2'), cria_posicao('b', '3')]:
        if obter_peca(tab, pos) == cria_peca(' '):
            return pos


def verifica_vitoria(tab, pec, vetor):
    '''verifica_vitoria :  tabuleiro x peca x vetor-> posicao/bool
    Recebe um tabuleiro uma peca e um tuplo como argumento e devolve a posicao livre, caso o
    vetor tenha duas posicoes ocupadas pela peca, caso contrario, retorna False'''    
    num_pec = 0
    num_adv = 0
    dic = {cria_peca('X'): cria_peca('O'), cria_peca('O'): cria_peca('X')}
    adv = dic[pec]    
    for ind in range(0, 3):
        if obter_vetor(tab, vetor)[ind] == pec:
            num_pec = num_pec + 1
        if obter_vetor(tab, vetor)[ind] == adv:
            num_adv = num_adv + 1
    if num_pec == 2 and num_adv == 0:
        return obter_vazio(obter_vetor(tab, vetor))
    return False


#verifica_vitoria - funcao auxiliar
def obter_vazio(vetor):
    '''obter_vazio:  tuplo-> posicao
    Recebe um tuplo como argumento e devolve o indice da posicao vazia, caso a tenha'''    
    for ind in range(0, 3):
        if vetor[ind] == cria_peca(' '):
            return ind


#auto - funcoes auxiliares
def facil(tab, pec):
    '''verifica_cantos :  tabuleiro x pec->tuplo de posicoes
    Recebe um tabuleiro e uma peca como argumento e devolve um tuplo de posicoes '''    
    for lin in ['1', '2', '3']:
        for col in ['a', 'b', 'c']:
            if obter_peca(tab, cria_posicao(col, lin)) == pec:
                conjunto = obter_posicoes_adjacentes(cria_posicao(col, lin))
                for adj in conjunto:
                    if eh_posicao_livre(tab, adj):
                        return (cria_posicao(col, lin), adj)


#Funcao Minimax
def minimax(tab, jogador, prof, seq_mov):
    '''minimax :  tabuleiro x peca x inteiro x tuplo -> inteiro x tuplo
    Recebe um tabuleiro, uma peca, um inteiro e um tuplo como argumentos e devolve um inteiro e 
    um tuplo que indicam o valor do tabuleiro e a melhor sequencia de jogadas'''    
    dic = {cria_peca('X'): cria_peca('O'), cria_peca('O'): cria_peca('X')}
    dic2 = {cria_peca('X'): 1, cria_peca('O'): -1}
    if valor_tabuleiro(tab) != 0 or prof == 0:
        return valor_tabuleiro(tab), seq_mov
    else:
        melhor_resultado = dic2[dic[jogador]]
        joga = obter_posicoes_jogador(tab, jogador)
        melhor_seq_mov = seq_mov
        for pec in joga:
            for pec_adj in obter_posicoes_adjacentes(pec):
                if eh_posicao_livre(tab, pec_adj):
                    tab2 = cria_copia_tabuleiro(tab)
                    move_peca(tab2, pec, pec_adj)
                    novo_resultado, nova_seq_movs = minimax(tab2, dic[jogador], prof-1, seq_mov + (pec, pec_adj))
                    if melhor_seq_mov == seq_mov or (jogador == cria_peca('X') and novo_resultado > melhor_resultado) or\
                            (jogador == cria_peca('O') and novo_resultado < melhor_resultado):
                        melhor_resultado = novo_resultado
                        melhor_seq_mov = nova_seq_movs
        return melhor_resultado, melhor_seq_mov
    

#Minimax - funcoes auxiliares
def valor_tabuleiro(tab):
    '''valor_tabuleiro :  tabuleiro-> inteiro
    Recebe um tabuleiro como argumento e devolve o valor do tabuleiro
    (1 caso 'X' ganhe, -1 'O' ganhe e 0 caso nao haja vencedor)'''    
    if obter_ganhador(tab) == cria_peca(' '):
        return 0
    if obter_ganhador(tab) == cria_peca('X'):
        return 1
    if obter_ganhador(tab) == cria_peca('O'):
        return -1
    

#Funcao principal
def moinho(jogador, dificuldade):
    '''moinho :  str x str-> str
    Recebe duas strings como argumento e executa um jogo do moinho segundo as condicoes indicadas, devolvem uma string que indica o jogador vencedor'''    
    dic = {cria_peca('X'): cria_peca('O') , cria_peca('O'): cria_peca('X')}
    if jogador in ['[X]', '[O]'] and dificuldade in ['facil', 'normal', 'dificil']:
        tab = cria_tabuleiro()
        if jogador == '[X]':
            print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + dificuldade)
            print(tabuleiro_para_str(tab))
            while obter_ganhador(tab) == cria_peca(' '):
                tab = player(tab, jogador)
                if obter_ganhador(tab) == cria_peca(' '):
                    tab = computador(tab, jogador, dificuldade)
        if jogador == '[O]':
            print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + dificuldade)
            print(tabuleiro_para_str(tab))
            while obter_ganhador(tab) == cria_peca(' '):
                tab = comoutador(tab, jogador, dificuldade)
                if obter_ganhador(tab) == cria_peca(' '):
                    tab = player(tab, jogador)
        vencedor = obter_ganhador(tab)
        print(peca_para_str(vencedor))
    else:
        raise ValueError('moinho: argumentos invalidos')
    
#Moinho - funcoes auxiliares
def player(tab, jogador):
    '''player :  tabuleiro x peca -> tabuleiro
    Recebe um tabuleiro e uma peca como argumento e devolve o tabuleiro apos ter sido executada
    a jogada do jogador e imprimido o tabuleiro no ecra'''    
    dic = {'[X]': 'X', '[O]': 'O'}
    mov = obter_movimento_manual(tab, cria_peca(jogador))
    if len(mov) == 1:
        coloca_peca(tab, cria_peca(dic[jogador]), mov[0])
    if len(mov) == 2:
        move_peca(tab, mov[0], mov[1])
    print(tabuleiro_para_str(tab))
    return tab


def computador(tab, jogador, dificuldade):
    '''computador :  tabuleiro x peca x string -> tabuleiro
    Recebe um tabuleiro e uma peca e uma string como argumento e devolve o tabuleiro apos ter sido executada
    a jogada da peca segundo o criterio indicado pela string e imprimido o tabuleiro no ecra'''    
    dic = {cria_peca('X'): cria_peca('O') , cria_peca('O'): cria_peca('X')}
    dic2 = {'[X]': 'X', '[O]': 'O'}
    print('Turno do computador (' + dificuldade + '):')
    mov = obter_movimento_auto(tab, dic[cria_peca(dic2[jogador])], dificuldade)
    if len(mov) == 1:
        coloca_peca(tab, dic[cria_peca(dic2[jogador])], mov[0])
    if len(mov) == 2:
        move_peca(tab, mov[0], mov[1])
    print(tabuleiro_para_str(tab))
    return tab