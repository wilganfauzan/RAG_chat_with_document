from django.views import View
from django.shortcuts import render, redirect

from core.ai.mistralai import mistral
from .models import Document
from .task import process_document

from core.ai.chromadb import chroma, openai_ef


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

class QueryView(View):
    def get(self, request):
        return render(request, "documents/query.html")

    def post(self, request):
        query = request.POST.get("query")

        collection = chroma.get_or_create_collection(name="6810ee5905ad88e6897ff7fe", embedding_function=openai_ef)
        data = collection.query(
            query_texts=[query],
            n_results=3
        )
        print(data)