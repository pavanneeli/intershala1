from urllib.request import urlopen
import re
url='https://raw.githubusercontent.com/pytorch/pytorch/master/README.md'
f=urlopen(url)

ing=[]
ion=[]
for line in f:
    k=line.decode('utf-8')
    ing+=re.findall(r'\b(\w+ing)\b',k)
    ion+=re.findall(r'\b(\w+ion)\b',k)
ing.extend(ion)
avg = sum(map(len, ing))/len(ing)
print(avg)


