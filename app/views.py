from django.shortcuts import render

# Create your views here.
def jinga_tags(request):
    d={'name':'Gundupalli Madhumathi','age':22,'education':'Btech'}
    return render(request,'jinga_printing_tags.html',d)

