from django.shortcuts import render
from WAT1_0.utilities.HAR_processor import HttpTrafficHAR
from WAT1_0.utilities.search_request_match import SerachData

# Create your views here.
from django.http import HttpResponse
import json
import pprint

def index(request):
    context = dict()
    json_data = dict()
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
        obj = SerachData()
        data = obj.get_HAR(url,term)
    #pprint.pprint(obj.searching_filter_records(data,"usb"))
    
        json_load = obj.searching_filter_records(data,term)
        dump_josn = json.dumps(json_load)
        json_data = json.loads(dump_josn)
    return render(request,"index.html",{'josn_data':json_data})

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