from django.utils import timezone

from apps.user.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserStatus:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_user = JWTAuthentication().authenticate(request)[0]


        for user in User.objects.all():
            if (timezone.now() - user.last_action) > timezone.timedelta(minutes=1):
                user.is_online=False
                user.save()
        
        if request_user:
            user = User.objects.get(id=request_user.id)
            user.is_online=True
            user.last_action = timezone.now()
            user.save()

        return self.get_response(request)




        #    def process_view(self, request, view_func, view_args, view_kwargs):
        # for user in User.objects.all():
        #     if (timezone.now() - user.last_action) > timezone.timedelta(minutes=2):
        #         user.is_online=False
        #         user.save()
        
        # assert hasattr(request, 'user')
        # if request.user.is_authenticated:
        #     user = User.objects.get(id=request.user.id)
        #     user.is_online=True
        #     user.last_action = timezone.now()
        #     user.save()