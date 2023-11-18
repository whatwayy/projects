print('Bem vindo ao seu Identificador de Antecessor e Sucessor \n* +plus Calcular soma, Subtração, Multiplicação, Divisão \nExponenciação e Raízes(raíz quadrada e raíz cúbica)')
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
s = n1 + n2
# s = abreviatura de soma
su = n1 - n2
# su abreviatura de subtração
m = n1 * n2
# m abreviatura de multiplicação
d = n1 / n2
# d abreviatura de divisão
ex = n1 ** n2
# ex abreviatura de exponenciação
rq = n1 / pow(1/2) # ou sqrt(n1, 2) ou sqrt(n1, [variável que preferir])
# rq abreviatura de raíz quedrada
rc = n1 / pow(1/3) # ou sqrt(n1, 3) ou sqrt(n1, [variável que preferir])
# rc abreviatura de raíz cúbica
print('Resultados: \nsoma = {} + {} = {} \nsubtração = {} - {} = {} \nmultiplicação = {} * {} = {}\n divisão = {} / {} = {} \nexponenciação = {} ** {} = {} \nraíz quadrada = {} ')