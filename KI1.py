import string
import os

wordlist = []

with open("AlleDeutschenWoerter-main\\Adjektive\\Adjektive.txt", "r", encoding="utf-8") as f:
    for line in f:
        wordlist.append(line.strip().lower())
    f.close()
with open("AlleDeutschenWoerter-main\\Substantive\\substantiv_singular_alle.txt", "r", encoding="utf-8") as f:
    for line in f:
        wordlist.append(line.strip().lower())
    f.close()
with open("AlleDeutschenWoerter-main\\Verben\\Verben_regelmaesig.txt", "r", encoding="utf-8") as f:
    for line in f:
        wordlist.append(line.strip().lower())
    f.close()
with open("AlleDeutschenWoerter-main\\Verben\\Verben_unregelmaeßig_Infinitiv.txt", "r", encoding="utf-8") as f:
    for line in f:
        wordlist.append(line.strip().lower())
    f.close()
def word_probability(text):
    t = text.lower()

    only_letters = all(c in string.ascii_letters + "äöüß" for c in t)
    if not only_letters:
        return 0.0
    charstxt=list(t)
    if t in wordlist: return 100
    probability = 0.0
    prop2=0.0
    for word in wordlist:
        prop2=0.0
        charsword=list(word)
        if len(charsword)==0:
            continue
        if len(charsword)>=len(charstxt):
            for i in range(len(charstxt)):
                if charstxt[i]==charsword[i]:
                    prop2+=1
            if prop2-(len(charsword)-len(charstxt))>0:
                prop2-=len(charsword)-len(charstxt)
            prop2=prop2/len(charsword)
        if len(charsword)<=len(charstxt):
            for i in range(len(charsword)):
                if charstxt[i]==charsword[i]:
                    prop2+=1
            prop2=prop2/len(charsword)
        if prop2>probability:
            probability=prop2

    return round(probability * 100, 2)
# Demo
print(len(wordlist))
while True:
    txt = input("Gib ein Wort ein: ")
    if txt == "exit":
        break
    os.system('cls')
    if word_probability(txt.strip())>=90.0:
        print(f'"{txt}" scheint ein ECHTES deutsches Wort zu sein.')
    else:
        print(f'"{txt}" scheint KEIN ECHTES deutsches Wort zu sein.')
    