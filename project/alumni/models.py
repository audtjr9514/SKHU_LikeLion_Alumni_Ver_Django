from django.db import models

class Term(models.Model):
    term = models.IntegerField(null=False) # 기수
    def __str__(self):
       return str(self.term)

# 회원 정보
class Member(models.Model):
    name = models.CharField(max_length=10)          # 이름
    major = models.CharField(max_length=15)         # 학과
    enter_year = models.IntegerField()              # 입학년도
    enter_term = models.ForeignKey('Term', on_delete=models.CASCADE, related_name="enter_members") 
                                                    # 활동한 기수
    tutor = models.ManyToManyField('Term', blank=True, related_name="tutors") 
                                                    # 운영진 기수
                                                    # 한 회원이 여러번의 운영진을 할 수 있고, 한 기수에 여러명이 있을 수 있다.
    image = models.CharField(max_length=30)         # 사진
    portfolio = models.ManyToManyField('Port', blank=True, related_name="port_members")
                                                    # 해커톤 프로젝트
    def __str__(self):
        return self.name


class Port(models.Model):
    title = models.CharField(max_length=30)         # 제목
    content = models.TextField()                    # 내용
    Image = models.CharField(max_length=30)         # 사진
    def __str__(self):
        return self.title

