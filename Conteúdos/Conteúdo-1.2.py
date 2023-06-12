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

# Manipulando arquivos JSON
import json  # json é um modulo que vem embutido, porém precisamos importá-lo


with open("pokemons.json") as file:
    content = file.read()  # leitura do arquivo
    pokemons = json.loads(content)[
        "results"
    ]  # o conteúdo é transformado em estrutura python equivalente, dicionário neste caso.
    # acessamos a chave results que é onde contém nossa lista de pokemons

print(pokemons[0])  # imprime o primeiro pokemon da lista

# A leitura pode ser feita diretamente do arquivo, utilizando o método load ao invés de loads. O loads carrega o JSON a partir de um texto e o load carrega o JSON a partir de um arquivo.
import json


with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

print(pokemons[0])  # imprime o primeiro pokemon da lista

# A escrita de arquivos no formato JSON é similar à escrita de arquivos comuns, porém temos que transformar os dados primeiro.
import json

# Leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# Abre o arquivo para escrevermos apenas o pokemons do tipo grama
with open("grass_pokemons.json", "w") as file:
    json_to_write = json.dumps(
        grass_type_pokemons
    )  # conversão de Python para o formato json (str)
    file.write(json_to_write)

# Assim como a desserialização, que faz a transformação de texto em formato JSON para Python, a serialização (caminho inverso) possui um método equivalente para escrever em arquivos de forma direta.
import json

# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformando em formato json a estrutura
    json.dump(grass_type_pokemons, file)


# Manipulando arquivos CSV
import csv

with open("graduacao_unb.csv", encoding="utf-8") as file:
    # Os valores padrão de 'delimiter' e 'quotechar' são os mesmos utilizados
    # abaixo. Você pode removê-los ou alterá-los conforme necessidade
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')

    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader

print(data)

# Podemos fazer uma análise e verificar quantos cursos são ofertados por departamento. Em seguida salvamos o resultado também no formato .csv:
import csv

with open("graduacao_unb.csv", encoding="utf8") as file:
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader

group_by_department = {}
for row in data:
    department = row[15]
    if department not in group_by_department:
        group_by_department[department] = 0
    group_by_department[department] += 1

# Escreve o relatório em .csv
# Abre um arquivo para escrita
with open("department_report.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Escreve o cabeçalho
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    writer.writerow(headers)

    # Escreve as linhas de dados
    # Desempacotamento de valores
    for department, grades in group_by_department.items():
        # Agrupa o dado com o turno
        row = [
            department,
            grades,
        ]
        writer.writerow(row)

# Existem ainda o leitor e o escritor baseados em dicionários. A principal vantagem é que não precisamos manipular os índices para acessar os dados das colunas. A desvantagem é o espaço ocupado em memória (que é maior que o comum), devido à estrutura de dados utilizada.
import csv

# lê os dados
with open("graduacao_unb.csv", encoding="utf-8") as file:
    graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')

    # A linha de cabeçalhos é utilizada como chave do dicionário
    # agrupa cursos por departamento
    group_by_department = {}
    for row in graduacao_reader:
        department = row["unidade_responsavel"]
        if department not in group_by_department:
            group_by_department[department] = 0
        group_by_department[department] += 1
