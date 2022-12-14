from django.urls import path # import Django's 'path' function
from . import views # Import our views from the 'blog' application 

# URL patterns for Blog Application 
urlpatterns = [
    path('', views.post_list, name = 'post_list'), # The 'view' called 'post_list' is assigned too the root URL. This pattern will match an empty string, and the Django URL resolver will ignore the domain name (i.e., http://127.0.0.1:8000/) that prefixes the full URL Path.  It will tell Django that views.post_list is the place to go if someone enters the website at http://127.0.0.1:8000/
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]