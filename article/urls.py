from django.urls import path
from article.views import ArticleView , ArticleDetail
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/article/', ArticleView.as_view(), name='articleview'),
    path('api/article/<int:article_id>', ArticleDetail.as_view(), name='articledetail'),
]

