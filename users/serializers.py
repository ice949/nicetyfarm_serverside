from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
    phone_number = serializers.CharField()


class CohortSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    year = serializers.IntegerField()
    author = UserSerializer()


class CohortMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cohort = CohortSerializer()
    member = UserSerializer()
    is_active = serializers.BooleanField()
    author = UserSerializer()