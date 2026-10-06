import pandas as pd

dados = {
    "cliente": ["Joao", "Maria", "Carlos","Mario"],
    "cidade": ["São Paulo", "Minas Gerais", "Ribeirão Preto","São Paulo"],
    "valor": [150.0, 234.56, 224.67, 120]
}

df = pd.DataFrame(dados)

print(df.head(1))
print(df.shape)
print(df[df["valor"].between(120,230)])
print(df.groupby("cidade")["valor"].sum())
df["com_frente"]=df["valor"]+15
print(df.head(2))


