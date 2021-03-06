from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    
    context = {
        "questions" : questions
    }

    return render(request, "polls/index.html",context)


def detail(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question
    }

    return render(request, "polls/detail.html", context)

def results(request, q_id):
    res = "Result for question number %s." % q_id,
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s." % q_id,
    return HttpResponse(res)















def meme(request):
    return HttpResponse("<img src='https://n1s1.hsmedia.ru/c8/9f/cb/c89fcb31dd077084bc8bbc2284586b7f/1000x600_0xac120003_16946826431608901545.jpg'>")