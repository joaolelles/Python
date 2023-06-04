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

fruits.index("maçã")  # retorna o índice onde a fruta está localizada, neste caso, 1

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
)  # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

permissions.union(
    {"user"}
)  # novos conjuntos imutáveis podem ser criados à partir do original, mas o mesmo não pode ser modificado

permissions.intersection(
    {"user", "member"}
)  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# dict
people_by_id = {
    1: "Maria",
    2: "Fernanda",
    3: "Felipe",
}  # elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves

people_by_name = {
    "Maria": 1,
    "Fernanda": 2,
    "Felipe": 3,
}  # outro exemplo, dessa vez usando strings como chaves. As aspas são necessárias para que o Python não ache que `Maria`, `Fernanda` e `Felipe` sejam variáveis.

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
