from django.urls import path, include

from post import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.PostViewSet)
                # api/v1/posts/ - GET(list), POST(create)
                # api/v1/posts/<id>/ - GET(retrieve), PUT/PATCH(update/partial update), DELETE(destroy)


urlpatterns = [
    path('', include(router.urls)),
    # path('', views.PostListCreateView.as_view()),
    # path('<int:pk>/', views.PostDetailView.as_view()),
]

