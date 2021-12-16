from django.urls import path,re_path
from firstapp import views


urlpatterns = [
   re_path(r'^test/$',views.test),
   re_path(r'^$', views.index, name='index'),
   re_path(r'^student/$',views.student),
   # 位置参数：新闻查看/第几页/第几行
   re_path(r'show_news/(\d+)/(\d+)/$',views.show_news),
   re_path(r'show_news2/(?P<category>\d+)/(?P<page_no>\d+)/$',views.show_news2),
]