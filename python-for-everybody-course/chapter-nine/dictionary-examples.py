fname = input('Enter File ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for line in hand :
    line = line.strip()
    wds = line.split()
    for w in wds :
        #idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1

#print(di)

#now we want to find the most common word
largest = -1
theword = None
for key,value in di.items():
    if value > largest :
        largest = value
        theword = key #capture/remember the word that was largest

print(theword,largest)
