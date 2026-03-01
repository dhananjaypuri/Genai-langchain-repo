from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="Punjab_Two_Page_Overview.pdf");

docs = loader.load();

print(len(docs));

for pdf in docs:
    print(pdf.page_content);
    print(pdf.metadata);
    print("==========================");