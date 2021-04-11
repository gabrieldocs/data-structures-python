# Esta implementação faz o uso cache para verificar casos conhecidos 
# a cada chamada já conhecida o valor é recuperado diretamete do cache 
# 2021

from functools import lru_cache

# utilizando um decorator para armazenar o cache 
# @lru_cache indica quantas chamadas recentes da função decorada devem ser armazenadas em cache
# passando None como valor para maxsize faz com que não haja um limite para a quantidade de chamadas armazenadas

@lru_cache(maxsize=None)
def fib(n: int)-> int:
    if n < 2:
        return n 
    else:
        return fib(n-2) + fib(n-1)

if __name__ == "__main__":
    print(fib(4))
    print(fib(8))
    print(fib(12))
    print(fib(12))
    print(fib(50))