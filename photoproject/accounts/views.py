from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import CustomUsertionForm
from django.urls import reverse_lazy

class SignUpView(CreateView):#サインアップページのビュー

  from_class = CustomUsertionForm
  template_name = "signup.html"
  success_url = reverse_lazy('accounts:signup_success')

  def from_vaild(self,form):#formオブジェクトのフィールドの値をデータベースに保存
    user = form.save()
    self.object = user
    return super().form_valid(form)#戻り値はスーパークラスのform_validの戻り値
  
class SignUpSuccessView(TemplateView):#サインアップ完了ページのビュー
  template_name = "acocunt/signup_success.html"#レンダリングるするテンプレート

# Create your views here.
