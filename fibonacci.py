# Implementando métodos para resolver a sequência de Fibonacci


## O método abaixo recebe um inteiro n e retorna o valor de fibonacci nesta posição
def fib(n:int)->int:
    if n < 2: # Caso de base 
        return n     
    return fib(n-2) + fib(n-1) #caso recursivo


# Executando o método fib() 
if __name__ == "__main__":
    print(fib(6))