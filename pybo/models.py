from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)      #질문의 제목
    content = models.TextField()                    #질문의 내용
    create_data = models.DateTimeField()           #질문 시각
    
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)       #질문(어떤 질문의 답변인지 알기 위함)
    content = models.TextField()                                           #질문 내용
    create_date = models.DateTimeField()                                   #질문 시각
