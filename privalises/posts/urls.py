from django.urls import path
#from django.conf import settings
#from django.conf.urls.static import static
from .views import AddFavourites, AddLike, AddDislike, Search, AddCommentLike, AddCommentDislike, CommentReply, ProfileView, get_profile_view_by_username, settings, AddFollower, RemoveFollower,PostListView, PostDetailView, PostUpdateView, PostDeleteView, CommentDeleteView
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('profile/settings', settings, name='profile-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/remove/follower/<int:pk>', RemoveFollower.as_view(), name='remove-follower'),
    path('profile/add/follower/', AddFollower, name='add-follower'),
    path('post/add/like/', AddLike, name='add-like'),
    path('post/remove/comment/like/<int:post_pk>/<int:pk>', AddCommentLike.as_view(), name='add-comment-like'),
    path('post/add/comment/like/<int:post_pk>/<int:pk>', AddCommentDislike.as_view(), name='add-comment-dislike'),
    path('post/add/comment/reply/<int:post_pk>/<int:pk>', CommentReply.as_view(), name='add-comment-reply'),
    path('post/remove/like/', AddDislike, name='add-dislike'),
    path('search/', Search.as_view(), name='search'),
    path('fav/add/<int:id>', AddFavourites, name='add-fav'),
    path('profile/<str:username>', get_profile_view_by_username, name='profile-by-username'),
    #path('post/create', PostCreateView.as_view(), name='post-create'),
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 