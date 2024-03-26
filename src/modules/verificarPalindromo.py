def verificarPalindromo(palavra):
    ehpalindromo = False
    if palavra.lower()[::-1] == palavra.lower():
        ehpalindromo = True
    return ehpalindromo