from django.http import Http404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.file.models import File, FileSerializer
from common.permissions import IsOwnerOrReadOnly


# Create your views here.


class FileListCreateAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    """
    List all article files or create a new article file.
    """
    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)

# 返回文件的url
    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            obj = {
                **serializer.data,
                'path': serializer.instance.file.url
            }
            return Response(obj, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDetailAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def get_object(self, pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist as e:
            raise Http404

    def get(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        file = self.get_object(pk)
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        file = self.get_object(pk)
        file.delete()
        return Response({'msg': '删除成功！'}, status=status.HTTP_200_OK)