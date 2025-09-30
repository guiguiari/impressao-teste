import os
import sys
import win32print
import win32api
from datetime import datetime

def enviar_impressao():
    # Conteúdo da impressão
    conteudo = f"""********
IMPRESSAO TESTE - {datetime.now().strftime('%d/%m/%Y')}
********

"""
    
    # Nome da impressora (ajuste conforme o nome exato no seu sistema)
    nome_impressora = "EPSON TM-T20X RECEIPT"
    
    try:
        # Converte o conteúdo para bytes
        dados = conteudo.encode('utf-8')
        
        # Abre a impressora
        handle = win32print.OpenPrinter(nome_impressora)
        
        # Cria um job de impressão
        job_info = win32print.StartDocPrinter(handle, 1, ("Impressao Termica", None, "RAW"))
        win32print.StartPagePrinter(handle)
        
        # Envia os dados para a impressora
        win32print.WritePrinter(handle, dados)
        
        # Finaliza a página e o job
        win32print.EndPagePrinter(handle)
        win32print.EndDocPrinter(handle)
        
        # Fecha a impressora
        win32print.ClosePrinter(handle)
        
        print("Impressão enviada com sucesso!")
        
    except Exception as e:
        print(f"Erro ao enviar impressão: {e}")

if __name__ == "__main__":
    enviar_impressao()