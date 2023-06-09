# 1.1
my_age = 18
print(my_age)
team_names = ["Eli", "João", "Ann"]


# int
a = 5
type(a)

# float
a = 5.0
type(a)

# str
a = "olá"
# sequência(list, tuple, range)
# conjuntos(set, frozenset)
# mapeamento(dict)
# sequências binárias(bytes, bytearray, memoryview)

# list
fruits = [
    "laranja",
    "maçã",
    "uva",
    "abacaxi",
]  # elementos são definidos separados por vírgula, envolvidos por colchetes

fruits[0]  # o acesso é feito por índices iniciados em 0

fruits[-1]  # o acesso também pode ser negativo

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("abacaxi")  # removendo uma fruta

fruits.extend(
    ["pera", "melão", "kiwi"]
)  # acrescenta uma lista de frutas a lista original

fruits.index("maçã")  # retorna o índice onde a fruta está localizada,
# neste caso, 1

fruits.sort()  # ordena a lista de frutas

# tuple
user = (
    "Will",
    "Marcondes",
    42,
)  # elementos são definidos separados por vírgula, envolvidos por parênteses

user[0]  # acesso também por índices

# set
permissions = {
    "member",
    "group",
}  # elementos separados por vírgula, envolvidos por chaves

permissions.add("root")  # adiciona um novo elemento ao conjunto

permissions.add(
    "member"
)  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

permissions.union({"user"})  # retorna um conjunto resultado da união

permissions.intersection(
    {"user", "member"}
)  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# fronzenset
permissions = frozenset(
    ["member", "group"]
)  # assim como o set, qualquer estrutura iterável pode ser utilizada
# para criar um frozenset

permissions.union(
    {"user"}
)  # novos conjuntos imutáveis podem ser criados à partir do original,
# mas o mesmo não pode ser modificado

permissions.intersection(
    {"user", "member"}
)  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# dict
people_by_id = {
    1: "Maria",
    2: "Fernanda",
    3: "Felipe",
}  # elementos no formato "chave: valor" separados por vírgula,
# envolvidos por chaves

people_by_name = {
    "Maria": 1,
    "Fernanda": 2,
    "Felipe": 3,
}  # outro exemplo, dessa vez usando strings como chaves. As aspas
# são necessárias para que o Python não ache que `Maria`,
# `Fernanda` e `Felipe` sejam variáveis.

# elementos são acessados por suas chaves
people_by_id[1]  # saída: Maria

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(2, "Fernanda"), (3, "Felipe")])
# é retornada uma coleção iterável de tuplas contendo chaves e valores


# range
# vamos converter o range em uma lista para ajudar na visualização

# definimos somente o valor de parada
list(range(5))  # saída: [0, 1, 2, 3, 4]

# definimos o valor inicial e o de parada
list(range(1, 6))  # saída: [1, 2, 3, 4, 5]

# definimos valor inicial, de parada e modificamos o passo para 2
list(range(1, 11, 2))  # saída: [1, 3, 5, 7, 9]

# podemos utilizar valores negativos para as entradas também
list(range(10, 0, -1))  # saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# if/ elif / else
position = ""
salary = "3500"

if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"

# for
# Quando um cliente pede a listagem de restaurantes, ele pode escolher filtrar o resultado de acordo com a nota. Essa filtragem pode ocorrer percorrendo a lista de restaurantes ou criando uma nova lista com somente aqueles que atendem ao filtro, assim como mostra o exemplo abaixo:
restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# Em alguns casos, podemos ainda querer percorrer uma sequência numérica, e para isto iteramos sobre a estrutura de dados range.
for index in range(5):
    print(index)

# Compreensão de lista
# A compreensão de listas é declarada da mesma maneira que uma lista comum, porém no lugar dos elementos nós colocamos a iteração que vai gerar os elementos da nova lista.
min_rating = 3.0
filtered_restaurants = [
    restaurant for restaurant in restaurants if restaurant["nota"] > min_rating
]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# Poderíamos listar também somente o nome dos restaurantes, veja o exemplo abaixo:
min_rating = 3.0
filtered_restaurants = [
    restaurant["name"]  # aqui pedimos somente o nome do restaurante
    for restaurant in restaurants
    if restaurant["nota"] > min_rating
]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# A compreensão de listas também funciona com listas de strings. A seguinte cria uma nova lista de strings com os nomes que contém a letra ‘a’.
names_list = ["Duda", "Rafa", "Cris", "Yuri"]
new_names_list = [name for name in names_list if "a" in name]

# Aqui o for percorre cada nome em "names_list", verifica se existe a letra "a" nele,
# o adiciona à variável "name", e então gera nossa nova lista "new_names_list"
print(new_names_list)

# Saída
["Duda", "Rafa"]

# O exemplo a seguir usa uma compreensão de listas para criar uma lista com o quadrado dos números entre 1 e 10.
quadrados = [x * x for x in range(11)]
print(quadrados)

# Saída
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# while
# Com o while nós podemos executar um conjunto de declarações
# enquanto a condição for verdadeira.
# No código abaixo mostramos uma implementação da Sequência de Fibonacci,
# presente em diversas formas na natureza. Ela é uma sequência numérica começando por 0 e 1, e cada termo subsequente corresponde à soma dos dois anteriores.
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next

# enumerate
languages = ["Python", "Java", "JavaScript"]

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
print(list(enumerate_prime))

# Saída: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


# funções
def soma(x, y):
    return x + y


soma(2, 2)  # os parâmetros aqui são posicionais

soma(x=2, y=2)  # aqui estamos nomeando os parâmetros

len([1, 2, 3, 4])  # função len não aceita argumentos nomeados

len(obj=[1, 2, 3, 4])  # este código irá falhar

print("Coin", "Rodrigo", ", ")  # imprime Coin Rodrigo ,

print(
    "Coin", "Rodrigo", sep=", "
)  # nomeando o terceiro parâmetro, agora temos a saída: Coin, Rodrigo


def concat(*strings):
    # Equivalente a um ", ".join(strings), que concatena os elementos de um iterável em uma string utilizando um separador
    # Nesse caso a string resultante estaria separada por vírgula
    final_string = ""
    for string in strings:
        final_string += string
        if not string == strings[-1]:
            final_string += ", "
    return final_string


# pode ser chamado com 2 parâmetros
concat("Carlos", "Cristina")  # saída: "Carlos, Cristina"

# pode ser chamado com um número n de parâmetros
concat("Carlos", "Cristina", "Maria")  # saída: "Carlos, Cristina, Maria"

# dict é uma função que já vem embutida no python
dict(
    nome="Felipe", sobrenome="Silva", idade=25
)  # cria um dicionário utilizando as chaves passadas

dict(
    nome="Ana", sobrenome="Souza", idade=21, turma=1
)  # o número de parâmetros passados para a função pode variar
