'''
QUIZ - MONTE EVEREST
2025.07.02
Maísa G. Bom
'''
# OBJETIVO: Criar um QUIZZ sobre o MONTE EVEREST

# BIBLIOTECAS:
# Espaço reservado para a declaração das bibliotecas e funções
from random import randint 
from time import sleep
from modules import limpaTela, mostraLine, msgCenter, msgLeft, mostraCabecalho, mostraMenu, sortNum, validaValue, getValue, mostraDica, playAgain # Sub-rotina

# CONSTANTES 
TAM = int(50)   
MAR = int(2)    

# VARIÁVEIS (int)
key = 0         
resp = 0        
vidas = 0       
limite = 0      
tentativa = 0   
msg = ''        

# LISTAS
MSGS = []       
msgsCab = ['QUIZ - MONTE EVEREST',      
            'Desenvolvido por Maísa G. Bom']

# FUNÇAO PRINCIPAL DO JOGO
def playGame(): 
    global key, resp, vidas, limite, tentativa, MSGS # Variáveis global
    pontos = 0

    # CHAMADA DE SUB-ROTINAS:
    limpaTela()  # Sub-rotina             
    mostraCabecalho(msgsCab)    
    mostraCabecalho([f'A sua pontuação inicial é 0'])       

    # Primeira pergunta
    msg = ('A-> Onde está localizado o Monte Everest?' , '[1] Nepal' , '[2] Nepal e China' , '[3] China') 
    resp = getValue(msg)   # Entrada de dados
    opcoes = ['1', '2', '3']    
    while not validaValue(resp, opcoes): # estrutura de repetição (while)
        resp = getValue(msg) 

    # Verifica se a resposta está correta
    correta = '2'
    if resp == correta:  # Estrutura de decisão
        mostraCabecalho(['Parabéns! Você acertou a primeira questão!']) # Saída de dados
        pontos += 1
    else:                # estrutura de decisão
        mostraCabecalho(['Já começa assim? Resposta errada!', 'A resposta correta é Nepal e China.']) # Saída de dados
    
    # Segunda pergunta
    msg2 = ('B-> Qual é a altitude aproximada do Monte Everest?' , '[1]  7.848 metros' , '[2] 8.848 metros' , '[3] 8.849 metros')
    resp2 = getValue(msg2)
    while not validaValue(resp2, ['1', '2', '3']):
        resp2 = getValue(msg2)
    if resp2 == '3':
        mostraCabecalho(['Olha só! Você manda bem!'])
        pontos += 1
    else:
        mostraCabecalho(['Pare de ser besta! Resposta errada!', 'A resposta correta é 8.849 metros.'])

    # Terceira pergunta
    msg3 = ('C-> Qual o nome da cadeia de montanhas onde está o Everest?' , '[1] Himalaia' , '[2] Alpes' , '[3] Andes')
    resp3 = getValue(msg3)
    while not validaValue(resp3, ['1', '2', '3']):
        resp3 = getValue(msg3)
    if resp3 == '1':
        mostraCabecalho(['Parabéns! Você é feraaa!'])
        pontos += 1 
    else:
        mostraCabecalho(['Trate de estudar mais! Resposta errada!', 'A resposta correta é Himalaia.'])

    # Quarta pergunta
    msg4 = ('D-> Qual foi o primeiro homem a alcançar o topo do Everest, junto com Tenzing Norgay?' , '[1] Edmund Hillary' , '[2] Waldemar Niclevicz' , '[3] Junko Tabei')
    resp4 = getValue(msg4)
    while not validaValue(resp4, ['1', '2', '3']):
        resp4 = getValue(msg4)
    if resp4 == '1': 
        mostraCabecalho(['Você é um poço de conhecimento! Você acertou!'])
        pontos += 1
    else:
        mostraCabecalho(['Você e um inútil! Resposta errada!', 'A resposta correta é Edmund Hillary.']) 

    # Quinta Pergunta
    msg5 = ('E-> Qual o principal risco enfrentado pelos alpinistas no "Death Zone" (Zona da Morte) do Everest?' , '[1] Fome, frio e falta de água', '[2] Ataque de animais selvagens', '[3] Pouco oxigênio')
    resp5 = getValue(msg5)
    while not validaValue(resp5, ['1', '2', '3']):
        resp5 = getValue(msg5)
    if resp5 == '3':
        mostraCabecalho(['Você é bom nisso! Você acertou!']) 
        pontos += 1 
    else:
        mostraCabecalho(['Ahhh! Você errou! Resposta errada.', 'A resposta correta é Pouco oxigênio.'])

    # Mostra a pontuação final
    mostraCabecalho([f'Sua pontuação final foi: {pontos} de 5'])

    # Pergunta se o jogador deseja jogar novamente
    if playAgain(): # Entrada de dados
        playGame()
    else:
        mostraCabecalho(['Obrigado por jogar!', 'Até a próxima!'])
# Fim de jogo

# Início do jogo
playGame()