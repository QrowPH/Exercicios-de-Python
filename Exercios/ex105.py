def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos. (Aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação do aluno.
    :return: Dicionário com varias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa principal
resp = notas(5.5, 2.5, 9, 8.5)
print(resp)