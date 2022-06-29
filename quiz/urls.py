# quiz 폴더 안의 urls는 quiz app에 대한 url을 관리
# myapi 폴더 안의 url은 전체 프로젝트에 대한 url을 관리

from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
	path("hello/", helloAPI),
	path("<int:id>/", randomQuiz),
]