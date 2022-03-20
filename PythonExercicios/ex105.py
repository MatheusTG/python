def notas(*n, sit=False):
    """
    ==> Função para analizar notas de alunos!
    :param n: Digite nota de quantos alunos quiser.
    :param sit: Se sit=True você ira abilitar a função de
           situação! (mostra se o aluno foi bem, na média ou ruim)
    :return: um dicionrio com informaçãoes de cada aluno!
    """
    dicio = {'total': len(n), 'menor': min(n), 'maior': max(n), 'media': sum(n) / len(n)}
    if sit and dicio['media'] < 6:
        dicio['situação'] = 'Ruim'
    elif sit and 6 <= dicio['media'] < 7:
        dicio['situação'] = 'Razoável'
    elif sit:
        dicio['situação'] = 'Boa'
    return dicio


resp = notas(8.5, 8, 5.5, 7, 9, sit=True)
resp1 = notas(3.5, 7, 9.2, 6, sit=True)
resp2 = notas(4.6, 5, 6.1, 4, 3.5, 5, sit=True)
print(f'Turma 1 = {resp}\nTurma 2 = {resp1}\nTurma 3 = {resp2}')

help(notas)
