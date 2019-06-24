from django.shortcuts import render, get_object_or_404
from .models import Member, Term, Port
# Create your views here.

# 첫 화면
def index(request):
    return render(request, 'index.html')

# 현재까지 멋쟁이 사자처럼의 회원
def members(request):
    members = Member.objects.all()
    terms = Term.objects.all()
    return render(request, 'members.html', {'terms':terms, 'members':members})
  
# 현재까지 멋쟁이 사자처럼의 운영진
def tutors(request):
    members = Member.objects.all()
    terms = Term.objects.all()
    return render(request, 'tutors.html', {'terms':terms, 'members':members})

# 현재까지 멋쟁이 사자처럼의 해커톤 출전 내용
def portfolios(request):
    ports = Port.objects.all()
    return render(request, 'portfolios.html', {'ports':ports, 'members':members})