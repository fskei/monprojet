from django.shortcuts import render, redirect

def home(request):
    # tu peux ici par exemple rediriger vers login si tu veux
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html')
