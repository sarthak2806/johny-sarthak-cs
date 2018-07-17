while True:
    sen=raw_input("Enter a sentence:")
    c=0
    for x in range (len(sen)):
        if sen[x]==' ':
            c+=1
    else:
        print "Number of Words:",c+1
