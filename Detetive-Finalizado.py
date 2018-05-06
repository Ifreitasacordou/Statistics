import random

#Limpar a tela do IDLE
def cls():
    print("\n"*100)

def espaco():
            print("\n")

def pergunta():
    perguntas = ["Pergunta 1 ?","Pergunta 2 ?","Pergunta 3 ?","Pergunta 4 ?"]
    r =  random.randrange(len(perguntas))            
    return perguntas[r]
    perguntas.pop[r]
    
def dica(x):
    dicas = ["Dica 1:\n V+F = 2+A","Dica 2:\n Dodecaedro é um polígono de Platão", "Dica 3:\n Use análise combinatória", "Dica 4:\n Um dodecadro tem 20 faces"]
    if x == 0:                  
        print("Você não receberá nenhuma dica")
    elif x == 1:                            
        for i in range(x):
            print(dicas[i])
    elif x == 2:                            
        for i in range(x):
            print(dicas[i])                            
    elif x == 3:
        for i in range(x):
            print(dicas[i])
    elif x == 4:
        for i in range(x):
            print(dicas[i])

    def desafios():        
        while gatilho != 0:
            desafio = input("Qual é o XXXX ?")
            print("A)euhuehu\nB)euhuehu\nC)euhuehu\nD)sdhaudh\n")
            if desafio != "a" or "A":
                print("Resposta inválida, tente outra vez !")
            else:
                print("Parabéns, você acertou o desafio você é o grande vencedor !!!")
                break            

print(45*"#")
print("##  Bem vindo ao Detetive com Matemática   ##")
print(45*"#")
espaco()
 
start = 0
while start != 1:
    start = input("Digite 1 para começar ou 0 para sair: \n")
    if start == '1':
        #nome = input('Digite seu nome: ')
        start = 1           

       
        instrucao = -1
        while instrucao != 1 or instrucao != 0:
            instrucao = input("Digite 1 para ler as regras ou 0 caso ja às conheça: \n")

            print("\n")
            if instrucao == '1':
                print("As regras são as seguintes: ")
                regras = ["Não consulte Terceiros","Após iniciado o jogo va até o final"]
                for i in range(len(regras)):
                    print(i+1,"-",regras[i])
                
                instrucao = 1                                
                print("\n")

                print("Vamos começar, boa sorte !")
                espaco()
            elif instrucao == '0':
                print("Vamos começar, boa sorte !")
                espaco()
                instrucao = 0
                

            desafio = 1 
            resposta = 0
            texto = ["Em uma circunferência são marcados 7 pontos distintos:A, B, C, D, E, F, G.\n Com estes pontos quantas cordas podem ser traçadas ?",
                     "Efetuando(2**0,5/2)*(2**0,25)**-2-(6/6**3**0,5)3**0,5+1, temos por resultado:",
                     "Em um estacionamento havia carros e motocicletas num total de 43 veículos e 150 rodas.\n Calcule o número de carros e motocicletas estacionados.",
                     "Uma empresa desejava contratar técnicos e, para isso aplicou uma prova, com 50 perguntas a todos os candidatos.\n Cada candidato ganhou 4 pontos para cada resposta errada.\nSe marcelo fez 130 pontos quantas perguntas ele acertou ?"]
            acertos = 0
            total_questoes = len(texto)
            
            while resposta != 1:
                for i in range(len(texto)):                    
                    p = texto[i]
                print(p,"\n")
                
                if p == texto[0]:
                    print("A)42\nB)14\nC)28\nD)Pular\n")
                    
                elif p == texto[1]:
                    print("A)17/36\nB)-71/12\nC)36/35\nD)Pular\n")
                    
                elif p == texto[2]:
                    print("A)20 Motos e 23 Carros\nB)11 Motos e 32 Carros\nC)13 Carros e 30 Motos\nD)Pular\n")
                    
                elif p == texto[3]:
                    print("A)56\nB)13\nC)36\nD)Pular\n")                  

                    
                resposta = input("Qual a alternativa correta ?\n")
                dicas = 0
                
                if p == texto[0]:
                    
                    if resposta == 'C' or resposta == 'c':
                        print(36*"#")
                        print("Parabéns a resposta está correta !")
                        print(36*"#")
                        acertos += 1
                        texto.pop(0)
                        espaco()
                    
##                  elif resposta == 'D' or resposta == 'd':
                       #print("Próxima questão")
                                           
                    else:
                        print(20*"#")
                        print("Resposta incorreta")
                        print(20*"#")
                        texto.pop(0)
                        espaco()
                        
                elif p == texto[1]:
                    if resposta == 'B' or resposta == 'b':
                        print(36*"#")
                        print("Parabéns a resposta está correta !")
                        print(36*"#")
                        acertos += 1
                        texto.pop(1)
                        espaco()
                    
##                    elif resposta == 'D' or resposta == 'd':
##                        print("Próxima questão")
                                           
                    else:
                        print(20*"#")
                        print("Resposta incorreta !")
                        print(20*"#")
                        texto.pop(1)
                        espaco()
                        
                elif p == texto[2]:
                    if resposta == 'C' or resposta == 'c':
                        print(36*"#")
                        print("Parabéns a resposta está correta !")
                        print(36*"#")
                        acertos += 1
                        texto.pop(2)
                        espaco()
                    
#                    elif resposta == 'D' or resposta == 'd':
#                        print("Próxima questão")
                                           
                    else:
                        print(20*"#")
                        print("Resposta incorreta !")
                        print(20*"#")
                        texto.pop(2)
                        espaco()
                        
                elif p == texto[3]:
                    if resposta == 'C' or resposta == 'c':
                        print(36*"#")
                        print("Parabéns a resposta está correta !")
                        print(36*"#")
                        acertos += 1
                        texto.pop(3)
                        espaco()
                    
