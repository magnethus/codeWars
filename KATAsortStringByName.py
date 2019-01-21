#KATA Sort a string by name
def order(sentence):
    new_list = []
    lista = sentence.split()
    for x in range(1, len(lista)+1):
        for y in range(len(lista)):
            if str(x) in lista[y]:
                new_list.append(lista[y])
            else:
                pass
    sentence = ' '.join(new_list)
    return sentence