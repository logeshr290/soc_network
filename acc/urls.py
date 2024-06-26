from django.urls import path
from .views import home, UserSignupView, UserLoginView, UserSearchView, ListFriendsView, logout_view, SendFriendRequestView, AcceptFriendRequestView, RejectFriendRequestView

urlpatterns = [
    path('', home, name='home'),
    path('signup/', UserSignupView.as_view(), name='signup-page'),
    path('login/', UserLoginView.as_view(), name='login-page'),
    path('logout/', logout_view, name='logout'),
    path('search', UserSearchView.as_view(), name='search-users'),
    path('friends', ListFriendsView.as_view(), name='list-friends'),
    path('send-friend-request', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('accept-friend-request', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('reject-friend-request', RejectFriendRequestView.as_view(), name='reject-friend-request'),
]
