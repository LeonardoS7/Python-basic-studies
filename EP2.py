# -*- coding: utf-8 -*-
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
from math import sqrt
G = 8.65*10**-13


        


def distancia (P1, P2):
    aux = (P2[0] - P1[0])**2 + (P2[1] - P1[1])**2
    distancia = sqrt(aux)
    return distancia   
def coss (a, b):
    x = (b[0]-a[0]) / distancia(a,b)
    return x
def sinn (a, b):
    x = (b[1]-a[1]) / distancia(a,b)
    return x
# astros definidos ([posx,posy],massa,raio)
def aceleracaoGravitacional(astro, P):
    pastro = astro[0]
    ac = (G * (astro[1]))/ (distancia(pastro, P)**2)
    acx = ac * coss(pastro,P) * -1
    acy = ac * sinn(pastro,P) * -1
    x = [acx,acy]
    return x
def aceleracaoResultante(astros, P):
    acrx = 0
    acry = 0
    for x in astros:
        ac = aceleracaoGravitacional(x,P)
        ax = float(ac[0])
        ay = float(ac[1])
        acrx += ax
        acry += ay
    x = [acrx, acry]
    return x
def deteccaoColisao(Nave, Astros):
    x = distanciaAstroMaisProximo(Nave, Astros)
    if x <= Nave[2]:
        return True
    else:
        return False
def atualizaNave(Nave, Astros, delta_t):
# naves definidas ([posx, posy], [vx, vy], raio)
        pNave = Nave[0]
        vNave = Nave[1]
        ar = aceleracaoResultante(Astros,pNave)
      #  x[0][0] = x[0][0] +  x[1][0]*delta_t + (ar[0]*delta_t**2/2)
      #  x[0][1] = x[0][1] +  x[1][1]*delta_t + (ar[1]*delta_t**2/2)
      #  x[1][0] = x[1][0] + (ar[0]*delta_t)
      #  x[1][1] = x[1][1] + (ar[1]*delta_t)
        posx = pNave[0] +  vNave[0]*delta_t + (ar[0]*delta_t**2/2)
        posy = pNave[1] +  vNave[1]*delta_t + (ar[1]*delta_t**2/2)
        vx = vNave[0] + (ar[0]*delta_t)
        vy = vNave[1] + (ar[1]*delta_t)
        patual = [posx,posy]
        vatual = [vx,vy]
        Nave[0] = patual
        Nave[1] = vatual
      

def distanciaAstroMaisProximo(Nave, Astros):
    a = []
    pNave = Nave[0]
    for x in Astros:
        r = distancia(pNave,x[0]) - (Nave[2]+x[2])
        a.append(r)
    b = min(a)
    if b > 0:
        return b
    else:
        return 0
        
def simulacao (Naves, Astros, niter, delta_t):   
    D = []
    T = []
    for j in range (0,niter):
        for k in Naves:
            atualizaNave(k,Astros,delta_t)
            pos = k[0]
            dp = distanciaAstroMaisProximo(k,Astros)
            T.append([pos])
            D.append([dp])
    return T,D
             
def main():
    niter = int(input("Número máximo de iterações: "))    
    delta_t = float(input("Delta t: "))
    nnaves = int(input("Número de naves: "))
    Naves = []
    for i in range(nnaves):
        print("*** Nave %d ***"%(i+1))
        x,y = input("Digite a posição (x,y): ").split()
        x,y = float(x),float(y)
        vx,vy = input("Digite a velocidade inicial (vx,vy): ").split()
        vx,vy = float(vx),float(vy)
        r = float(input("Digite o raio: "))
        Naves.append([[x,y], [vx,vy], r])

    nastros = int(input("Número de astros: "))
    Astros = []
    for i in range(nastros):
        print("*** Astro %d ***"%(i+1))
        x,y = input("Digite a posição (x,y): ").split()
        x,y = float(x),float(y)
        massa = float(input("Digite a massa: "))
        R = float(input("Digite o raio: "))        
        Astros.append([[x,y], massa, R])

    T, D = simulacao(Naves, Astros, niter, delta_t)
    for i in range(niter):
        print("********* iteração %d *********"%(i+1))
        for j in range(nnaves):
            print("*** Nave %d ***"%(j+1))
            print("Posição: ",end="")
            P = T[j][i]
            print("(%.3f,%.3f)"%(P[0],P[1]))
            print("Distância ao astro mais próximo: ",end="")
            print("%.3f"%(D[j][i]))

if __name__ == "__main__":
    main()
        
        



























