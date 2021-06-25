from django.shortcuts import render

Drawings = [
    {
        'creator':'Tahmeem',
        'title': 'First Drawing',
        'Price': 50,
        'description': 'First art to be hosted on the site. A random image from google image.',
        'image': '/Art/Assets/ArtShowcase/Art1.jpg',
    },
    {
        'creator':'Bob Ross',
        'title': 'Link',
        'Price': 50,
        'description': 'The protagonist from the Legend of Zelda game series.',
        'image': '/Art/Assets/ArtShowcase/Art1.jpg',
    }
]

def home(request):
    context = {
        'Drawings': Drawings
    }
    return render(request, 'Art/home.html', context)

def Profile(request):
    return render(request, 'Art/profile.html')