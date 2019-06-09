#Built-Ins on string

name="Fionna Flynn"
#name.upper()
#print(name) #Strings are immutable
#whenever we perform any manipulation operation on string a new string in memory
newName=name
newName.upper()
print(newName)

anotherName="john wattson"
anotherName= anotherName.capitalize()
print(anotherName)

names="John,Jennie,Jim,Jack,Joe"
#idx=names.index("h")
idx=names.index("Jennie")
print(idx)

newNames=names.replace('J','K')
print(names)
print(newNames)

num=names.count("John",0,len(names))
print(num)
print()
data=names.split(",")
print(data,type(data))

for n in data:
    print(n.strip())

quotes="Search The the candles rather than darkness"
data=quotes.strip(" ")
print(data,len(data))

salutation="Mr."
fname="George"
name=salutation+fname
print(name)

number="100"
print(type(number))
if number.isdigit():
    n=int(num)
    print("n is:",type(n))
songName="Hello.mp3"
if songName.endswith(".mp3"):
    print("play the autio")
#explore more string built ins by using . as intellisense