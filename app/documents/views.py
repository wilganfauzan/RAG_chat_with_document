# If you want a generic view for the documents
# from django.views.generic import TemplateView
#
# class DocumentUploadView(TemplateView):
#     template_name = 'documents/index.html'


# A simple way to make a GET and POST in one page
from django.views import View
from django.shortcuts import render, redirect

from core.ai.mistralai import mistral
from .models import Document

class DocumentUploadView(View):
    def get(self, request):
        return render(request, 'documents/index.html')

    def post(self, request):
        file = request.FILES.get("file")

        try :
            Document.objects.create(file=file, name=file.name)

            uploaded_pdf = mistral.files.upload(
                file={
                    "file_name": document.name,
                    "content": open(f"media/{document.name}", "rb")
                }
            ) # private

            signed_url = mistral.files.get_signed_url(file_id=uploaded_pdf.id)
            print(signed_url)

            ocr_result = mistral.ocr.process(
                model="mistral-ocr-latest",
                document={
                    "type": "document_url"
                    "document_url": signed_url.url
                }
            )

        except Exception as e:
            print(e)

        return redirect("documents")