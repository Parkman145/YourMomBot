import random
import simple_utils as su
uwu_table = {108: 119, 114: 119}
def stroke(text):
    text = text.split()
    text_len = len(text)
    print("Words: "+str(text_len))
    end = random.randint(round(text_len/4), round(text_len-round(text_len/4)))
    print("End: "+str(end))
    for i in range(0, end):
        text = su.flip(text, random.randint(0, len(text)), random.randint(0, len(text)))
    for i in range(0, end):
        text.insert(random.randint(0, len(text)-1), text[random.randint(0, len(text)-1)])
        text.pop(random.randint(0, len(text)-1))
    return text
def uwu(text):
    text = text.translate(uwu_table)
    return text