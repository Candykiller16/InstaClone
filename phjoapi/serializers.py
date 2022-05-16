from rest_framework import serializers
from photojournal.models import Post, Profile, Comments, Category


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'username', 'short_intro', 'bio']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['body']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    category = CategoriesSerializer(many=True)
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments_set.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'slug', 'owner', 'category', 'likes', 'comments']
