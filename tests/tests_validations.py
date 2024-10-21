from src.modules.utils import verificarPalindromo

# Realizando testes na função verificarPalindromo
def tests_validate_palindromo_passed():
    assert verificarPalindromo("aaaa") == "É Palindromo!"
    assert verificarPalindromo("abababa") == "É Palindromo!"
    assert verificarPalindromo("aaaaa      ") == "É Palindromo!"
    assert verificarPalindromo("      aaaaa") == "É Palindromo!"
    assert verificarPalindromo("     aaaaa      ") == "É Palindromo!"
    
def tests_validate_palindromo_fails():
    assert verificarPalindromo("1aa") == "É aceito apenas palavras!"
    assert verificarPalindromo("") == "O valor não pode ser vazio!"
    assert verificarPalindromo("      ") == "O valor não pode ser vazio!"
    assert verificarPalindromo("4n4") == "É aceito apenas palavras!"
    assert verificarPalindromo("!a!") == "É aceito apenas palavras!"
    