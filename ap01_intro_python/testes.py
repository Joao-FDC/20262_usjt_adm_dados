import pandas as pd
# 21 tabela com panda

pedidos = pd.DataFrame({
    "id_cliente": [1, 2, 1, 3],
    "valor": [100, 200, 50, 80]
})

clientes = pd.DataFrame({
    "id_cliente": [1, 2, 3],
    "nome": ["Ana", "Bruno", "Carla"],
    "cidade": ["SP", "Rio", "BH"]  
})

completo = pedidos.merge(clientes, on="id_clientes")
print(completo)

df = pd.read_csv(
    "clientes.csv",

    sep=",",
    decimal = ".",
    encoding = "utf-8"
)
# df["com_frete"] = df["valor"] + 15
# df["faixa"] = df["valor"].apply(
#     lambda v: "alto" if v > 100 else "baixo"
# )
# print(   
#     df.sort_values("valor", ascending=False).head(3)
# )   


# print(df.groupby("cidade")["valor"].mean()) #agrupa os valores por cidade

print(
    df.groupby("cidade").agg(
        total=("valor", "sum"),
        media=("valor", "mean"),
        pedidos=("valor", "count")
    )
)

# print(df[["cliente", "valor", "faixa"]])
# print(df.head)



# print(df.isnull().sum())
# df["valor"].fillna(0) #substitui null por 0
# print(df.head())
# serie = pd.Series(["1.234,56" , "89.9", "abc"])
# numeros = serie.str.replace(".","", regex=False) #regex= expresssao regular - modelo matematico
# numeros = serie.str.replace(",",".", regex=False)
# numeros = pd.to_numeric(numeros, errors="coerce")
# print(numeros)
# print(df.head(2))# um print da tabela
# print(df.shape)# diz o numero de linhas e colunas
# print(df.info())# info de estrutura, tipo, memoria, null e etc
# print(df.describe)
# print(df["cidade"].value_counts())#conta a quantidade de valores
# print(df.loc[0,"cidade"]) #localizar
# print(df.iloc[0, 2]) #localizar por indice linha,coluna
# print (df.loc[df["valor"]>100, "cliente"])
# print(df[df["valor"]> 100])
# print(df[df["cidade"].isin(["Recife", "Curitiba"])])
# print(df[df["valor"].between(60,230.5)])
# print(df[df["cliente"].str.contains("a")])
# print(df[(df["valor"] > 100) & (df["cidade"] == "Curitiba")])

# dados = {
#     "cliente": ["Maria", "João", "Ana","Bruno"],
#     "cidade": ["São Paulo" , "Recife", "Curitiba", "Recife"],
#     "valor" : [150.0, 89.90, 230.5, 60.0]

# }
# df = pd.DataFrame(dados)
# print(dados)
# 20 f
"""
nome = "Ana"
#O nome é : Ana
print("O nome é: " + nome)
print(f"O nome é: {nome}")
# 2 + 2 = 4
numero = 2
print(f"{numero} + {numero} = {numero}")
"""

#19 try/except
"""
valores = ["100","abc","250",""]

for v in valores:
    try:
        numero = int(v)
        print(f"2 * {numero} = {2 * numero}")
    except ValueError:
        print(f"{v} não é númerico")
"""
#18 dobro de valor
"""
situacao = lambda nota: "aprovado" if nota >= 70 else "reprovado"

dobro = lambda x: x * 2

def dobro(x):
    return 2 * x
"""

#17 definir funçao
"""
#def resumo vendas(valores, imposto= 0.1):
def teste(p=2):
    print(p)

teste()
teste(3)

def resumo_vendas(valores, imposto= 0.1):
    total = sum(valores)
    media = total / len(valores)
    total_com_imposto = total*(1+imposto)
    return total, media, total_com_imposto
t, m, ti = resumo_vendas([100, 200, 300])
print(f"Total: {t}, Média: {m:.2f}, Com imposto: {ti:.2f}")
"""

