from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = dict()
    term = None
    if request.GET.get('URL'):
        url = request.GET.get('URL')
        radio_value = request.GET.get('inlineDefaultRadiosExample')
        if radio_value == "searchRadio":
            term = request.GET.get('term')
        radio_value1 = request.GET.get('inlineDefaultRadiosExample')
        context.update({
            'url' : url,
            'IsSearch' : radio_value,
            'ISMonitor' : radio_value1,
            'term' : term,
            'radio_value' : radio_value
        })
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