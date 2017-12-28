from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
 
from .permissions import IsStaffOrTargetUser
from .serializers import UserSerializer 
 
class UserView(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),


