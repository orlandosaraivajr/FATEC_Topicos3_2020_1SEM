'''
Resolver o bug das expressões 'do', 'da', 'dos', das'
'''
def abnt(nome_autor):
    nome_autor = nome_autor.upper()
    nomes_finais = ["FILHO", "FILHA", "NETO"]
    nomes_finais = nomes_finais + ["NETA", "SOBRINHO"]
    nomes_finais = nomes_finais + ["SOBRINHA", "JUNIOR"]
    nome_lista = nome_autor.split()
    if nome_lista[-1] in nomes_finais:
        novo_nome = nome_lista[-2] 
        novo_nome = novo_nome + ' '
        novo_nome = novo_nome + nome_lista[-1] 
        novo_nome = novo_nome + ','
        nome_lista.pop()
        nome_lista.pop()
        for nome in nome_lista: 
            novo_nome = novo_nome + nome.capitalize() + ' '
        return novo_nome
    else:
        nome_lista = nome_autor.split()
        novo_nome = nome_lista[-1] 
        novo_nome = novo_nome + ','
        nome_lista.pop()
        for nome in nome_lista: 
            novo_nome = novo_nome + nome.capitalize() + ' '
        print(novo_nome)
        return novo_nome


assert abnt('orlando saraiva do Nascimento') == 'NASCIMENTO, Orlando'
assert abnt('fabio gomes suzarth junior') == 'SUZARTH JUNIOR,Fabio Gomes '
assert abnt('angelo lotienzo filho') == 'LOTIENZO FILHO,Angelo '