from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ContentSerializer
from .models import Content
from django.shortcuts import get_object_or_404
from .permissions import IsCourseStudentPermission
from courses.permissions import SuperUserPermission
from courses.models import Course


class ContentView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [SuperUserPermission]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer) -> Content:
        get_object_or_404(Course, id=self.kwargs["course_id"])
        return serializer.save(course_id=self.kwargs["course_id"])


class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCourseStudentPermission]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    lookup_url_kwarg = "content_id"
    http_method_names = ["get", "patch", "delete"]

    def perform_update(self, serializer) -> Content:
        get_object_or_404(Content, id=self.kwargs["content_id"])
        return serializer.save(id=self.kwargs["content_id"])
