# Revisão de Estruturas de Dados em Python 

Lucas Gabriel G. dos Santos - Engenheiro de Computação

lucas.gabriel@uninta.edu.br

## Adicionando implementação dos métodos de Fibonacci

Realizei a implementação de dois exemplos de código do livro "Problemas Clássicos de Ciências de Computação com Python". Nestes exemplos são apontados problemas decorrentes da quantidade de chamadas recursivas e como isto pode comprometer o desempenho da aplicação. 

No arquivo fib-memo.py fiz uso da estrutura de dicionário para armazenar passos já concluídos de casos já resolvidos em etapas anteriores. Um exemplo de como a memoização pode reduzir a quantidade de chamadas recursivas. 
Exemplo de saída com fibonacci.py:

    n = 6

Exemplo de saída com fib-memo.py:

    n = 5 e n = 20

❯ python fib-memo.py 
5
6765
```javascript
{
    "0": 0,
    "1": 1,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 5,
    "6": 8,
    "7": 13,
    "8": 21,
    "9": 34,
    "10": 55,
    "11": 89,
    "12": 144,
    "13": 233,
    "14": 377,
    "15": 610,
    "16": 987,
    "17": 1597,
    "18": 2584,
    "19": 4181,
    "20": 6765
}
```

## Update 01: Conversão para o formato de módulos

Como realizei a implementação do método de fibonacci com memoização e com o uso de cache optei por ter um módulo próprio com
as funções, por hora pertencentes a arquivo distintos.

Para criar um módulo é necessário adicionar uma nova pasta ao projeto com o arquivo __init__.py. 

para importar de um módulo pode-se fazer:

    from nome_do_modulo.nome_do_arquivo import nome_da_func 

Demais detalhes e otimizações poderãos ser feitos futuramente.

## Árvore binária de busca


Árvores são estruturas muito práticas para algumas classes de problemas. 
Pretendo abordar mais deste assunto a partir deste repositório, planejando atualizações semanais. 

