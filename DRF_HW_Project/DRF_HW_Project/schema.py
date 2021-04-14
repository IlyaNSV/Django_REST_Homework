import graphene
from graphene_django import DjangoObjectType
from todoapp.models import ToDoNote, Project
from userapp.models import DefaultUser


class NoteType(DjangoObjectType):
    class Meta:
        model = ToDoNote
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = DefaultUser
        fields = '__all__'


class Query(graphene.ObjectType):
    all_notes = graphene.List(NoteType)
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)

    def resolve_all_notes(root, info):
        return ToDoNote.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return DefaultUser.objects.all()


schema = graphene.Schema(query=Query)
