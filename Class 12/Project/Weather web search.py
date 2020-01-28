while 1==1:
    import re
    import urllib.request
    cityl=[i for i in input('Enter your city: ')]
    city=''
    if ' ' in cityl:
        for i in cityl:
            if i!=' ':
                city+=i
            else:
                city+='-'
    else:
        for x in cityl:
            city+=x
    url='http://www.weather-forecast.com/locations/'+city+'/forecasts/latest'
    data=urllib.request.urlopen(url).read()
    data1=data.decode('utf-8')
    m=re.search('span class="phrase">',data1)
    start=m.end()
    end=start+300
    newString=data1[start:end]
    m=re.search('</span>',newString)
    end=m.start() - 2
    final=newString[:end+2]
    print(final)
