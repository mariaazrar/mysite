from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # questions = " , ".join([q.question_text for q in latest_question_list])
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You are looking at question {question_id}.")


def results(request, question_id):
    response = f"You are looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")