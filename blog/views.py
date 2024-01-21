from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')
    return render(
        request,
        'blog/index.html'
        )