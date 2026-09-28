import pandas as pd
df = pd.DataFrame({
    "cliente": ["Ana", "Bruno", "Carla", "Diego", "Ana"],
    "cidade" : ["SP", "RJ", "SP", "MG", "SP"],
    "valor": [120.0, 80.0, 200.0, 50.0, 120.0],   
})

print("14 Mostre as primeiras linhas e descubra quantas linhas e colunas o DataFrame tem:")
print(df.head())
print(df.shape)
print()

print("15 Quantas vezes cada cidade aparece na coluna cidade?")
print(df["cidade"].value_counts())
print()

print("16 Filtre e mostre apenas os clientes com valor acima de 100:")
print(df.loc[df["valor"]>100,"cliente"])

print("17 Remova as linhas duplicadas e diga quantas linhas sobraram:")
df_duplicadas = df.drop_duplicates(inplace=False)
print(f"{df_duplicadas}")
print(f"O total de linhas sem duplicadas é: {len(df_duplicadas)}")

print("18  Calcule o ticket médio (média de valor) por cidade")
print(f"Ticket Médio: R${df.groupby("cidade")["valor"].mean().round(0)}")

print("19 Crie uma coluna faixa com ”alto” para valor >= 100 e ”baixo” caso contrário (use apply com lambda.")
df['Faixa'] = df['valor'].apply(lambda x: 'alto' if  x >=100  else "baixo")
print(df.head())

print("20 Mostre as 2 maiores compras (Top-2 por valor).")
print(df.sort_values('valor', ascending=False).head(2))

print("21 Junte (merge) o DataFrame de pedidos abaixo com o de clientes pela coluna id_cliente e " \
"calcule o total gasto por cliente:")

pedidos = pd.DataFrame({"id_cliente": [1, 2, 1, 3],"valor": [100, 200, 50, 80]})
clientes = pd.DataFrame({"id_cliente": [1, 2, 3],"nome": ["Ana", "Bruno", "Carla"]})


Juncao = pedidos.merge(clientes,on='id_cliente', how='inner')
print(pedidos['valor'].sum)





# pensamentos e ideias complementares
# contagem = df["cidade"].value_counts()
    
# for cidade, quantidade in contagem.items():
#     print(f"A cidade {cidade} apareceu {quantidade} vezes.")
    