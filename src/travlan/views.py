from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from . import models
from django.utils.text import slugify

# Create your views here.

def get_star(post):
    comments = models.Comment.objects.filter(post_num=post.post_num)
    star = 0
    for comment in comments:
        star += comment.score
    return star/(len(comments) + 1)

def insert_post(post):
    return {
        'num': post.post_num,
        'title': post.title,
        'date': post.created_date,
        'image': post.thumbnail,
        'star': get_star(post)
    }

def best_region(request):
    age = request.GET.get('age', '')
    posts = models.Post.objects.filter()
    data = {
        'result': []
    }
    
    result = {}
    if age:
        for post in posts:
            if hasattr(post.member_num, 'memberinfo'):
                if post.member_num.memberinfo.age == age:
                    if not post.region_num.region in result:
                        result[post.region_num.region] = 1
                    else:
                        result[post.region_num.region] += 1

    else:
        for post in posts:
            if not post.region_num.region in result:
                result[post.region_num.region] = 1
            else:
                result[post.region_num.region] += 1
    data['result'] = sorted(result.items(), key=lambda instance:instance[1], reverse=True)[:3]
    return JsonResponse(data, json_dumps_params = {'ensure_ascii': True})


def recommend_season(request):
    if not request.GET.get('value', ''):
        raise Http404()
    
def recommend_by_type(request):
    if not request.GET.get('value', ''):
        raise Http404()
    value = request.GET.get('value', '')
    posts = models.Post.objects.filter(type=value)

    data = {
        'posts': list()
    }

    for post in posts:
        data['posts'].append(insert_post(post))
    data['posts'] = sorted(data['posts'], key=lambda instance:instance['star'], reverse=True)[:3]
    return JsonResponse(data, json_dumps_params = {'ensure_ascii': True})

def recommend_by_type_one(request, number):
    if not request.GET.get('value', ''):
        raise Http404()
    value = request.GET.get('value', '')
    posts = models.Post.objects.filter()

    data = {
        'posts': list()
    }

    for post in posts:
        if post.type[number-1] == value:
            data['posts'].append(insert_post(post))
    data['posts'] = sorted(data['posts'], key=lambda instance:instance['star'], reverse=True)[:3]
    return JsonResponse(data, json_dumps_params = {'ensure_ascii': True})

def recommend_by_age(request):
    if not request.GET.get('value', ''):
        raise Http404()
    value = request.GET.get('value', '')
    posts = models.Post.objects.filter()
    
    data = {
        'posts': []
    }

    for post in posts:
        if hasattr(post.member_num, 'memberinfo'):
            if post.member_num.memberinfo.age == value:
                data['posts'].append(insert_post(post))
    data['posts'] = sorted(data['posts'], key=lambda instance:instance['star'], reverse=True)[:3]
    return JsonResponse(data, json_dumps_params = {'ensure_ascii': True})