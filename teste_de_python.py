
#Exercicio 1
interv = list(range(5000001)) # intervalo onde serão analisados se os numeros obedecem ou não a condição

alg1 = sum(map(lambda i: (i%2 ==0) & (i%49==0) & ((i%37==0)),interv))
#Resposta do algoritimo 
print(alg1) 

#########################################################################

#Exercicio 2 (uso da biblioteca math)


def f(i):
    """
    calcula o valor das posições pares
    """
    import math
    return(3**i +7 * math.factorial(i))


def g(i):
    """
    calcula o valor das posições impares
    """
    import math
    return(2**i + 4*math.log(i))


vet = [f(i)  if (i%2 == 0) else g(i) for i in list(range(10))]

posição_max = vet.index(max(vet))
media= round(sum(vet)/len(vet),2)
print(f'A posição com o maior elemento será a {posição_max}. A Media dos valores será {media}')




#########################################################################
#Exercicio 3
def alg3(notas):
    alunos = {}
    for i in range(len(notas)):
        alunos[f'Aluno{i+1}'] = notas[i]
    
    return (f'O aluno com a maior nota foi o {max(alunos,key=alunos.get)}, com uma nota igual a {max(alunos.values())}')

#Resposta do algoritimo (exemplo)
print(alg3([5,6,8,4.5,3]))
    


