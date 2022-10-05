from django.shortcuts import render

animals= [
        {
            "id" :1,
            "name": "Chien",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Chat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3
        },
        {
            "id": 4,
            "name": "cameléon",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 5,
            "name": "cocinelle",
            "legs": 6,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5
        }
    ]
def index(request):
    context = {
        'page_title' : "Animal",
        'animals' : animals,
    }
    return render(request, 'posts/animal.html', context)


families= [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },
        {
            "id": 3,
            "name": "mammifère"
        },
        {
            "id": 4,
            "name": "reptile"
        },
        {
            "id": 5,
            "name": "insecte"
        },
        {
            "id": 6,
            "name": "mammifère"
        },
        {
            "id": 7,
            "name": "arachnide"
        },
        {
            "id": 8,
            "name": "amphibien"
        }
    ]
def posts(request):
    context = {
        'page_title' : "Family",
        'families' : families,
    }
    return render(request, 'posts/family.html', context)

# Create your views here.
