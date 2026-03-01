from langchain_community.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader(path='pdfs');

docs = loader.load();

print(docs);



