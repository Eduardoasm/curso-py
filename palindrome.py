def delete_blanks(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reversed(text):
    new_text = ""
    for char in text:
        new_text = char + new_text
    return new_text


def es_palindromo(texto):
    texto = delete_blanks(texto)
    new_texto = reversed(texto)
    return new_texto.lower() == texto.lower()


print(es_palindromo("Amo la paloma"))
