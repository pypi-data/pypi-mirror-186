from django.urls import path, include
from . import views


app_name = 'zenblog'

urlpatterns = [
    # robots.txt는 반드시 가장 먼저
    path('robots.txt', views.robots),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:category_int>', views.Category.as_view(), name='category'),
    path('search-result/', views.SearchResult.as_view(), name='search_result'),
    path('search-tag/<str:tag>', views.SearchTag.as_view(), name='search_tag'),
    path('<slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]
