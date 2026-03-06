# p074-suma-mutiplos.py
# Imprime multipltiplos m entre 1 y n

while(True):
    print('\033[H\033[J')

    print('Imprime mutiplos de m entre 1 y n')
    n = int(input('Hasta donde ? '))
    m = int(input('Que multiplos quieres ? '))
    cm = sm = 0

    for i in range(1, n+1):
        if i % m == 0:
            print(i, end=' ')
            sm += i
            cm += 1

    print(f'\nFueron {cm} multiplos, los cuales suman {sm}')

    if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break

print('\nHemos llegado al final ....')
