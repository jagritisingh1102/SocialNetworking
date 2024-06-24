from django.urls import path
from .views import UserCreate, UserList, UserLogin, UserSearch, SendFriendRequest, AcceptFriendRequest, RejectFriendRequest, FriendList, PendingRequestsList

urlpatterns = [
    path('signup/', UserCreate.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('users/', UserList.as_view(), name='user-list'),
    path('search/', UserSearch.as_view(), name='user-search'),
    path('send-request/', SendFriendRequest.as_view(), name='send-request'),
    path('accept-request/', AcceptFriendRequest.as_view(), name='accept-request'),
    path('reject-request/', RejectFriendRequest.as_view(), name='reject-request'),
    path('friends/', FriendList.as_view(), name='friends-list'),
    path('pending-requests/', PendingRequestsList.as_view(), name='pending-requests'),
]

