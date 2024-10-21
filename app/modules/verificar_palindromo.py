def verificar_palindromo(palavra: str) -> str:
    """
    Verifica se a palavra fornecida é um palíndromo.
    
    Um palíndromo é uma palavra que pode ser lida da mesma forma de trás para frente.
    
    Params:
    palavra (str): A palavra a ser verificada.

    Return:
    str: Uma mensagem indicando se a palavra é um palíndromo ou não, 
         ou se há um erro na entrada.
    """
    
    # Converte a palavra para minúsculas e remove espaços em branco no início e no fim
    palavra = palavra.lower().strip()
    
    # Verifica se a palavra não está vazia
    if palavra:
        # Verifica se a palavra contém apenas letras
        if palavra.isalpha():
            # Compara a palavra com sua reversa para determinar se é um palíndromo
            if palavra[::-1] == palavra:
                return "É Palíndromo!"  # A palavra é um palíndromo
            else:
                return "Não é Palíndromo!"  # A palavra não é um palíndromo
        else:
            return "É aceito apenas palavras!"  # A palavra contém caracteres não alfabéticos
    else:
        return "O valor não pode ser vazio!"  # A palavra fornecida está vazia
