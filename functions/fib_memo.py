# Esta implementação faz o uso de dicionários para armazenar resultados já calculados e conhecidos
# Uma observação interessante é a de que um dicionário Python possui estrutura e declaração semelhante ao JSON 
# 2021
import json
from typing import Dict 

memo: Dict[int, int] = {
    0 :0, 
    1:1
} # Adicionando aos casos de base 

def fib_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n - 2) + fib_memo( n - 1 ) #etapa de memoização 
    return memo[n]

