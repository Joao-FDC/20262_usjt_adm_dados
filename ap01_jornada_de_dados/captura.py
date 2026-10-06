import shutil 
from datetime import date
import pandas as pd
import config
#copia byte a byte

def capturar():
    config.preparar_pastas()
    origem = config.ENTRADA / config.ARQUIVO
    if not origem.exists():
        raise SystemExit(f'Baixe o arquivo do kaggle e salve em: {origem}') 
        #questao de segurança, se nao tiver arquivo ou ocorrer algum erro, sai do sistema

    destino = config.RAW / f"vendas_{date.today()}.csv"
    #define o nome como vendas e produz o dado do dia de hj(atualizado)

    if destino.exists():
        print("O arquivo de hoje já foi capturado: ", destino.name)
    else:
        shutil.copy(origem, destino)
        print("Arquivo capturado: ", destino.name)     
        
    linhas = len(pd.read_csv(destino))
    tamanho = destino.stat().st_size / 1024
    print(f"{config.br(linhas)}linhas, {config.br(tamanho,1)}kiB")#conta a quantidade de linhas no padrao br "1.245,53"
    return {"resumo" :  [f"{config.br(linhas)} linhas", "somente leitura"] }
    
    
if __name__ == "__main__": #sem isso, o vsc executa o config inteiro na hora do import, só executa o config se assim for solicitado extritamente
    capturar()#executar no terminal (python captura.py)
    
    #nao tem validação