from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Lesson, Comment, User
from courses.serializers.category import CourseCategoryResumeSerializer

class LessonSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_category(self, obj):
        return CourseCategoryResumeSerializer(obj.category).data
    
class LessonWithPrevNextSerializer(serializers.ModelSerializer):
    prev = serializers.SerializerMethodField('get_prev_lesson')
    next = serializers.SerializerMethodField('get_next_lesson')
    professor = serializers.SerializerMethodField('get_professor_from_course')
    category = serializers.SerializerMethodField('get_category')
    
    class Meta:
        model = Lesson
        fields = '__all__'
        depth = 0
    
    def get_prev_lesson(self, obj):
        prev_lesson = Lesson.objects.filter(course=obj.course, id__lt=obj.id).order_by('-id').first()
        if prev_lesson:
            return LessonResumeSerializer(prev_lesson).data
        return None
    
    def get_category(self, obj):
        return CourseCategoryResumeSerializer(obj.category).data
    
    def get_next_lesson(self, obj):
        next_lesson = Lesson.objects.filter(course=obj.course, id__gt=obj.id).order_by('id').first()
        if next_lesson:
            return LessonResumeSerializer(next_lesson).data
        return None
    
    def get_professor_from_course(self, obj):
        return obj.course.professor.id
        


class LessonResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'banner']
        
        
class CommentReplySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'lesson']
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSimpleSerializer(user)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replies = CommentReplySerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'lesson', 'replies']
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSimpleSerializer(user)
        return serializer.data


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'photo']