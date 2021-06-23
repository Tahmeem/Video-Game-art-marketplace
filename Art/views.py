from django.shortcuts import render

posts = [
    {
        'creator':'Tahmeem',
        'title': 'Mario jumping',
        'image': 'something.jpeg'
    },
    {
        'creator':'Bob',
        'title': 'Luigi jumping',
        'image': 'something2.jpeg'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'Art/home.html',context)

def Profile(request):
    return render(request, 'Art/profile.html')