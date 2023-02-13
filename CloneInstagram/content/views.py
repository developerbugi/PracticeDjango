from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        print("GET 형식 호출")
        # select * from content_feed 와 동일
        fead_list = Feed.objects.all()

        # DB 넘어온 값 출력
        for feed in fead_list:
            print(feed.content)
            print(feed.image)
            print(feed.profile_image)
            print(feed.user_id)
            print(feed.like_count)

        return render(request, "cloneinstagram/main.html")
