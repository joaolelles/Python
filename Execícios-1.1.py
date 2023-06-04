# Operações básicas
# Exercício 1a = 10
b = 5

print(a + b)
# 15
print(a - b)
# 5
print(a * b)
# 50
print(a / b)
# 2.0
print(a // b)
# 2
print(a**b)
# 100000
print(a % b)
# 0

# Exercício 2
hours = 6
minutes = hours * 60
seconds = minutes * 60
print(hours)
# 6
print(minutes)
# 360
print(seconds)
# 21600

# Exercício 3
# Opcional:
x = 5
print(x)

# Obrigatório:
# x = 5; y = 10; z = x + y
# print(z)

# Exercício 4
books = 60
book_price = (1 - 0.4) * 24.20
logistic = 3 + (books - 1) * 0.75
cost = books * book_price + logistic
print(cost)

# Tipos de dados embutidos
trybe_course = ["Introdução", "Front-end", "Back-end"]

# Execício 5
trybe_course.append("Ciência da Computação")

# Exercício 6
trybe_course[0] = "Fundamentos"

# Exercício 7
nome = set()
nome.add("João")
print(nome)

# Exercício 8 e 9
info = {
    "personagem": "Margarida",
    "origem": "Pato Donald",
    "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

# 8
info["recorrente"] = "sim"
print(dict)
# ou
info.update({"color": "red"})

# 9
del info["origem"]

# Exercício 10
# truple. usariamos uma list para adicionar ou editar os valores.

# Exercício 11
my_array = [20, 20, 1, 2]

freq_dict = {}

for item in my_array:
    if (item in freq_dict):
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1

for key, valor in freq_dict.items():
    print(f"{key} : {valor}")

# Saída
20: 2
1: 1
2: 1