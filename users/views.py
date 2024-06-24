from rest_framework import generics, filters
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FriendRequestSerializer
from .models import FriendRequest
from django_ratelimit.decorators import ratelimit
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.db.models import Q

CustomUser = get_user_model()


class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = CustomUser.objects.get(Q(email__iexact=email) | Q(username__iexact=email))
            print("came here")
        except CustomUser.DoesNotExist:
            print("came in exception")
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            print(token)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = []


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserSearch(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'username']


class SendFriendRequest(APIView):
    def post(self, request, *args, **kwargs):
        from_user = request.user
        to_user_id = request.data.get('to_user_id')

        # Check if a friend request already exists
        existing_request = FriendRequest.objects.filter(
            from_user=from_user, to_user_id=to_user_id
        ).exists()

        if existing_request:
            return Response(
                data={"message": "Friend request already sent."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            to_user = CustomUser.objects.get(id=to_user_id)
            FriendRequest.objects.create(from_user=from_user, to_user=to_user)
            return Response(
                data={"message": "Friend Request Sent Successfully"},
                status=status.HTTP_201_CREATED
            )
        except CustomUser.DoesNotExist:
            return Response(
                data={"message": "Invalid user ID."},
                status=status.HTTP_400_BAD_REQUEST
            )


class AcceptFriendRequest(APIView):
    def post(self, request, *args, **kwargs):
        friend_request = FriendRequest.objects.get(id=request.data['request_id'])
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.delete()
        return Response(data={"message": "Request Accepted Successfully"}, status=status.HTTP_204_NO_CONTENT)


class RejectFriendRequest(APIView):
    def post(self, request, *args, **kwargs):
        friend_request = FriendRequest.objects.get(id=request.data['request_id'])
        friend_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FriendList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user.friends.all()


class PendingRequestsList(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return self.request.user.received_requests.all()
