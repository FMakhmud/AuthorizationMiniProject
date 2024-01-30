from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Prize


# Create your views here.


# def index(requests):
#     members = Member.objects.all()
#     ismlar = ""
#     for member in members:
#         ismlar += f"{member.firs_name} <br>"
#
#     return HttpResponse(ismlar)


def register_pages(request):
    if request.method == "POST":
        firs_name = request.POST.get('firs_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        bio = request.POST.get('bio')
        Member.objects.create(
            firs_name=firs_name,
            last_name=last_name,
            age=age,
            bio=bio
        )
    return render(request, template_name="index.html")

# def register_pages(request):
#     if request.method == "POST":
#         print(request.POST)
#         money = request.POST.get('money')
#         members_count = request.POST.get('members_count')
#         min_age = request.POST.get('min_age')
#         Prize.objects.create(
#             money=money,
#             members_count=members_count,
#             min_age=min_age
#
#         )
#     return render(request, template_name="index1.html")
