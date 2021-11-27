from rest_framework import serializers
from user.models import CustomUser


class SignupSerializer(serializers.ModelSerializer):
    password2= serializers.CharField(style= {'input_type': 'password'}, write_only= True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'birthday', 'address', 'sex', 'phone', 'password', 'password2']
    
    def validate_email(self, email):
        try:
            email = CustomUser.objects.get(email = email)
            raise serializers.ValidationError({'error': 'email is exist'})
        except:
            return email
    
    def validate_phone(self, phone):
        try:
            phone = CustomUser.objects.get(phone = phone)
            raise serializers.ValidationError({'error': 'phone is exist'})

            # note check phone is valid format
        except:
            return phone

    def create(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({ 'error': "password must match" })
        
        new_user = CustomUser(  
                                email=validated_data['email'],
                                username=validated_data['username'],
                                birthday=validated_data['birthday'],
                                address=validated_data['address'],
                                sex=validated_data['sex'],
                                phone=validated_data['phone']
                            )

        new_user.set_password(password)
        new_user.is_active = True
        new_user.save()

        return new_user

class LoginSerializer(serializers.ModelSerializer):

    user_id = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields= ('access_token', 'refresh_token', 'user_id')

        read_only_fields = ['access_token', 'refresh_token', 'user_id']
    
    def get_user_id(self, instance):
        return instance.id