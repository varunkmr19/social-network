from django.urls import path
#from django.conf import settings
#from django.conf.urls.static import static
from .views import AddLike, AddDislike, ProfileView, settings, AddFollower, RemoveFollower,PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentDeleteView
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('profile/settings', settings, name='profile-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/remove/follower/<int:pk>', RemoveFollower.as_view(), name='remove-follower'),
    path('profile/add/follower/<int:pk>', AddFollower.as_view(), name='add-follower'),
    path('post/add/like/<int:pk>', AddLike.as_view(), name='add-like'),
    path('post/remove/like/<int:pk>', AddDislike.as_view(), name='add-dislike'),

]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 