qtd_al = int(input('Informe a quantide de alunos da turma: '))
i = 1
for i in range (1, qtd_al + 1):
    pr_a = float(input('Informe a nota da prova a: '))
    pr_b = float(input('Informe a nota da prova b: '))
    pr_c = float(input('Informe a nota da prova c: '))
    result = (pr_a + pr_b + pr_c) / 3
    if result >= 6:
        print(f'Parabéns! O aluno {i} foi aprovado com nota média de {result:.2f}')
    else:
        print(f'Tristeza! O aluno {i} foi reprovado com nota média de {result:.2f}')