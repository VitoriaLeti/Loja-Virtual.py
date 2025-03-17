import produtos


carrinho = []
print("\nBem-vindo a Papelaria da Vitoria!")
print("Esses são os produtos disponíveis para montar seu carrinho:")

#função exibir produtos
def exibir_produtos():
    print("Produtos disponíveis:")
    for produto in produtos.produtos:
        print(f"Nome: {produto['nome']}, Preço: R${produto['preco']}, Estoque: {produto['estoque']} unidades")

exibir_produtos()
 


#funcao adicionar carrinho de compras


def adicionar_carrinho(produto, unidades):
    for item in produtos.produtos:
        if item["nome"] == produto:
            if item["estoque"] >= unidades:
                carrinho.append({"nome": produto, "unidades": unidades, "preco_unitario": item["preco"]})
                item["estoque"] -= unidades
                print(f"{unidades} x {produto} adicionado ao carrinho")
                return
            else:
                print("Produto indisponível ou quantidade maior do que o estoque disponível")
                return
    print("Produto não encontrado.")


# Função para exibir total da compra
def exibir_total(com_desconto=False,desconto=0):
    total = sum(item["preco_unitario"] * item ["unidades"] for item  in carrinho)
    if com_desconto:
        total_com_desconto=total *(1-desconto/100)
        print(f"Total da compra com {desconto}% de desconto: R$ {total_com_desconto:.2f}")
    else:
        print(f"Total da compra: R$ {total:.2f}")


# Loop para montar o carrinho
while True:
    try:
        produto_nome = input("\nDigite o nome do produto que você deseja adicionar ao carrinho (ou 0 para finalizar): ")
        if produto_nome == '0':
            print("Finalizando montagem do carrinho...")
            break

        unidades = int(input("Digite a quantidade desejada: "))
        if unidades <= 0:
            print("Quantidade inválida! Tente novamente.")
            continue

        adicionar_carrinho(produto_nome, unidades)

    except ValueError:
        print("Entrada inválida! Tente novamente.")



# Exibir carrinho final
print("\nSeu carrinho de compras:")
for i, item in enumerate(carrinho, start=1):
   print(f"{i} - {item['unidades']} x {item['nome']} (Preço unitário: R${item['preco_unitario']})")

# Função para aplicar desconto
def aplicar_desconto(total):
    if total >= 200:
        desconto = 20
    elif total >= 100:
        desconto = 10
    else:
        print("Total menor que R$ 100. Desconto não aplicado.")
        return total

    total_com_desconto = total * (1 - desconto / 100)
    print(f"Desconto de {desconto}% aplicado. Total com desconto: R$ {total_com_desconto:.2f}")
    return total_com_desconto
#funcao aplicar desconto
while True:
    aplicar_desconto_input=input("deseja aplicar o desconto?(sim ou não)").lower()
    if aplicar_desconto_input == 'sim':
     total=sum(item["preco_unitario"]*item["unidades"]for item in carrinho)
     total_com_desconto_input = aplicar_desconto(total)
     break
    elif aplicar_desconto_input =='não':
        total_com_desconto= sum(item["preco_unitario"]*item["unidades"]for item in carrinho)
        break
    else:
        print("Resposta inválida! Tente novamente.")





print("\nObrigado por comprar na Papelaria da Vitória!")



