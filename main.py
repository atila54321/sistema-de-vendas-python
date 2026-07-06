produtos = []
historico = []
total_vendido = 0


while True:
    print("\n==== SISTEMA DE VENDAS ====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Realizar venda")
    print("5 - Histórico de vendas")
    print("6 - Ver total vendido")
    print("7 - Repor estoque")
    print("8 - Remover produto")
    print("9 - Estatísticas")
    print("10 - Sair")

    opcao = input("Escolha uma opção: ")

    # CADASTRAR PRODUTO
    if opcao == "1":
        nome = input("Nome do produto: ").strip()

        if nome == "":
            print("❌ O nome não pode ficar vazio!")
            continue

        if any(p["nome"].lower() == nome.lower() for p in produtos):
            print("❌ Produto já cadastrado!")
            continue

        try:
            preco = float(input("Preço: R$"))

            if preco <= 0:
                print("❌ O preço deve ser maior que zero!")
                continue

            estoque = int(input("Quantidade em estoque: "))

            if estoque < 0:
                print("❌ O estoque não pode ser negativo!")
                continue

        except ValueError:
            print("❌ Digite valores válidos!")
            continue

        produto = {
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }

        produtos.append(produto)
        print("✅ Produto cadastrado com sucesso!")

    # LISTAR PRODUTOS
    elif opcao == "2":
        print("\n==== PRODUTOS CADASTRADOS ====")

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(
                    f'Produto: {produto["nome"]} | '
                    f'Preço: R${produto["preco"]:.2f} | '
                    f'Estoque: {produto["estoque"]}'
                )

    # BUSCAR PRODUTO
    elif opcao == "3":
        nome = input("Digite o nome do produto: ").strip()

        encontrado = False

        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                print(
                    f'Produto: {produto["nome"]} | '
                    f'Preço: R${produto["preco"]:.2f} | '
                    f'Estoque: {produto["estoque"]}'
                )
                encontrado = True
                break

        if not encontrado:
            print("❌ Produto não encontrado!")

    # REALIZAR VENDA
    elif opcao == "4":
        nome = input("Digite o nome do produto: ").strip()

        produto_encontrado = None

        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                produto_encontrado = produto
                break

        if produto_encontrado is None:
            print("❌ Produto não encontrado!")
            continue

        try:
            quantidade = int(input("Quantidade: "))

            if quantidade <= 0:
                print("❌ Quantidade inválida!")
                continue

        except ValueError:
            print("❌ Digite um número válido!")
            continue

        if quantidade > produto_encontrado["estoque"]:
            print("❌ Estoque insuficiente!")
            continue

        valor = quantidade * produto_encontrado["preco"]

        produto_encontrado["estoque"] -= quantidade
        total_vendido += valor

        venda = {
            "produto": produto_encontrado["nome"],
            "quantidade": quantidade,
            "total": valor
        }

        historico.append(venda)

        print(f"✅ Venda realizada! Total: R${valor:.2f}")

    # HISTÓRICO DE VENDAS
    elif opcao == "5":
        print("\n==== HISTÓRICO DE VENDAS ====")

        if len(historico) == 0:
            print("Nenhuma venda realizada.")
        else:
            for venda in historico:
                print(
                    f'Produto: {venda["produto"]} | '
                    f'Quantidade: {venda["quantidade"]} | '
                    f'Total: R${venda["total"]:.2f}'
                )

    # TOTAL VENDIDO
    elif opcao == "6":
        print(f"💰 Total arrecadado: R${total_vendido:.2f}")

    # REPOR ESTOQUE
    elif opcao == "7":
        nome = input("Produto: ").strip()

        encontrado = False

        for produto in produtos:
            if produto["nome"].lower() == nome.lower():

                try:
                    quantidade = int(
                        input("Quantidade a adicionar: ")
                    )

                    if quantidade <= 0:
                        print("❌ Quantidade inválida!")
                        encontrado = True
                        break

                    produto["estoque"] += quantidade
                    print("✅ Estoque atualizado!")

                except ValueError:
                    print("❌ Digite um número válido!")

                encontrado = True
                break

        if not encontrado:
            print("❌ Produto não encontrado!")

    # REMOVER PRODUTO
    elif opcao == "8":
        nome = input("Digite o produto para remover: ").strip()

        removido = False

        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                produtos.remove(produto)
                print("✅ Produto removido!")
                removido = True
                break

        if not removido:
            print("❌ Produto não encontrado!")

    # ESTATÍSTICAS
    elif opcao == "9":
        print("\n==== ESTATÍSTICAS ====")
        print(f"Total de produtos cadastrados: {len(produtos)}")
        print(f"Total arrecadado: R${total_vendido:.2f}")

        if len(historico) == 0:
            print("Nenhuma venda realizada.")
        else:
            vendas_produtos = {}

            for venda in historico:
                nome = venda["produto"]

                if nome not in vendas_produtos:
                    vendas_produtos[nome] = 0

                vendas_produtos[nome] += venda["quantidade"]

            mais_vendido = max(
                vendas_produtos,
                key=vendas_produtos.get
            )

            print(
                f"Produto mais vendido: "
                f"{mais_vendido} "
                f"({vendas_produtos[mais_vendido]} unidades)"
            )

    # SAIR
    elif opcao == "10":
        print("Encerrando sistema...")
        break

    else:
        print("❌ Opção inválida!")