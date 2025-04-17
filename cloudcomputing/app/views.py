from django.http import HttpResponse
from rest_framework import viewsets, parsers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser]

    @action(methods=['get'], detail=False, url_path='current-user', permission_classes=[IsAuthenticated])
    def get_current_user(self, request):
        user = request.user
        user.check_expiration()
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='search')
    def search_user(self, request):
        username = request.query_params.get('username')
        if not username:
            return Response({'error': 'Không có username.'}, status=status.HTTP_400_BAD_REQUEST)

        users = User.objects.filter(username__icontains=username)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='check-valid', permission_classes=[IsAuthenticated])
    def check_valid(self, request):
        user = request.user
        user.check_expiration()
        try:
            user.check_valid()
            return Response({'message': 'Dung lượng hợp lệ'}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, url_path='upgrade-plan', permission_classes=[IsAuthenticated])
    def upgrade_plan(self, request):
        user = request.user
        user.check_expiration()
        try:
            user.upgrade_plan()
            return Response({
                'message': 'Đã nâng cấp gói thành công!',
                'maximum_capacity': user.maximum_capacity,
                'expiration_date': user.expiration_date
            }, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(methods=['get'], detail=False, url_path='user-files', permission_classes=[IsAuthenticated])
    def get_user_files(self, request):
        user = request.user
        files = File.objects.filter(owner=user)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='shared', permission_classes=[IsAuthenticated])
    def get_shared_files(self, request):
        user = request.user.id
        shared_files = File.objects.filter(fileshare__user=user)
        serializer = FileSerializer(shared_files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FileShareViewSet(viewsets.ModelViewSet):
    queryset = FileShare.objects.all()
    serializer_class = FileShareSerializer