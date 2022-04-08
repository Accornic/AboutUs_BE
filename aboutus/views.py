from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    BlogContent,
)
from .serializers import (
    BlogContentSerializer
)

# Create your views here.
class GetBlogContent(APIView):
    def get(self,request):
        blog_id = request.GET.get('blog_id',None)
        if blog_id:
            data_fd = BlogContent.objects.get(uuid=blog_id)
            serialized_fd_list = BlogContentSerializer(data_fd).data
        else :
            data_fd = BlogContent.objects.all()
            serialized_fd_list = BlogContentSerializer(data_fd, many=True).data
        
        data = dict(record=serialized_fd_list)
        return Response(dict(status=1, data=data))