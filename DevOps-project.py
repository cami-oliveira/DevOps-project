print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") #Separar
print("") #pula uma linha na saída  
print("         Bem-vindo à Loja da Amora!")
print("Aqui quem fala é a Husky mais famosa da cidade.")
print("") #pula uma linha na saída
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") #Separar
print("") #pula uma linha na saída
print("Vamos fazer uma linha de crédito para você? Precisamos saber de alguns dados:") 
print("") #pula uma linha na saída

def obter_limite ():
    cargo_da_empresa_atual = str(input("Qual é o seu cargo atualmente?: "))#Lê o cargo
    salario = float(input("Qual é o seu salário?: ")) #Lê o salário
    data_nascimento = str(input ("Qual é a sua data de nascimento? dd/mm/aaaa: ")) #Lê a data de nascimento do cliente
    ano_de_nascimento = int(data_nascimento.split("/")[2]) #Busca apenas a parte do ano de nacimento
    print("") #pula uma linha na saída
    print("Seu cargo é:" , cargo_da_empresa_atual) #Imprime o cargo
    print("Seu salário é R$: %.2f"  %salario) #Imprime o salário
    print("Seu ano de nascimento é:" , ano_de_nascimento) #Imprime o ano de nascimento 
    print("") #pula uma linha na saída

    from datetime import datetime #Biblioteca para hora e data
    hoje=datetime.now() # Data corrente
    ano= hoje.strftime("%Y") # Ano corrente
    idade_cliente= int(ano) - ano_de_nascimento #Lê a idade do usuário
    print("Sua idade aproximada é de:" , idade_cliente , "anos") #Imprime a idade do usuário
    limite_de_gasto= float(salario * (idade_cliente/1000) + 100) #Lê o limite de gasto
    print("De acordo com a nossa análise de crédito, você poderá gastar até R$: %.2f" %limite_de_gasto) #Imprime o limite de gasto
    print("") #pula uma linha na saída
    return limite_de_gasto, idade_cliente #Retorna o limite de gasto e a idade 


def verificar_produto (limite_de_gasto, idade_cliente):
    print("") #pula uma linha na saída
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") #Separar
    print("") #pula uma linha na saída
    nome_produto = str(input("Nome do produto: ")) #Lê o nome do produto
    preco_produto = float(input("Preço do produto: ")) #Lê o preço do produto
    print("") #pula uma linha na saída

    nome_completo_sistema = "Camilla Cidral da Costa Oliveira" #Lê o nome do vendedor para calcular o desconto, nesse caso, o meu nome completo
    primeiro_nome = str(nome_completo_sistema.split(" ")[0]) # Busca apenas o primeiro nome
    tamanho_nome_completo_sistema = len(nome_completo_sistema) # Busca o tamanho do nome completo em caracteres
    tamanho_primeiro_nome = len(primeiro_nome) #busca o tamanho do primeiro nome em caracteres
    print("O nome da vendedora é:", nome_completo_sistema) # Imprime o nome do vendedor
    print("O nome tem:", tamanho_nome_completo_sistema, "caracteres") #Imprime o tamanho do nome completo 
    print("O primeiro nome tem:", tamanho_primeiro_nome,"caracteres") #Imprime o tamanho do primeiro nome
    print("") #pula uma linha na saida

    porcentagem_preco_produto = float((preco_produto*100)/limite_de_gasto) #Calcula a porcentagem do preço do produto
    bloqueado=0 #flag de controle para calcular o desconto depois das condições
    if porcentagem_preco_produto <= 60:
        print("Liberado!")
    elif porcentagem_preco_produto <= 90:
        print("Liberado ao parcelar em até 2 vezes")
    elif porcentagem_preco_produto <= 100:
        print("Liberado ao parcelar em 3 ou mais vezes")
    else:
        print("Bloqueado")
        bloqueado=1
        
    if (not bloqueado):
        if (tamanho_nome_completo_sistema<preco_produto<idade_cliente):
            desconto = tamanho_primeiro_nome
            print("Seu desconto será de: %.2f" %desconto, "reais")
            preco_final= preco_produto - desconto
            print("Valor do produto com desconto é de: %.2f" %preco_final , "reais")
            return preco_final
        else:
            print("Não há desconto.")

        return preco_produto

    print("") #pula uma linha na saída
    return 0

            

limite, idade_cliente = obter_limite()


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") #Separar
print("") #pula uma linha na saída
qtde_produtos = int(input("Quantos produtos você deseja cadastrar? ")) #Busca a quantidade de produtos que o cliente deseja cadastrar
print("Você deseja cadastrar: ", qtde_produtos, "produtos") #Imprime a quantidade de produtos 
n=qtde_produtos
compra_valor_total = 0
for i in range(n):
    valor = verificar_produto(limite, idade_cliente)
    limite -= valor
    print("Seu limite de compra atualizado é de: %.2f" %limite, "reais") #Imprime o limite restante
    compra_valor_total += valor

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") #Separar
print("") #pula uma linha na saída
print("Seu valor total da compra é de: %.2f" %compra_valor_total, "reais") #Imprime o valor total que o cliente gastou
print("Seu limite de compra atualizado é de: %.2f" %limite, "reais") #Imprime o limite restante
print("") #pula uma linha na saída
print("Volte sempre...")
print("") #pula uma linha na saída
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") #Separar




    
            
