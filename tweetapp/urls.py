from django.urls import path
from .views import PicList, PicDetail, PicCreate, PicDelete, PicUpdate, SignUpView

app_name = 'tweetapp'

urlpatterns = [
    path('list/', PicList.as_view(), name='list'),
    path('detail/<int:pk>', PicDetail.as_view(), name='detail'),
    path('create/', PicCreate.as_view(), name='create'),
    path('delete/<int:pk>', PicDelete.as_view(), name='delete'),
    path('update/<int:pk>', PicUpdate.as_view(), name='update'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]