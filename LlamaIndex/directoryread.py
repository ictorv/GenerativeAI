from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from dotenv import load_dotenv
import sys,os

load_dotenv()

def main(url:str)->None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine=index.as_query_engine()
    response=query_engine.query("what is difference between webpageread and readdirectory files")
    print(response)

if __name__=='__main__':
    main(url='E:\Generative')