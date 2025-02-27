# Estrutura de dados não lineares

*Edilson Gomes*

## Rb_Tree_Products


A implementação é feita com **Python** e começa importando algumas *bibliotecas*, como **random** (para gerar preços aleatórios) e **time** (para medir o tempo das buscas). A estrutura de dados principal é encapsulada na classe **ProductRBTree**, que utiliza a **RBTree** da biblioteca **bintrees**. Existem outras opções comentadas no código, como **AVLTree** e **SortedDict**, que são variações de árvores balanceadas, vão ser usadas separadamente para poder comparar o tempo usado na busca.  

Dentro da classe, o método **insert()** adiciona um produto à árvore. Como os preços são as chaves, se houver mais de um produto com o mesmo preço, as descrições são armazenadas em uma lista dentro da chave correspondente. Isso permite que produtos com valores idênticos não se sobrescrevam.  

Depois, temos dois métodos para buscar produtos: um para recuperar os que estão abaixo de um determinado valor **get_products_below()** e outro para os que estão acima **get_products_above()**. Ambos percorrem a árvore e filtram os preços conforme o critério solicitado.  

No trecho principal do código, são gerados 10.000 produtos com preços aleatórios entre R$10,00 e R$200,00, que são inseridos na árvore. Em seguida, são feitas as buscas para separar os produtos abaixo e acima de R$100,00, e o tempo gasto nessa operação é medido. No final, o código exibe quantos produtos caíram em cada categoria e o tempo que levou para buscar essas informações, o arquivo **resultados.txt** exibi as comparações de busca de árvore.  

### Arquivos
* [ProductRBTree.py](./ProductRBTree.py)  
* [resultados.txt](./resultados.txt)  
* [bintrees código-fonte](https://github.com/mozman/bintrees?tab=readme-ov-file)  
A biblioteca **bintrees** foi descontinuada, mas podemos análisar sua documentação nesse [link](https://pypi.org/project/bintrees/).