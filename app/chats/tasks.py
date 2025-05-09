from huey.contrib.djhuey import task

from core.ai.prompt_manager import PromptManager
from core.methods import send_chat_message
from core.ai.chromadb import chroma, openai_ef


@task()
def process_chat(message, document_id):

    collections = chroma.get_collection(document_id, embedding_function=openai_ef)
    res = collection.query(query_texts=[message], n_results=3)

    print(res) #39.23

    pm = PromptManager()
    pm.add_message("user", message)

    assistant_message = pm.generate()
    send_chat_message(assistant_message)