#desenvolver um programa que leia uma string e diga quais vogais estão presentes.
palavras = ('Aprender', 'Jogar', 'Desenvolver', 'Comprar', 'Morrer')
for p in palavras:
    print(f'\n Na Palavra {p} temos: ', end= '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')