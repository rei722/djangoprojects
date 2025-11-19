from django.urls import path

from . import views

app_name = 'accounts'
#URLパターンを登録するための変数
urlpatterns = [
#サインアップページのビューの呼び出し
  path('signup/',
       views.SignUpView.as_view(),
       name='signup'),

#サインアップ完了ページのビューの呼び出し
  path('signup_success/',
       views.SignUpSuccessView.as_view(),
       name='signup_success'),
]