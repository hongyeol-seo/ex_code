alpa = dict()

msg = "baaa".upper()

for i in msg:
    if i in alpa :
        alpa[i] +=1
    
    else :
        alpa[i] = 1
    
res = sorted(alpa.items(), key=(lambda x: x[1]),reverse=True)

max_count = -1
max_spell = ""

for i in range(len(res)):
    if res[i][1] > max_count:
        max_count = res[i][1]
        max_spell = res[i][0]
    elif res[i][1] < max_count:
        continue
    else :
        max_count = 0    

if max_count :
    print(max_spell)
else :
    print("?")
