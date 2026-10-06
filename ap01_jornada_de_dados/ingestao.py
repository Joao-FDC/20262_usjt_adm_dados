from datetime import datetime
import pandas as pd
import config

#define o arquivo mais recente
def arquivo_mais_recente():
    arquivos = sorted(config.RAW.glob("vendas_*.csv"))
    return arquivos[-1]
    #quando procurar o ultimo/ mais novo indice, use o -1

    
def ingerir():
    arquivo = arquivo_mais_recente()
    bronze = pd. read_csv(arquivo, dtype=str)
    #onde e quando foi ingerido
    bronze["arquivo"] = arquivo.name
    bronze["_ingerido_em"] = datetime.now().strftime("%Y-%m-%d-%H:%M")#meta dados sao retratados começando com um caracter especial 
    bronze.to_parquet(config.BRONZE / "vendas.parquet", index=False)#o que era linha virou coluna
    #pyarrow >= representa os dados de um modo diferente
    #pesquisar modelo parquet
    print(f"Camada Bronze: {config.br(len(bronze))} linhas gravadas")
    return{"resumo": [f"{config.br(len(bronze))} linhas", "sem correções"]}

if __name__ == "__main__":
    ingerir()
    print(pd.read_parquet(config.BRONZE/"vendas.parquet").iloc[0])
    #até a pagina 11