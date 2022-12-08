from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet

from api.serializers import *
from tatoo.models import *


class UserViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class PinnerApi:
    queryset = Pinner.objects.all()
    serializer_class = PinnerSerializer


class PinnerAPIView(PinnerApi, RetrieveAPIView):
    pass


class PinnerUpdateAPIView(PinnerApi, RetrieveUpdateAPIView):
    pass


class PinnerDestroyAPIView(PinnerApi, RetrieveDestroyAPIView):
    pass


class BoardrApi:
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardListAPIView(BoardrApi, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]


class BoardDetailAPIView(BoardrApi, RetrieveAPIView):
    permission_classes = [IsAuthenticated]


class BoardUpdateAPIView(BoardrApi, RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]


class BoardDestroyAPIView(BoardrApi, RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]


class PinApi:
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class PinListAPIView(PinApi, ListAPIView):
    pass


class PinDetailAPIView(PinApi, RetrieveAPIView):
    pass


class PinUpdateAPIView(PinApi, RetrieveUpdateAPIView):
    pass


class PinDestroyAPIView(PinApi, RetrieveDestroyAPIView):
    pass


class ImageApi:
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageListAPIView(ImageApi, ListAPIView):
    pass


class ImageDetailAPIView(ImageApi, RetrieveAPIView):
    pass


class ImageUpdateAPIView(ImageApi, RetrieveUpdateAPIView):
    pass


class ImageDestroyAPIView(ImageApi, RetrieveDestroyAPIView):
    pass


class CommentApi:
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListAPIView(CommentApi, ListAPIView):
    pass


class CommentDetailAPIView(CommentApi, RetrieveAPIView):
    pass


class CommentUpdateAPIView(CommentApi, RetrieveUpdateAPIView):
    pass


class CommentDestroyAPIView(CommentApi, RetrieveDestroyAPIView):
    pass
