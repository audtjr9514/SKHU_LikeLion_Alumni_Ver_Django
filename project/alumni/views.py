from django.shortcuts import render
# from .models import Member, Quarter, Port
# Create your views here.

# 첫 화면
def index(request):
    return render(request, 'index.html')

# 현재까지 멋쟁이 사자처럼의 회원
def members(request):
    return render(request, 'members.html')

# 현재까지 멋쟁이 사자처럼의 운영진
def tutors(request):
    return render(request, 'tutors.html')

# 현재까지 멋쟁이 사자처럼의 해커톤 출전 내용
def portfolios(request):
    return render(request, 'portfolios.html')
