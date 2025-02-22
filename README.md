# Rb_Tree_Products
### Projeto implementação arvore rubro negra.  
Utilize a estrutura de dados árvore binária para resolver um problema real. Pode ser feito em qualquer linguagem. Utilize uma que tenha a implementação de arvore rubro negra. (*TreeMap no Java, por exemplo*).

**Sugestão:** Crie uma aplicação que armazene produtos com descrição e valor em uma estrutura de arvore rubro negra. 

Gere subgrupos de produtos com preço abaixo de R$100,00 e outro com preços acima de R$100,00.

Simule uma quantidade de pelo menos 10 mil produtos.

## Rb_Tree_Products  
Obtei escolher a linguagem Python, que sou mais familharizado, utilizando a biblioteca **bintrees**, que é uma biblioteca de python direcionada para arvores binárias especialmente AVL e RB, com **bintrees** invoco **RBTree**, que é a árvore pedido no projeto, e a **AVLTree** para poder comparar o tempo de buscar entre as duas. Também importei a biblioteca **SortedContainers**, que também tem arvores binárias, nela invoco a **SortedDict** (que representa uma árvore binária aproximada da rubro-negra, mas com uma otimização melhorada) também para poder comparar o tempo de buscar com a **RBTree**. Utilizo também as bibliotecas **time**(para usar os metodos de contagem de tempo) e **random**(para poder registrar os produtos com valores aleatórios. Segue o link para acessar o código: [ProductRBTree.py]().
No arquivo de [anotações.txt]() informa o tempo gasto de cada árvore binária usada com as mesmas quantidades de produtos registrados.
