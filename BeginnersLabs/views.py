from django.shortcuts import render, redirect


def main(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'main.html')
