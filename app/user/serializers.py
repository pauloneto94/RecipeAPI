from django.contrib.auth import get_user_model, authenticate
from rest_framework.serializers import Serializer, ModelSerializer, CharField, ValidationError
from django.utils.translation import ugettext_lazy as _


class UserSerializer(ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
            }
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(Serializer):
    """Serializer for the user authentication object"""
    email = CharField()
    password = CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise ValidationError(msg, code='authentication')
        
        attrs['user'] = user
        
        return attrs