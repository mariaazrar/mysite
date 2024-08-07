from django.shortcuts import render
# from django.template import loader
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # questions = " , ".join([q.question_text for q in latest_question_list])
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404(f"Question associated with Id:{question_id} does not exist")
    
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = f"You are looking at the results of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You are voting on question {question_id}")