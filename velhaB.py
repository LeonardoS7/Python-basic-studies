"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Leonardo de Oliveira Santos
  NUSP : 11276812   

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em
  http://wiki.python.org.br/QuickSort
"""
a,b,c,d,e,f,g,h,i = 0,0,0,0,0,0,0,0,0
a1,b1,c1,d1,e1,f1,g1,h1,i1 = '1','2','3','4','5','6','7','8','9'
jogador  = 1
jogo = 1
vez = 1
contador = 0
while jogo == 1:
    jogada = int (input('Jogada?'))
    if vez % 2 == 0:
        jogador = 2
        jogador1 = 'O'
    else:
        jogador = 1
        jogador1 = 'X'
    if jogada == 1:
        if a == 0:
            a = jogador
            a1 = jogador1
            vez += 1
            contador += 1
    if jogada == 2:
        if b == 0:
            b = jogador
            b1 = jogador1
            vez += 1
            contador += 1
    if jogada == 3:
        if c == 0:
            c = jogador
            c1 = jogador1
            vez += 1
            contador += 1
    if jogada == 4:
        if d == 0:
            d = jogador
            d1 = jogador1
            vez += 1
            contador += 1
    if jogada == 5:
        if e == 0:
            e = jogador 
            e1 = jogador1
            vez += 1
            contador += 1
    if jogada == 6:
        if f == 0:
            f = jogador 
            f1 = jogador1
            vez += 1
            contador += 1
    if jogada == 7:
        if g == 0:
            g = jogador
            g1 = jogador1
            vez += 1
            contador += 1
    if jogada == 8:
        if h == 0:
            h = jogador
            h1 = jogador1
            vez += 1
            contador += 1
    if jogada == 9:
        if i == 0:
            i = jogador 
            i1 = jogador1
            vez += 1      
            contador += 1
    config = (a * 3**0)+(b * 3**1)+(c * 3**2)+(d * 3**3)+(e * 3**4)+(f * 3**5)+(g * 3**6)+(h * 3**7)+(i * 3**8)
    print ('Tabuleiro:')
    print (a1+b1+c1)
    print (d1+e1+f1)
    print (g1+h1+i1)
    if (a == 1 and b == 1 and c == 1) or (d == 1 and e == 1 and f == 1) or (g == 1 and h == 1 and i == 1):
        jogo = 0
        print('VENCEU JX')
    if (a == 1 and e == 1 and i == 1) or (c == 1 and e == 1 and g == 1) :
        jogo = 0
        print('VENCEU JX')
    if (a == 1 and d == 1 and g == 1) or (b == 1 and e == 1 and h == 1) or (c == 1 and f == 1 and i == 1):
        jogo = 0
        print('VENCEU JX')  
    if (a == 2 and b == 2 and c == 2) or (d == 2 and e == 2 and f == 2) or (g == 2 and h == 2 and i ==2):
        jogo = 0
        print('VENCEU JO')
    if (a == 2 and e == 2 and i == 2) or (c == 2 and e == 2 and g == 2) :
        jogo = 0
        print('VENCEU JO')
    if (a == 2 and d == 2 and g == 2) or (b == 2 and e == 2 and h ==2) or (c == 2 and f == 2 and i == 2):
        jogo = 0
        print('VENCEU JO')  
    if contador == 9 and jogo == 1:
        print ('EMPATOU')
        jogo = 0