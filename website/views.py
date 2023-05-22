from django.shortcuts import render
import website.db as db
from bson import json_util
from bson import BSON

def index(request):
    '''
    Index
    '''
    return render(request, "main/index.html")

def documents(request):
    '''
    Documents
    '''
    
    coll = db.get_collection("documents")

    result={}

    id = 0
    for document in coll:
        id += 1
        result.update({str(id): json_util.loads(json_util.dumps(document))})

    return render(request, "documents/index.html", {'result': result})

def news(request):
    '''
    News
    '''


    return render(request, "news/index.html")
