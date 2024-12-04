import unicodedata

# Autor: Rafael Jiménez

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas y tildes.
    """
    # Normalizar cadena para eliminar tildes y convertir a caracteres simples
    cadena_normalizada = ''.join(
        c for c in unicodedata.normalize('NFD', cadena)
        if unicodedata.category(c) != 'Mn'
    )
    # Convertir a minúsculas y eliminar caracteres no alfanuméricos
    cadena_limpia = ''.join(
        char.lower() for char in cadena_normalizada if char.isalnum()
    )
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]