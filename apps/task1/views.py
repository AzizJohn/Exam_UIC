from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.task1.models import Company, Vacancy, Resume
from rest_framework.views import APIView

from apps.task1.models import Company, Vacancy, Resume


# Create your views here.

class CompanyView(APIView):
    def get(self, request, *args, **kwargs):
        companies = Company.objects.all().count()
        vacancies = Vacancy.objects.all().count()
        resumes = Resume.objects.all().count()

        data = {
            'companies': companies,
            'vacancies': vacancies,
            'resumes': resumes,
        }

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
