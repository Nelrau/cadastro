menu = {
    'produto': 'preço',
    'produto1': 'preço',
    'produto2': 'preço',
    'produto3': 'preço'
}
class loja:
    def __init__(self, produto):
        self.produto = produto


    def quantidade(self):
        valor = int(input('Quantidade:'))
        return valor

    def custo(self):
        total = menu.get(self.produto)
        return total


while True:
    mercadoria = input('Mercadoria:')
    while True:
        r = input('Quer comprar mais? ').lower()[0]
        if r in 'sn':
            break
        print('apenas s ou n')
    if r == 'n':
        break


#if mercadoria == 'produto':
        #print(menu.items())'''
