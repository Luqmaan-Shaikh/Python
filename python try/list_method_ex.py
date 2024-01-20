num = [2,2,4,6,3,4,6,1]
uniques = []
for no in num:
    if no not in uniques:
        uniques.append(no)
print(uniques)