#16
"""
nomes = ["Maria", "João", "Ana"]
for i, nome in enumerate(nomes):
    print(i, nome)
"""

#15 verificação de caracter
'''
emails = ["ana@x.com", "joao.com", "maria@y.com", "pedro"]
#variavel contadora
invalidos = 0
for email in emails:
    if "@" not in email:
        invalidos = invalidos + 1
        print(f"Inválido: {email}")
print(f"Total de inválidos: {invalidos}")
'''

#14
#acumulador
'''
precos = [19.9, 45, 12.5]
total = 0 #acumulador
for p in precos:
    total = total + p
print(f"Total: R$ {total:.2f}")
'''

#13
#operador in
""""
uf = "MG"
validos = ["SP","RJ", "MG", "PR" , "RS"]
if uf in validos:
    print ("UF reconhecida")
else:
    print ("UF inválida")
"""

#12
#if elif else
""""
valor = 250
#se for pelo menos 500, é alto
#se for pelo menos 100 é médio
#caso contrário, é baixo
if valor >= 500:
    faixa = "alto"
elif valor >= 100:
    faixa = "média"
else:
    faixa = "baixo"
print(faixa)
"""

#11
#valores unicos usando conjuntos (sets)
"""
estados = ["SP", "RJ", "MG", "RJ", "SP"]
print(set(estados)) 
print(len(set(estados)))
"""

#10
#tabela = [  
#    {"Nome": "Maria", "saldo": 150},
#    {"Nome": "João", "saldo": 200},
#    {"Nome": "Ana", "saldo": 250}
#]
#print(tabela[2]["Nome"])

#9
#dicionario: coleção de pares chave/valor
#cliente = {
#    "nome": "Maria",
#    "idade": 34,
#    "cidade":"São Paulo"
#}
#print(cliente["cidade"])
#cliente["Email"] = "Maria@email.com"
#for chave, valor in cliente.items():
#    print(chave, "->", valor)

#8
#lista comprehensions (compreensao de lista)
#precos = [19.90, 45.00, 12.50, 89.90]
#aplicar 10% a todos
#com_imposto= [p*1.1 for p in precos]
#print(com_imposto)
#caros = [p for p in precos if p > 40]
#print(caros)

#7
#listas
#precos = [19.90, 45.00, 12.50, 89.90]
#quantos
#print(len(precos))
#soma
#print(sum(precos))
#maior valor
#print(max(precos))
#menor valor
#print(min(precos))
#adicionar um valor
#precos.append(30.00) #concatenar
#apenas os dois primeiros
#print(precos[:2])


#6
#valor_txt = "R$ 1.234,56"
#limpo = valor_txt.replace("R$","").replace(".", "").replace(",",".").strip()
#valor = float(limpo)
#print(valor + 10)

#5
#nome = " maria  SIlva  "
#limpo = nome.strip().title()#strip tira os espaços e o title deixa a primeira palavra em maiuscula
#print(limpo)
#print(limpo.split())
#print(" ".join(limpo.split()))

#4
#indice e fatiamento
#cpf = '12345678900'
#print (cpf[0])
#print (cpf[10])
#print(cpf[0:3])
#print(cpf[-3])
#print(cpf[-11])
#print(cpf[-3:])
#print(cpf[-3:-1])

#3
#f- string
#nome = "Maria"
#valor = 1234.50
#Maria gastou R$1234.50
#print(f'{nome} gastou R${valor:.2f}')

#2
#preco_textual = "19.90"
#preco = float(preco_textual)
#idade_textual = "18"
#idade = int(idade_textual)
#print(type("Maria"))

#1
#nome = "Maria"
#sobrenome = 'Silva'  
#idade = 34
#ativo = True
#altura = '180'
#print(nome, sobrenome, idade, ativo, altura)
#print(10/0)
#print("Olá, mundo dos dados!")