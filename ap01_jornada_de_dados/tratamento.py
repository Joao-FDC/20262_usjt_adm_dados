import pandas as pd
import config 

NOMES = {
    "Transaction ID": "id_transacao",
    "Item": "item",
    "Quantity": "quantidade",
    "Price Per Unit": "preco_unitario",
    "Total Spent": "total",
    "Payment Method": "forma_pagamento",
    "Location": "local",
    "Transaction Date": "data"   
}

CAMPOS = list(NOMES.values())

PROBLEMAS = ["", "ERROR", "UNKNOWN"]
AUSENTES = PROBLEMAS + ["Não informado", "Não identificado"]

ITENS = {
    "Coffe" : "Café",
    "Tea" : "Chá",
    "Sandwich": "Sanduíche",
    "Salad" : "Salada",
    "Cake" : "Bolo",
    "Cookie" : "Cookie",
    "Smoothie" : "Smoothie",
    "Juice" : "Suco"
}

PAGAMENTO = {
    "Cash" : "Dinheiro",
    "Credit Card" : "Cartão de crédito",
    "Digital Wallet" : "Carteira digital"
}

LOCAIS = {
    "In-Store" : "No local",
    "Takeaway" : "Para viagem"
}

Cardapio = {
    "Café" : 2.0, 
    "Chá" : 1.5,
    "Sanduíche" : 4.0,
    "Salada" : 5.0,
    "Bolo" : 3.0,
    "Cookie" : 1.0,
    "Smoothie" : 4.0,
    "Suco" :3.0
    }

PRECO_EXCLUSIVO = {
    1.0 : "Cookie",
    1.5 : "Chá",
    2.0 : "Café",
    5.0 : "Salada"
}

def diagnosticar(df):
    ruim = df[CAMPOS].isna() | df[CAMPOS].isin(AUSENTES)
    completude = (1 - ruim.mean()) * 100
    perfeitas = (~ruim.any(axis=1)).mean() * 100
    return completude, perfeitas



def mostrar_diagnostico(completude, perfeitas):
    for coluna, valor in completude.items():
        print(f"{coluna} {config.br(valor, 1)}%")
    print(f"Linhas perfeitas: {config.br(perfeitas, 1)}%")

def padronizar(bronze):
    df = bronze.rename(columns=NOMES)
    df = [CAMPOS] = DF[CAMPOS].replace(PROBLEMAS, pd.NA)
    for coluna in ["quantidade", "preco_unitario","total"]:
        df[´coluna] = pd.to_numeric(df[coluna], errors="coerce")
    df["data"] = pd.to_datetime(df["data"],format="%Y-%m-%d", errors="coerce")
    
    df["item"] = df["item"].map(ITENS)
    df["forma_pagamento"] = df["forma_pagamento"].map(PAGAMENTOS)
    df["local"] = df["local"].map(LOCAIS)
    return df
    
def tratar():
    bronze = pd.read_parquet(config.BRONZE / "vendas.parquet")
    antes, perfeitas_antes = diagnosticar(bronze.rename(columns=NOMES))
    print("Diagnóstico da camada bronze (valores utilizáveis):")
    mostrar_diagnostico(antes, perfeitas_antes)    
    
if __name__ == "__main__":
    tratar()
    
