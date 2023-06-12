# 1.2
# Entrada
user_input = input("Digite uma mensagem: ")
print("O valor recebido foi:", user_input)

# Saída
print("O resultado é", 42)  # saída: O resultado é 42
print("Os resultados são", 6, 23, 42)  # saída: Os resultados são 6 23 42

# O separador padrão dos argumentos é um espaço em branco, que pode ser alterado.
print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print(
    "Maria", "João", "Miguel", "Ana", sep=", "
)  # saída: Maria, João, Miguel, Ana

# Além do separador, podemos também alterar o caractere de fim de linha que, por regra, é uma quebra de linha:
print("Na mesma", end=" ")
print("linha.")
# saída: Na mesma linha.

# Existe um parâmetro que nos permite modificar a saída padrão para a saída de erros:
import sys

err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)

# Desempacotamento de valores
a, b = "cd"
print(a)  # saída: c
print(b)  # saída: d

head, *tail = (
    1,
    2,
    3,
)  # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
print(head)  # saída: 1
print(tail)  # saída: [2, 3]

# Manipulação de arquivos
# open
file = open(
    "arquivo.txt", mode="w"
)  # ao abrir um arquivo para escrita, um novo arquivo é criado mesmo que ele já exista, sobrescrevendo o antigo.
file.close()

# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    # como estamos DENTRO do contexto, verificamos que o arquivo está ABERTO
    # através do atributo booleano 'closed' (file.closed = False)
    print(file.closed)
# como estamos FORA do contexto, o arquivo está FECHADO (file.closed = True)
print(file.closed)


with open("arquivo.txt", "w") as file:
    #     file.write("nome idade\n")
    file.write("Maria 45\n")
    file.write("Miguel 33\n")


with open("arquivo.txt", "w") as file:
    #     file.write("Miguel 33\n")

    # Não precisa da quebra de linha, pois esse é um comportamento padrão do print
    print("Túlio 22", file=file)


with open("arquivo.txt", "w") as file:
    #   ...

    LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
    file.writelines(LINES)


# escrita
with open("arquivo.txt", "w") as file:
    file.write("Trybe")

# leitura
with open("arquivo.txt", "r") as file:
    content = file.read()
    print(content)


# escrita
with open("arquivo.txt", "w") as file:
    LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
    file.writelines(LINES)

# leitura
with open("arquivo.txt", "r") as file:
    for line in file:
        print(
            line
        )  # não esqueça que a quebra de linha também é um caractere da linha

# Lidando com exceções
# Tratamento de exceções
while True:
    try:
        x = int(input("Por favor digite um número inteiro: "))
        break
    except ValueError:
        # 'ValueError' é a exceção que ocorre quando a função int() recebe um
        # valor que não pode ser traduzido para número inteiro
        print("Oops! Esse não era um número inteiro. Tente novamente...")

# Lidando com exceções enquanto manipulamos arquivos
try:
    with open("arquivo.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    # será executado caso haja a exceção 'FileNotFoundError'
    print("Arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("Arquivo manipulado e fechado com sucesso")
finally:
    # será sempre executado, independentemente de erro
    print("Fim da tentativa de ler o arquivo")
