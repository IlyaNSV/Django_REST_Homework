from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class DefaultLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5


class ProjectListPagination(PageNumberPagination):
    page_size = 10


class ToDoNoteListPagination(PageNumberPagination):
    page_size = 20
