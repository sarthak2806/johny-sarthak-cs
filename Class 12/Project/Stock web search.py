import re
import urllib.request
arrayofStocks = ["FB", "GOOG", "DATA", "BABA"]
stock = input("Enter your stock: ")
url = "https://www.google.com/search?q=nse%3A"+stock+"&rlz=1C1GIWA_enIN739IN739&oq=nse%3A"+stock+"&aqs=chrome..69i57j69i58j69i59.6527j1j4&sourceid=chrome&ie=UTF-8"
data= urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('meta itemprop="price"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]
m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]
m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
print("The value of " + stock.upper() + " is " + final)