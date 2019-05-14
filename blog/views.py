from django.shortcuts import render, get_object_or_404
from blog.models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Create your views here.

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return  HttpResponse(output)
    #render(request, 'blog/index.html')
    def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return  render(request, 'blog/index.html',context)
"""
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #retrun the last five publish questions.
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/form_detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'
def year_article(request,year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year':year, 'artical_list':a_list}
    return render(request, 'blog/year_archive.html', context)

"""
==========================
test urls
==========================
def detail(request, question_id):
    return HttpResponse("Your are looking at question %s"%question_id)
    

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'blog/detail.html',{'question': question})
    
    def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'blog/detail.html',{'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'blog/form_detail.html',{'question': question})


def results(request, question_id):
    return  HttpResponse("You are looking  at result %s"%question_id)

def results(request, question_id):
    return  HttpResponse("You are looking  at result %s"%question_id)


def vote(request, question_id):
    return  HttpResponse("You are voting on question %s"%question_id)
"""
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay  the question voting form.
        return render(
            request,
            'blog/form_detail.html',
            {
                'question':question,
                'error_message': "You didn't select a choice.",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing
        #with POST data, This prevents data from being posted twice if
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))


