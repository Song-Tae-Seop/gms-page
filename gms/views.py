from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    page=request.GET.get('page', '1')

    question_list=Question.objects.order_by('-create_date') #모델 데이터를 작성 날짜의 역순으로 조회

    paginator=Paginator(question_list, 10)
    page_obj=paginator.get_page(page)

    context={'question_list': page_obj} #context는 view에서 사용하던 파이썬 변수를 html 템플릿으로 넘겨준다.
            #파이썬 변수     #템플릿에서 사용할 이름

    return render(request, 'gms/question_list.html', context)

def detail(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    context={'question': question}

    return render(request, 'gms/question_detail.html', context)

def answer_create(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    if request.method=='POST':
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer=form.save(commit=False)
            answer.create_date=timezone.now()
            answer.question=question
            answer.save()
            return redirect('gms/detail', question_id=question_id)
    else:
        form=AnswerForm()
    context={'question': question, 'form': form}
    return render(request, 'gms/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('gms:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'gms/question_form.html', context)