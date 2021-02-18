import random

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys


def reverseCodeBook(dictOfElements = {}):
    keys = []
    keys = list(dictOfElements.keys())
    items = dictOfElements.items()
    new_items = []
    for i in items:
        new_items.append(i[1])
    keys.reverse()
    zip_it = zip(keys, new_items)
    new_codebook = dict(zip_it)
    return new_codebook


if __name__ == '__main__':
    # Declaracion de Independecia de México
    text = open('independence.txt')
    words = text.read().replace(',', '').split(' ') #Ejemplo de llave pública
    print(len(words))
    indexes = random.sample(range(1000, 9999), len(words)) #Ejemplo de Llave privada
    print(len(indexes))
    codebook = {}
    for i in range(len(words)):
        codebook[indexes[i]] = words[i]
    print(codebook)
    phrase = 'La Nación Mexicana sale hoy de la opresión'.split(' ')

    cipher = []
    mod_cipher = []
    for i in phrase:
        key = getKeysByValue(codebook, i)[0]
        cipher.append(key)
        mod_cipher.append(key + (key % 10))

    #supercifreado (superencryption)
    #cipher = mod_cipher

    print(cipher)
    print(mod_cipher)

    #reversed (obsolete)
    codebook = reverseCodeBook(codebook)

    print(codebook)

    for i in cipher:
        try:
            print(codebook[i], ' ')
        except:
            print("No se puede descifrar")
            break
