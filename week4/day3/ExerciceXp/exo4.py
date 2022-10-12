users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

resultat = [nom for nom,ordre in enumerate(users)]
disney_users_A = dict(zip(users,resultat))
print(disney_users_A)

disney_users_B = dict(zip(resultat,users))
print(disney_users_B)

disney_users_C = dict(zip(sorted(users),resultat))
print(disney_users_C)

user = []
for x in users :
    if "i" in x :
        user.append(x)
disney_users_A = dict(zip(user,resultat))
print(disney_users_A)