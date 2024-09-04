from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275746',
        'name': 'Joshua Montolalu',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)