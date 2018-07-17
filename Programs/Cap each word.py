'''while True:
    sen=raw_input("Enter a sentence:")
    c=0
    for x in range (len(sen)):
        if sen[x]==' ':
            c+=1
    else:
        print "Number of Words:",c+1'''

while True:
    sen=raw_input("Enter a sentence:")
    c=0
    sen2=""
    a=1
    x=1
    sen2+=chr(ord(sen[0])-32)
    while x<len(sen):
        if sen[x]==' ':
            sen2+=" "
            sen2+=chr(ord(sen[x+1])-32)
            x+=2
        else:
            sen2+=sen[x]
            x+=1            
    else:
        print sen2
