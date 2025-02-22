import random
import time
from bintrees import RBTree, AVLTree  # Utiliza árvore rubro-negra internamente
from sortedcontainers import SortedDict  # Utiliza árvore rubro-negra internamente

class ProductRBTree:
    def __init__(self):
        self.tree = RBTree()
        #self.tree = AVLTree()
        #self.tree = SortedDict()

    # insere os produtos com valores e descrição na árvore rubro-negra
    def insert(self, price, description):
        if price in self.tree:
            self.tree[price].append(description)
        else:
            self.tree[price] = [description]
    
    # busca os produtos com valores abaixo do valor pedido.
    def get_products_below(self, threshold):
        return {k: v for k, v in self.tree.items() if k < threshold}
    
    # busca os produtos com valores acima do valor pedido
    def get_products_above(self, threshold):
        return {k: v for k, v in self.tree.items() if k >= threshold}

# Criando a árvore
product_tree = ProductRBTree()
amount = 10_000
# Simulando 10 mil produtos
for _ in range(amount):
    price = round(random.uniform(10, 200), 2)
    description = f"Produto {_}"
    product_tree.insert(price, description)

# Separando produtos em dois grupos
inicio = time.perf_counter()
products_below_100 = product_tree.get_products_below(100)
products_above_100 = product_tree.get_products_above(100)
final = time.perf_counter()

# Exibindo a contagem de produtos por grupo
print(f"{amount} produtos registrados.")
print(f"Produtos abaixo de R$100,00: {sum(len(v) for v in products_below_100.values())}")
print(f"Produtos acima de R$100,00: {sum(len(v) for v in products_above_100.values())}")
print(f'Tempo de busca: {final - inicio:.4f} segundos')
#print(product_tree.tree)