from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    author = serializers.CharField()
    date_created = serializers.DateTimeField()


class ClassScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    start_date_and_time = serializers.DateTimeField()
    end_date_and_time = serializers.DateTimeField()
    is_repeated = serializers.BooleanField()
    repeat_frequency = serializers.CharField()
    is_active = serializers.BooleanField()
    organizer = serializers.CharField()
    cohort = CourseSerializer()
    venue = serializers.CharField()


class ClassAttendanceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    class_schedule = ClassScheduleSerializer()
    attendee = serializers.CharField()
    is_present = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = serializers.CharField()


class QuerySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    submitted_by = serializers.CharField()
    resolution_status = serializers.CharField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()
    author = serializers.CharField()


class QueryCommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    query = QuerySerializer()
    comment = serializers.CharField()
    author = serializers.CharField()
    date_created = serializers.DateTimeField()
    date_modified = serializers.DateTimeField()