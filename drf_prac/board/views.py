from django.http import JsonResponse
from django.utils import timezone
from requests import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from django.core.cache import cache
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework.permissions import AllowAny

class PostPagination(LimitOffsetPagination):
    default_limit = 100000
    ordering = 'created_date'

# Post의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    
    filter_backends = [filters.SearchFilter] # 👈 filters에 SearchFilter 지정
    search_fields = ['id', 'title'] # 👈 search가 적용될 fields 지정
    
    def list(self, request, *args, **kwargs):
        # 캐시 키 생성
        cache_key = 'posts_cache_key'

        # 캐시에서 데이터 조회
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            # 캐시에 데이터가 존재하는 경우 캐시 데이터 반환
            return JsonResponse(cached_data, safe=False)

        else:
            # 페이징된 쿼리셋 생성
            queryset = self.filter_queryset(self.get_queryset())
            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(queryset, request)
            
            # Serializer에 페이징된 쿼리셋을 전달하여 데이터 직렬화
            serializer = self.get_serializer(result_page, many=True)

            # 캐시에 데이터 저장 (유효 기간 설정 가능)
            cache.set(cache_key, serializer.data, timeout=3600)  # 예: 1시간 동안 캐시 유지

            # 페이징된 응답 반환
            return paginator.get_paginated_response(serializer.data)
        
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