from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])


# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from .views import SnippetList, SnippetDetail, UserList, UserDetail, SnippetHighlight, api_root


# urlpatterns = [
#     path('snippets/', SnippetList.as_view()),
#     path('snippets/<int:pk>/', SnippetDetail.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('', api_root),
#     path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view()),
# ]

# Добавляет суффиксы форматов (расширения)
# urlpatterns = format_suffix_patterns(urlpatterns)
