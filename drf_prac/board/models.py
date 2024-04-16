from django.db import models
from users.models import User
from django.core.cache import cache

class Post(models.Model):
    # 1. 게시글의 id 값
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    # 2. 제목
    title = models.CharField(max_length=100, db_index=True)
    # 3. 작성일
    created_date = models.DateTimeField(auto_now_add=True)
    # 4. 작성자
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # 5. 본문
    body = models.TextField()
    # 6. 조회수
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        cache.delete('posts')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.delete('posts')
        super().delete(*args, **kwargs)