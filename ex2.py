# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a 
# soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um 
# programa na linguagem que desejar onde, informado um número, ele calcule a sequência de 
# Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou 
# pode ser previamente definido no código;

# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(n):
    # Iniciando a sequência de Fibonacci
    fib_1, fib_2 = 0, 1

    # Verificando se o número informado é 0 ou 1 (pertence à sequência)
    if n == 0 or n == 1:
        return f"O número {n} pertence à sequência de Fibonacci."
    
    # Gerando a sequência até encontrar o número ou ultrapassá-lo
    while fib_2 < n:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    # Verificando se o número é encontrado na sequência
    if fib_2 == n:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Exemplo de uso da função
pertence_fibonacci(21)  # Testando com o número 21, que pertence à sequência