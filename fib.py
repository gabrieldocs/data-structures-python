# Testando as funções com otimização para as chamadas recursivas 
# Realizei uma pequena mudança na estrutura do projeto, adicionando as funções de fibonacci para o formato de módulo 

from functions.fib_cache import fib_cache 
from functions.fib_memo import fib_memo 

if __name__ == "__main__":
    print("# Fibonacci using cache")
    print(fib_cache(4))    
    print(fib_cache(8))    
    print(fib_cache(20))    
    print(fib_cache(49))    
    print("# Fibonacci using memoizations")
    print(fib_memo(4))    
    print(fib_memo(8))    
    print(fib_memo(20))    