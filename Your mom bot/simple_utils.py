def flip(list_val, idx_1, idx_2):
    idx_1 = idx_1-1
    idx_2 = idx_2-1
    print ("Text: "+str(list_val))
    print ("Word 1: "+str(idx_1))
    print ("Word 2: "+str(idx_2))
    val_1 = list_val[idx_1]
    val_2 = list_val[idx_2]
    list_val[idx_2] = val_1
    list_val[idx_1] = val_2
    return list_val
def merge(words):
    text = ""
    for i in words:
        text = text + i + " "
    return text
def isolate(text, start_char, end_char):
     start_index = text.index(start_char)
     end_index = text.find(end_char, start_index+1)
     print (start_index)
     print (end_index)
     if end_index == -1:
         isotext = text[start_index+1:]
     else:
         isotext = text[start_index+1:end_index]
     print(isotext)
     return isotext
def find(str, character):
    return [i for i, ltr in enumerate(str) if ltr == character]
#def range(val, start, end):
    