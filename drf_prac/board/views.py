from django.utils import timezone
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from django.core.cache import cache
from rest_framework.pagination import LimitOffsetPagination

class PostPagination(LimitOffsetPagination):
    default_limit = 100
    ordering = 'created_date'

# Post의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
   
   	# serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        cache_key = f"post_{instance.id}_views"
        last_update_key = f"last_update_{instance.id}_time"
        last_update_time = cache.get(last_update_key)

        # 조회수 증가 및 캐시에 저장
        current_views = cache.get(cache_key, 0)
        cache.set(cache_key, current_views + 1)

        # 조회수를 데이터베이스에 저장
        if not last_update_time or (timezone.now() - last_update_time).seconds > 300:
            cache_key = f"post_{instance.id}_views"
            cached_views = cache.get(cache_key, 0)
            instance.views += cached_views
            instance.save()

            # 데이터베이스에 instance.views를 저장한 후에 캐시된 조회수를 0으로 초기화
            cache.set(cache_key, 0)

            # 마지막 업데이트 시간을 캐시에 저장
            cache.set(last_update_key, timezone.now())

        return super().retrieve(request, *args, **kwargs)
    
    # 초기화
    def update(self, request, *args, **kwargs):
        print("views reset")
        instance = self.get_object()

        instance.views = 0
        instance.save()

        return super().update(request, *args, **kwargs)