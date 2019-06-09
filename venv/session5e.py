quote="work hard be luckier"
#data=list(quote)
#data=tuple(quote)
#data=set(quote)
#data=dict(quote) ->Try to explore this
print(quote*2)
print(quote[::-1])

for i in range(0,len(quote)):
    print(quote[i],end=" ")
for i in range(len(quote)-1,-1,-1):
    print(quote[i],end=" ")