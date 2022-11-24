class Info:
    def __init__(self):
      
        print(abs(4.5))
        print(int("7"))
        print(input('Appuyer sur Entrer'))

    def __doc__(self):
        return "Le programme imprime es résultats"

info = Info()
print(info.__doc__())