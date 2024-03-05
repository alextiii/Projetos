class Restaurante:
    def __init__(self):
        self.menu = {
            '1': {'nome': 'Hamburguer', 'preco': 10.0},
            '2': {'nome': 'Pizza', 'preco': 15.0},
            '3': {'nome': 'Salada', 'preco': 8.0},
            # Adicione mais itens ao menu conforme necessário
        }
        self.pedido = []

    def mostrar_menu(self):
        print("=== Menu ===")
        for chave, prato in self.menu.items():
            print(f"{chave}. {prato['nome']} - R${prato['preco']}")

    def fazer_pedido(self):
        while True:
            self.mostrar_menu()
            escolha = input("Escolha um prato (ou 'fim' para finalizar o pedido): ")

            if escolha.lower() == 'fim':
                break

            if escolha in self.menu:
                quantidade = int(input("Quantidade: "))
                self.pedido.append({'prato': self.menu[escolha]['nome'], 'quantidade': quantidade})
            else:
                print("Opção inválida. Tente novamente.")

    def mostrar_pedido(self):
        print("\n=== Seu Pedido ===")
        for item in self.pedido:
            print(f"{item['quantidade']}x {item['prato']}")
        total = sum(self.menu[prato['prato']]['preco'] * prato['quantidade'] for prato in self.pedido)
        print(f"Total a pagar: R${total:.2f}")


# Exemplo de uso
restaurante = Restaurante()
restaurante.fazer_pedido()
restaurante.mostrar_pedido()
