from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from prompt_templates import PROMPT_TEMPLATE

def generate_answer(query_type, query_data):
    db = Chroma(persist_directory="embeddings/chroma_db", embedding_function=HuggingFaceEmbeddings())
    retriever = db.as_retriever(search_kwargs={"k": 3})
    
    llm = Ollama(model="gemma:2b") 

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=False
    )

    user_prompt = PROMPT_TEMPLATE.format(query=query_data["text"])
    result = chain.run(user_prompt)
    return result
