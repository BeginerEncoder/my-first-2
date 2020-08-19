from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Advert, Comment
from django.urls import reverse
import datetime

now = datetime.datetime.now()

def board(request):
    latest_advert_list = Advert.objects.order_by('-pub_date')[:30]
    return render(request, 'CallBoard/list.html', {'latest_advert_list' : latest_advert_list})

def leave_advert(request):
    try:
        Advert.objects.create(
            advert_title = request.POST['name'],
            advert_text = request.POST['text'],
            pub_date = now
            )
    except:
        pass
    return render (request, 'CallBoard/leave.html',)


def detail(request, advert_id):
    try:
        a = Advert.objects.get(id = advert_id )
    except:
        raise Http404("Обьявление не найдено ^~^")

    latest_comments_list = a.comment_set.order_by('id')[:10]

    return render (request, 'CallBoard/detail.html', {'advert' : a, 'latest_comments_list' : latest_comments_list})

def leave_comment(request, advert_id):
    try:
        a = Advert.objects.get(id = advert_id )
    except:
        raise Http404("Обьявление не найдено ^~^")

    a.comment_set.create(author_name = request.user.username, comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('advert:detail', args = (a.id,)))






# Create your views here.
