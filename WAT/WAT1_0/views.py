from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = dict()
    if "submit" in request.POST:
        context.update({'post_output': request.POST.get('URL','')})
    return render(request,"index.html",context)

def test(request):
    questions=None
    name = None
    if request.GET.get('search'):
        search = request.GET.get('search')
        #questions = Queries.objects.filter(query__icontains=search)

        name = request.GET.get('name')
        #query = Queries.object.create(query=search, user_id=name)
        #query.save()

    return render(request, 'test.html',{
        'questions': name,
    })