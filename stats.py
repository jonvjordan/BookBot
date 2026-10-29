def count_words(text):
    return len(text.split())

def count_characters(text):
    counts= {}
    for ch in text:
        ch = ch.lower()
        if ch in counts:
            counts[ch] +=1
        else:
            counts[ch] = 1
    return counts

def sort_on(pair: tuple[str, int]) -> int:
    return pair[1]

def chars_dict_to_sorted_list(counts):
    lista = []
    for ch in counts:
        lista.append((ch, counts[ch]))
    sorted_list = sorted(lista, reverse=True, key=sort_on)
    return sorted_list
