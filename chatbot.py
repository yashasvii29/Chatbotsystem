from tkinter import *
root = Tk()
root.title("CHATBOT MUSIC RECOMMENDATION SYSTEM")
def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi")
    elif(user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(e.get() == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
    elif(user=='a'or user=='aankhein'or user=='aao'or user=='aasman'):
        txt.insert(END,"\n"+"Bot ->Ankhon Ankhon Men\nApril Fool Banaya \nAashiq Banaya Aapne\nAise Na Dekho\nAjab Leher Hai MeriApun Bola\nAa dekhe jara\nAapki nazro ne samja\nAankho se batana\nae dil hai muskil\nAgar tum sath ho")
    elif(user=='b'or user=='B'or user=="Baarish" or user=="Bewafa"):
        txt.insert(END,"\n"+"Bot ->Baarish Ban jana\n Baarish\nBaari\nBaatein ye kabhi na\nBewafa hai tu\nBewajah\nBeliya\nBulleya\nBuzz\nButtabomma")
    elif(user=='c'or user=='C' or user=='Chale'):
        txt.insert(END,"\n"+"Bot ->Cheap thrills\nChand Sifarish\nChale Ana\nChanna Ve\nChogada\nChaka Chak\nChaand Baliya\nCoca cola\nCare Ni Karda\nChashni")    
    elif(user=='d'or user=='D'):
        txt.insert(END,"\n"+"Bot ->Dhoka\nDespacito\nDholida\nDilbar\nDard dilo ke\nDaru badnaam\nDarasal\nDangal\nDance meri rani\nDil meri na sune")
    elif(user=='e'or user=='E' or user=="Ek" or user=="ek"):
        txt.insert(END,"\n"+"Bot ->Ek raat\nEk tarfa\nEk mulaqat\nEk pyar ka nagma hai\nEk do teen\nEk dujhe ke vaaste\nEk dil Ek jaan\nEk din meri baho me\nEk toh kam zindagani\nEk baat batao Toh")
    elif(user=='f'or user=='F'or user=='fa'):
        txt.insert(END,"\n"+"Bot ->Falling fo you\nFalak tak\nFilhaal\nFanna\nFirst class\nFakira\nFaraar\nFaasle\nFaaslo me\nFevicol se")
    elif(user=='g'or user=='G'):
        txt.insert(END,"\n"+"Bot ->Gal ban gayi\nGalti se mistake\nGallan kardi\nGajab ka hai din\nGal karke\nGalliyan\nGenda phool\nGulabi aankhein\nGali gali\nGarmi")
    elif(user=='h'or user=='H'):
        txt.insert(END,"\n"+"Bot ->Humsafar\nHaan tum ho\nHalka Halka\nHamari adhuri kahani\nHasi\nHaule Haule\nHawayein\nHumdard\nHawa banke\nHum nava mere")
    elif(user=='i'or user=='I'):
        txt.insert(END,"\n"+"Bot ->Ijazat\nIshq wala love\nI am rider\nIk tu hai\nIktara\nIs qadar\nIk vaari\nIk mulaqat\nIshare tere\nIk tera")
    elif(user=='j'or user=='J'):
        txt.insert(END,"\n"+"Bot ->Jaana ve\nJab we met\nJawani\nJab koi baat\nJashne bahara\nJanam Janam\nJaan ban gaye\nJalebi baby\nJaan nisaar\nJab tak")
    elif(user=='k'or user=='K'):
        txt.insert(END,"\n"+"Bot ->Kaun tujhe\nKaise hua\nKahani\nKabira\nKesariya\nkalank\nKabhi tumhe\nKacha badam\nKusu Kusu\nKhairiyat")
    elif(user=='l'or user=='L'):
        txt.insert(END,"\n"+"Bot ->Lehanga\nLut gaye\nLove dose\nLeja re\nLiwass\nLa La La\nLamborgini\nLat lag gyi\nlet me dance slowly\nLove nwantiti")
    elif(user=='m'or user=='M'):
        txt.insert(END,"\n"+"Bot ->Maa\nManjha\nMoonlight\nMakhna\nMast magan\nMera dil bhi kitna pagal hai\nMann Bharaya\nMere humsafar\nMehbooba\nMeri zindagi hai tu")
    elif(user=='n'or user=='N'):
        txt.insert(END,"\n"+"Bot ->Nakhre\nNajaa\nNazm Nazm\nNachne de saare\nNashe se chad gyi\nNaino ki do baat\nNaina re\nNaina\nNamo namo\nNaach meri Rani")
    elif(user=='o'or user=='O'or user=='Oh'):
        txt.insert(END,"\n"+"Bot ->On my way\nOodhni\nOh sanam\nOh humsafar\nO mere dil ke chain\nO palan hare\nO saki saki\nO khuda\nO saathi\nO re piya")
    elif(user=='p'or user=='P'or user=='Phir'):
        txt.insert(END,"\n"+"Bot ->Pehli nazar mein\npehli dafa\nPhir se\nPhir kabhi\nPhoto\nPhir mulaqat\nPani da rang\nParam sundari\nPal\nPaani Paani")
    elif(user=='q'or user=='Q'or user=='Qa'):
        txt.insert(END,"\n"+"Bot ->Qubool Kijiye\nQurbaan sanam\nQyamat hai\nQabaali\nQubool A\nQatra\nQurban\nQyaamat\nQismat\nQaafirana")
    elif(user=='r'or user=='R'or user=='Raa'):
        txt.insert(END,"\n"+"Bot ->Rozana\nRaat bhar\nRabba mehar kari\nRadhe radhe\nRafta rafta\nRang lageya\nRabba\nRaanjhana\nRaata lambiyaan\nRaabta")
    elif(user=='s'or user=='S'or user=='Sa'):
        txt.insert(END,"\n"+"Bot ->Salam e ishq\nSajda\nSauda khara khara\nSanam re\nsajde\nSaiyaara\nSanam teri kasam\nSayad\nSakhiyan\nSoch liya")
    elif(user=='t'or user=='T'or user=='Tera'or user=='Tu'):
        txt.insert(END,"\n"+"Bot ->Tere liye\nTum se hi\nTera fitoor\nTera ghata\nTum hi aana\nTera yaar hoon main\nTeri ore\nTum hi ho\nTu aake dekhle\nTum jo aaye")
    elif(user=='u'or user=='U'or user=='Ude'):
        txt.insert(END,"\n"+"Bot ->Urvashi\nUnke khayal aaye to\nUncha lamba kad\nUde dil befikre\nUden jab jab julfein teri\nUnse nazrein mili\nUdne do\nUdd gaya\nUff teri ada\nUska hi bana")
    elif(user == "v" or user=="V"):
        txt.insert(END, "\n" + "Bot -> ")
    elif(user == "w" or user == "W"):
        txt.insert(
            END, "\n" + "Bot -> Waah! Tera Kya Kehna\nWaaris\nWafa\nWafaa\nWafadaar\nWah Taj\nWahan\nWahan Ke Log ")
    elif(user == "x" or user == "X"):
        txt.insert(END, "\n" + "Bot -> X Ray\nX-Men: Apocalypse\nX")
    elif(user == "y" or user == "Y"):
        txt.insert(
            END, "\n" + "Bot -> Yeh Mera India\nYaad\nYaad Rakhegi Duniya\nYaadein\nYaadgaar")
    elif(user == "z" or user == "Z"):
        txt.insert(END, "\n" + "Bot -> Zaar\nZack\nZamboni\nZanzibar\nZaragon")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")
        e.delete(0, END)
    txt = Text(root)
    txt.insert(END, "\n" + 'Hi! Welcome to the music world\nHow may I help you?')
    txt.grid(row=0, column=0, columnspan=2)
    e = Entry(root, width=100)
    e.grid(row=1, column=0) 
    send = Button(root, text="Send", command=send).grid(row=1, column=1)
    root.mainloop()