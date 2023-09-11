from django.shortcuts import render

# Create your views here.

finches = [
  {'name': 'goldfinch', 'breed': 'european', 'description': 'fat little brown one', 'age': 3},
  {'name': 'finch', 'breed': 'american', 'description': 'fat little yellow one', 'age': 2},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
