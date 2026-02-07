from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv();

print("Checking/Creating Vector DB locally");

embeddings = OpenAIEmbeddings();

DB_NAME = "runbookdb";
try:
    vec_db = FAISS.load_local(DB_NAME, embeddings=embeddings,allow_dangerous_deserialization=True);
    print("Loaded existing incident knowledge base");
except:
    initial_incidents = [
        "EC2 root volume reached 95% usage due to large log files in /var/log",
        "Application server disk full caused by old rotated logs not deleted",
        "Docker container stopped because /var/lib/docker consumed all disk space",
        "EBS volume latency increased due to disk almost full",
        "Jenkins server disk filled up because of old build artifacts",
        "Jenkins Pipeline not working",
        "Linux server disk usage high due to core dump files in /var/crash",
        "Kubernetes node disk pressure triggered pod evictions",
        "Database server disk full due to unchecked backup files accumulation"
    ];
    vec_db = FAISS.from_texts(texts=initial_incidents, embedding=embeddings);
    print("As vector DB does not exists , so Created Vector db");
    vec_db.save_local(DB_NAME);


query = "Jenkins issue";

if query == "":
    print("Empty Query");
else:
    result = vec_db.similarity_search_with_score(query=query, k=1);
    for doc, score in result:
        if score < 0.5:   # lower = more similar
            print(doc.page_content, " | score:", score);
        else:
            print("No relevant document found. Human intervention is required");