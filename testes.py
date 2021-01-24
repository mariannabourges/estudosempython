'''
dia = 3
mes = "Março"
ano = 2021

print("Eu faço aniversário em {} de {} de {}.".format(dia,mes,ano))
'''


# nome = "clarice"
# nome = nome.capitalize()
# print(nome) #resultado = Clarice


''' palavra = "alura"
palavra.upper()
print(palavra) #qual é o resultado? = alura '''


'''# coding: utf-8
frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')
fruta_pedida = fruta_pedida.strip()
if(fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')
'''


'''precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]
print( min(precos)) # min() imprime o menor número da LISTA e max() o maior número da LISTA'''


'''funcionarios = ['Astrid','Flavia','Talia', ... ,'Mauricio', 'Waldemar', 'Marina']
print(funcionarios)
print(len(funcionarios)) # len() retorna o tamanho da lista'''


'''frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))  # RESULTADO = 3, volta o valor do índice do elemento na lista'''


'''frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))
#Assim temos certeza que a fruta_buscada está dentro da lista antes de 
#perguntarmos o seu índice, evitando assim de receber um erro no console.
'''


'''valores = ["a","b","c","d","e"]
del(valores[0]) #funciona pois é lista, não funciona com tupla
print(valores) #resultado é a retirada do A'''


'''#list usa colchetes [] para inicialização, tuple usa parênteses ()
#list é mutável, tuple é imutável
#Entre essas sequências, list é a única que é mutável. tuple, str e range são imutáveis.
# Range se comporta como tuples e strs.

lista = [4,3,2,1]
tuple = (4,3,2,1)'''



'''#tupla e lista permitem elementos duplicados, então ao usar chaves { }, não é possível duplicar elementos
#isto se chama set, set não é uma sequência, pois não tem índice, assim,
#ao fazer print, os elementos aparecem desordenados
colecao = {11122233344, 22233344455, 33344455566}
colecao.add(4455663388) #adicionar mais um elemento à coleção
print(colecao)'''



''' #A estrutura abaixo é um Dictionary. No lado esquerdo a chave e no lado direito o valor.
#Isso ajuda quando não sabemos um índice de um elemento, mas podemos buscá-lo pela 
#nome (a chave em dicionário), como no caso abaixo:

instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
print(instrutores['Flavio'])'''


'''total = 0
palavra = "python rocks!"
acabou = False
while (not acabou):
    acabou = (total == len(palavra))
    total = total + 1
print(total-1) 
# Por que (total - 1)????
#Pois na ultima execução ele verificara que total ==len(palavra) e em seguida
#fara novamente a soma total +1, para então sair do loop, o que vai fazer com 
#que total seja igual ao tamanho da palavra mais 1 e para que seja exibido 
#corretamente esse 1 deve ser subtraído'''

# List Comprehension
#
# frutas = ["maçã", "banana", "laranja", "melancia"]
# lista = [fruta.upper() for fruta in frutas]
# print(lista)

# inteiros = [1,3,4,5,7,8]
# quadrados = [n*n for n in inteiros]
# print(quadrados)

inteiros = [1,3,4,5,7,8,9]
pares = [numero for numero in inteiros if numero%2 == 0]
print(pares)
