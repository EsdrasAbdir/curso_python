import os
import re

def renomear_arquivos():
    # Lista todos os arquivos da pasta atual
    arquivos = os.listdir('.')
    
    for nome_antigo in arquivos:
        # Busca por um padrão de números no nome do arquivo (ex: 99 ou 100)
        busca = re.search(r'(\d+)', nome_antigo)
        
        if busca:
            # Extrai o número encontrado
            numero_str = busca.group(1)
            # Transforma em 3 dígitos (ex: '99' -> '099')
            numero_formatado = numero_str.zfill(3)
            
            # Cria o novo nome substituindo o número antigo pelo formatado
            # Mantém o restante do nome (como 'aula' e '.py')
            novo_nome = nome_antigo.replace(numero_str, numero_formatado)
            
            # Só renomeia se o nome realmente mudou
            if nome_antigo != novo_nome:
                print(f"Renomeando: {nome_antigo} -> {novo_nome}")
                os.rename(nome_antigo, novo_nome)

if __name__ == "__main__":
    renomear_arquivos()
    print("Concluído! Agora a ordem alfabética será igual à numérica.")