import pandas as pd
import matplotlib.pyplot as plt


dados = {
    "pedidos" : [1,2,3,4,5],
    "valor" : ["100,00", "250,50", "250,50", "abc", "80,00"]    
}

df = pd.DataFrame(dados)
print(df["valor"].dtype)
df = df.drop_duplicates(subset="pedidos")
df["valor"] = df["valor"].str.replace(",",".",regex=False)
df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
df = df.dropna(subset=["valor"])
print(f"Pedidos validos: {len(df)}")
print(f"Ticket Médio: R${df['valor'].mean():.2f}")


df = pd.read_csv("ap01_intro_python/clientes.csv")

total_cidade = df.groupby("cidade")["valor"].sum()
print(total_cidade)
total_cidade.sort_values().plot(kind="barh")
plt.title("Total vendido por cidade")
plt.xlabel("Valor(R$)")
plt.show()
