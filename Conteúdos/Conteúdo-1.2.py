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
