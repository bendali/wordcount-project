# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html',{'hithere': 'I am me'})
def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    textlist = fulltext.split()
    worddictionary = {}
    
    for word in textlist:
        if word in worddictionary:
           worddictionary[word]+=1
        else:
           worddictionary[word]=1
    sortedwords = sorted(worddictionary.items(),key= operator.itemgetter(1), reverse=True )         
    return render(request,'count.html',{'text':fulltext,'word':len(textlist),'sortedwords':sortedwords })