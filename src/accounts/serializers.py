from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # Assigning the model to the serializer
        fields = ('username', 'password', 'first_name', 'last_name', 'email',) # Explicit specification of fields to be 
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
 
    # # Deprecated method needs to be replaced
    # def restore_object(self, attrs, instance=None):
    #     # call set_password on user object. Without this
    #     # the password will be stored in plain text.
    #     user = super(UserSerializer, self).restore_object(attrs, instance)
    #     user.set_password(attrs['password'])
    #     return user
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password = make_password(validated_data['password'])
        )
        return user