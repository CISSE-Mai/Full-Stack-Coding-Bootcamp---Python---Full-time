print("...début...")
for i in range(1,21):
    print(i)

print("...Liste...")
liste = list(range(1,21))
print(liste)

print("...index...")
for i in liste:
    if liste.index(i) % 2 == 0 :
        print(liste[liste.index(i)])