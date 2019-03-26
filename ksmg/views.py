from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse 
from .models import Ksmg, KsmgEE
from .permissions import IsOwnerOrReadOnly
from .serializers import KsmgSerializer, KsmgEESerializer, UserSerializer
from ksmg import codes

def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'ksmg': reverse('ksmg-list', request=request, format=format)
    })

class KsmgViewSet(viewsets.ModelViewSet):
    queryset = Ksmg.objects.all()
    serializer_class = KsmgSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(KsmgViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='ksmg/index.html')
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super(KsmgViewSet, self).retrieve(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='ksmg/detail.html')
        return response

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(request_user=self.request.user)

class KsmgEEViewSet(viewsets.ModelViewSet):
    queryset = KsmgEE.objects.all()
    serializer_class = KsmgEESerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

