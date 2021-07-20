# from rest_framework import serializers, status
# from django.contrib.auth import get_user_model, authenticate
#
# User = get_user_model()
#
#
# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('login', 'password', )
#         extra_kwargs = {'password': {'write_only': True}, }
#
#         def create(self, validated_date):
#             user = User.objects.create(**validated_date)
#             return user
#
#         def update(self, instance, validated_data):
#             password = validated_data.pop('password', None)
#
#             for (key, value) in validated_data.items():
#                 setattr(instance, key, value)
#
#             if password is not None:
#                 instance.set_password(password)
#
#             instance.save()
#
#
# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ('id', 'login',)
#
#     def create(self, validated_data):
#         user = User.objects.create(**validated_data)
#         return user
#
#
# class LoginSerializer(serializers.Serializer):
#     login = serializers.CharField()
#     password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
#
#     def validate(self, data):
#         login = data.get('login')
#         password = data.get('password')
#
#         if login and password:
#             if User.objects.filter(login=login).exists():
#                 user = authenticate(request=self.context.get('request'), login=login, password=password)
#
#             else:
#                 raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)
#
#             if not user:
#                 raise serializers.ValidationError(status.HTTP_400_BAD_REQUEST)
#
#         else:
#             raise serializers.ValidationError(status.HTTP_401_UNAUTHORIZED)
#
#         data['user'] = user
#         return data
#
#
# class UsernameSerializer(serializers.Serializer):
#     login = serializers.CharField(required=True)
#
#
# class LoginResponseSerializer(serializers.Serializer):
#     expiry = serializers.DateTimeField(required=True)
#     token = serializers.CharField(required=True)
#     user = UsernameSerializer()
#
#
# class DiffSerialazer(serializers.Serializer):
#     initial_preprocessing_task_id = serializers.CharField(required=True)
#     changed_document_text = serializers.CharField(required=True)
#
#
# class PreprocessDocumentSerializer(serializers.Serializer):
#     document_content = serializers.CharField(required=True)
#
#
# class AdditionalMetaInfoSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     value = serializers.CharField(required=False, allow_blank=True)
#
#
# class DocumentMetaSerializer(serializers.Serializer):
#     additional_meta_info = AdditionalMetaInfoSerializer(
#         required=False,
#         many=True
#     )
#     author_name = serializers.CharField(
#         required=False,
#         allow_null=True,
#         allow_blank=True
#     )
#     date_of_sign = serializers.CharField(
#         required=False,
#         allow_null=True
#     )
#     id = serializers.CharField(
#         required=False
#     )
#     kind = serializers.CharField(
#         required=False,
#         allow_null=True,
#         allow_blank=True
#     )
#     name = serializers.CharField(
#         required=False,
#         allow_null=True,
#         allow_blank=True
#     )
#     number = serializers.CharField(required=False)
#     plain_text = serializers.CharField(required=False)
#     document_id = serializers.CharField(required=False)
#
#
# class StructureElementSerializer(serializers.Serializer):
#     element_number = serializers.IntegerField(required=True)
#     full_text = serializers.CharField(required=True)
#     internal_id = serializers.CharField(required=True)
#     kind = serializers.IntegerField(required=False)
#     name = serializers.CharField(
#         required=False,
#         allow_null=True,
#         allow_blank=True
#     )
#     number = serializers.CharField(
#         required=False,
#         allow_null=True,
#         allow_blank=True
#     )
#     paragraph_nr = serializers.ListField(required=True)
#     path = serializers.ListField(required=True, allow_empty=True)
#     text = serializers.CharField(required=False)
#     verbose_kind = serializers.CharField(required=False)
#
#
# class DiffStepsSerializer(serializers.Serializer):
#     text_action = serializers.CharField(required=True)
#     new_text = serializers.CharField(required=False)
#     removed_text = serializers.CharField(required=False)
#     start_index = serializers.IntegerField(required=True)
#     last_index = serializers.IntegerField(
#         required=False,
#     )
#
#
# class ChangesStructureElementsSerializer(serializers.Serializer):
#     structure_action = serializers.CharField(required=True)
#     structure_element = StructureElementSerializer()
#     diff_steps = DiffStepsSerializer(many=True)
#     changed_text = serializers.CharField(required=True)
#
#
# class GenerateDocumentSerializer(serializers.Serializer):
#     document_meta_info = DocumentMetaSerializer()
#     changes_structure_elements_info = ChangesStructureElementsSerializer(
#         many=True
#     )
#
#
# class TaskIdSerializer(serializers.Serializer):
#     task_id = serializers.CharField(required=True)
#
#
# class TaskStatusSerializer(serializers.Serializer):
#     task_id = serializers.CharField(source="guid")
#     status = serializers.CharField(source="task_status")
#
#
# class TaskResultSerializer(serializers.Serializer):
#     task_id = serializers.CharField()
#     result = serializers.JSONField()
