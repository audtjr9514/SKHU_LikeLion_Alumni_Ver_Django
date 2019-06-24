from django.shortcuts import render, get_object_or_404
from .models import Member, Term, Port
# Create your views here.

# 첫 화면
def index(request):    
    terms = Term.objects.all()
    return render(request, 'index.html',{'terms':terms})

# 현재까지 멋쟁이 사자처럼의 회원
def members(request):
    # members = Member.objects.all()
    # terms = Term.objects.all()
    members = list()
    terms = Term.objects.all()
    # for termm in terms:
    #     if Member.objects.filter(enter_term=termm.term).count() > 0 :
    #         members.append(Member.objects.filter(enter_term=termm.term))
    members.append(Member.objects.filter(enter_term=4))
    members.append(Member.objects.filter(enter_term=5))
    members.append(Member.objects.filter(enter_term=6))
    return render(request, 'members.html', {'terms':terms , 'memberss':members})
  
# 현재까지 멋쟁이 사자처럼의 운영진
def tutors(request):
    return render(request, 'tutors.html')

# 현재까지 멋쟁이 사자처럼의 해커톤 출전 내용
def portfolios(request):
    return render(request, 'portfolios.html')
