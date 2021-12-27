import random

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer

from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.
class QuizRandomView(APIView):
    model = Quiz

    def get(self, request, cnt):
        total_quiz = Quiz.objects.all()
        random_quiz = random.sample(list(total_quiz), cnt)
        context = {}
        context['quiz'] = QuizSerializer(random_quiz, many=True).data
        return Response(context, status=status.HTTP_200_OK)


class QuizListView(APIView, LimitOffsetPagination):
    model = Quiz

    def get_context_data(self, **kwargs):
        # query_params => url encoded
        # request.data => request body
        params = (
            self.request.query_params
            if len(self.request.data) == 0
            else self.request.data
        )
        queryset = self.model.objects.all().order_by('-id')
        if params:
            if params.get('category'):
                queryset = queryset.filter(category=params.get('category'))
            if params.get('created_by'):
                queryset = queryset.filter(created_by__username=params.get('created_by'))

        context = {}

        results_quiz = self.paginate_queryset(
            queryset.distinct(), self.request, view=self
        )

        quiz = QuizSerializer(results_quiz, many=True).data

        if results_quiz:
            offset = queryset.filter(id__gte=results_quiz[-1].id).count()
            if offset == queryset.count():
                offset = None
        else:
            offset = 0

        context.update(
            {
                'quiz_count': self.count,
                'offset': offset
            }
        )
        context['quiz'] = quiz
        return context

    def get(self,request, *args, **kwargs):
        # if self.request.profile.role != "ADMIN" and not self.request.profile.is_admin:
        #     return Response(
        #         {
        #             "error": True,
        #             "errors": "You don't have permission to perform this action.",
        #         },
        #         status=status.HTTP_403_FORBIDDEN,
        #     )
        context = self.get_context_data(**kwargs)
        return Response(context, status=status.HTTP_200_OK)
