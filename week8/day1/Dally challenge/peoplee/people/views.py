from operator import itemgetter

from django.shortcuts import render

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

people = sorted(people,key = lambda tri: tri['age'])


def index(request):
    context = {
        'page_title' : "people",
        'people' : people,
    }
    return render(request, 'posts/people.html', context)


def posts(request):
  context = {
    'page_title': "people",
    'people': people,
  }
  return render(request, 'posts/people_id.html', context)

# Create your views here.
