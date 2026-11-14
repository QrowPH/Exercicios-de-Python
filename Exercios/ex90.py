aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média igual a {aluno["média"]}')
if aluno['média'] < 5.9:
    aluno['situação'] = 'REPROVADO'
else:
    aluno['situação'] = 'APROVADO'
print(f'A sitação igual a {aluno["situação"]}')