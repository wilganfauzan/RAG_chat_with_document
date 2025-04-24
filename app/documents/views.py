from django.views import View
from django.shortcuts import render, redirect

from core.ai.mistralai import mistral
from .models import Document
from .task import process_document


class DocumentUploadView(View):
    def get(self, request):
        return render(request, "documents/index.html")

    def post(self, request):
        file = request.FILES.get("file")

        try :
            document = Document.objects.create(file=file, name=file.name)

            process_document(document)

        except UnicodeDecodeError:
            print("UnicodeDecodeError")

        except Exception as e:
            print(e)

        return redirect("documents")