#                    elif resposta == 'D' or resposta == 'd':
#                        print("Próxima questão")
                                                                   
                    else:
                        print(20*"#")
                        print("Resposta incorreta ! ")
                        print(20*"#")
                        texto.pop(3)
                        espaco()                
                   
                if (len(texto)) == 0 and acertos == 0:
                    print("Acabou o jogo, você não acertou nenhuma questão de um o total de", total_questoes,".")
                    print(70*"_")
                                        
                    while desafio != 0:
                        print("Desafio\n")
                        print("Sabe-se que o número total de vértices de um dodecaedro regular é 20 e que as faces são pentágonos.\nQuantas retas ligam dois vértices do dodecaedro não pertecentes à mesma face ?")
                        espaco()
                        print("A)60\nB)100\nC)30\nD)50\n")
                        df = input("Qual a alternativa correta ?\n")
                        espaco()
                        if df == 'b' or df == 'B':                                                       
                            print("Parabéns você é o grande vencedor !!!")
                            break
                        else:
                            print(20*"#")
                            print("Resposta incorreta")
                            print(20*"#")
                            espaco()
                    break 
                
                elif (len(texto)) == 0 and acertos == 1:
                    print("Acabou o jogo você acertou", acertos, "questão de um o total de", total_questoes,".")                    
                    print("Você tem direito a",acertos, "dicas.")
                    print(70*"_")
                    print("Dica: ")
                    espaco()
                    dica(acertos)
                    espaco()
                    
                    while desafio != 0:
                        print("Desafio\n")
                        print("Sabe-se que o número total de vértices de um dodecaedro regular é 20 e que as faces são pentágonos.\nQuantas retas ligam dois vértices do dodecaedro não pertecentes à mesma face ?")
                        espaco()
                        print("A)60\nB)100\nC)30\nD)50\n")
                        df = input("Qual a alternativa correta ?\n")
                        espaco()
                        if df == 'b' or df == 'B':                                                       
                            print("Parabéns você é o grande vencedor !!!")
                            break
                        else:
                            print(20*"#")
                            print("Resposta incorreta")
                            print(20*"#")
                            espaco()
                    break 
                
                elif (len(texto)) == 0 and acertos == 2:
                    print("Acabou o jogo você acertou", acertos, "questões de um o total de", total_questoes,".")                    
                    print("Você tem direito a",acertos, "dicas.")
                    print(70*"_")
                    print("Dicas: ")
                    espaco()
                    dica(acertos)
                    espaco()
                    
                    while desafio != 0:
                        print("Desafio\n")
                        print("Sabe-se que o número total de vértices de um dodecaedro regular é 20 e que as faces são pentágonos.\nQuantas retas ligam dois vértices do dodecaedro não pertecentes à mesma face ?")
                        espaco()
                        print("A)60\nB)100\nC)30\nD)50\n")
                        df = input("Qual a alternativa correta ?\n")
                        espaco()
                        if df == 'b' or df == 'B':                                                       
                            print("Parabéns você é o grande vencedor !!!")
                            break
                        else:
                            print(20*"#")
                            print("Resposta incorreta")
                            print(20*"#")
                            espaco()
                    break 
                
                elif (len(texto)) == 0 and acertos == 3:
                    print("Acabou o jogo você acertou", acertos, "questões  de um o total de", total_questoes,".")                   
                    print("Você tem direito a",acertos, "dicas.")
                    print(70*"_")
                    print("Dicas: ")
                    espaco()
                    dica(acertos)
                    espaco()                   
                    
                    while desafio != 0:
                        print("Desafio\n")
                        print("Sabe-se que o número total de vértices de um dodecaedro regular é 20 e que as faces são pentágonos.\nQuantas retas ligam dois vértices do dodecaedro não pertecentes à mesma face ?")
                        espaco()
                        print("A)60\nB)100\nC)30\nD)50\n")
                        df = input("Qual a alternativa correta ?\n")
                        espaco()
                        if df == 'b' or df == 'B':                                                       
                            print("Parabéns você é o grande vencedor !!!")
                            break
                        else:
                            print(20*"#")
                            print("Resposta incorreta")
                            print(20*"#")
                            espaco()
                    break
                
                elif (len(texto)) == 0 and acertos == 4:
                    print("Acabou o jogo você acertou", acertos, "questões  de um o total de", total_questoes,".")
                    print("Você tem direito a",acertos, "dicas.")
                    print(70*"_")
                    print("Dicas: ")
                    espaco()
                    dica(acertos)
                    espaco()
                    
                    while desafio != 0:
                        print("Desafio\n")
                        print("Sabe-se que o número total de vértices de um dodecaedro regular é 20 e que as faces são pentágonos.\nQuantas retas ligam dois vértices do dodecaedro não pertecentes à mesma face ?")
                        espaco()
                        print("A)60\nB)100\nC)30\nD)50\n")
                        df = input("Qual a alternativa correta ?\n")
                        espaco()
                        if df == 'b' or df == 'B':                                                       
                            print("Parabéns você é o grande vencedor !!!")
                            break
                        else:
                            
                            print(20*"#")
                            print("Resposta incorreta")
                            print(20*"#")
                            espaco()
                    break           
            break                 
    
    elif start == '0':
        print("Bye, bye")
        break
    else:
        print("Comando inválido !")
