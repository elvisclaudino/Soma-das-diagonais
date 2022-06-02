def diferenca(diagonalUm, diagonalDois): #função da diferença entre as diagonais
    for l in matriz:
        for c in matriz:
            diagonalUm = matriz[0][0] + matriz[1][1] + matriz[2][2] #soma da primeira diagonal

    for l in matriz:
        for c in matriz:
            diagonalDois = matriz[0][2] + matriz[1][1] + matriz[2][0] #soma da segunda diagonal

    print(f'A soma da diagonal da esquerda para a direita é: {diagonalUm}')
    print(f'A soma da diagonal da direita pra esquerda é: {diagonalDois}')

    total = diagonalUm - diagonalDois #diferença entre as duas diagonais
    print(f'A diferença entre as duas diagonais é: {total}')

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
somaUm = 0
somaDois = 0

for l in matriz:
    print(l)

diferenca(somaUm, somaDois)