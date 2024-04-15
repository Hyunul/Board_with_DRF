from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.nickname')
    created_date = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'created_date', 'user', 'body']

    def get_created_date(self, obj):
        return obj.created_date.strftime("%Y-%m-%d %H:%M:%S")  # 원하는 형식으로 변경