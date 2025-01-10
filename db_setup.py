import os
import json
from milvus import default_server
from pymilvus import (
    connections, 
    FieldSchema, 
    CollectionSchema, 
    DataType, 
    Collection,
    utility
)
import subprocess    
from sentence_transformers import SentenceTransformer

def restart_milvus():
    # 기존 Milvus 프로세스 종료
    subprocess.run(["pkill", "-f", "milvus"])
    
    # cleanup 수행
    default_server.cleanup()
    
    # 서버 재시작
    default_server.start()

# 서버 상태 확인 및 재시작

restart_milvus()

# 로컬호스트와 지정된 포트로 연결
connections.connect(host='127.0.0.1', port=default_server.listen_port)

# (1) 임베딩 모델 로드
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# if utility.has_collection("papers_vector_collection"):
#     utility.drop_collection("papers_vector_collection")
# 3) Collection Schema 정의
#    - id: 자동 생성되는 primary key
#    - paragraph_text: 실제 텍스트 저장용 (최대 길이 지정 필요)
#    - embeddings: 벡터 필드 (dim=384, float vector)
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="paragraph_text", dtype=DataType.VARCHAR, max_length=65535),  # or 적절히
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=384)
]
schema = CollectionSchema(fields, "Collection for storing paragraphs with embeddings")

collection_name = "papers_vector_collection"

# 컬렉션 생성 (이미 있다면 예외 처리)
try:
    collection = Collection(name=collection_name, schema=schema)
    print(f"Collection '{collection_name}' 생성 완료")
except Exception as e:
    print(f"이미 Collection이 존재하거나 오류 발생: {e}")
    collection = Collection(collection_name)

# (4) Milvus 검색에 유리하도록 인덱스 정의 (예: IVF_FLAT)
#     매개변수는 벡터 인덱싱 방법에 따라 달라짐
index_params = {
    "metric_type": "IP",   # inner product
    "index_type": "IVF_FLAT",
    "params": {"nlist": 128}
}
collection.create_index(
    field_name="embeddings",
    index_params=index_params
)
print("인덱스 생성 완료")

###############################################################################
# (5) PDF -> JSON/MD에서 텍스트 읽고, 단락 단위로 임베딩 후 Milvus에 Insert
###############################################################################
docs_base_path = "./data/md"  # JSON, MD 등이 있는 디렉토리
def load_paragraphs_from_files(dir_path):
    """PDF->JSON or MD로 변환된 파일들에서 텍스트를 추출해 paragraphs 리스트로 반환"""
    paragraphs = []
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if filename.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # JSON 구조 예시에 따라 추출
                if "paragraphs" in data:
                    for p in data["paragraphs"]:
                        if p.strip():
                            paragraphs.append(p.strip())
        elif filename.endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                splitted = content.split("\n\n")
                for p in splitted:
                    if p.strip():
                        paragraphs.append(p.strip())
    return paragraphs

paragraphs = load_paragraphs_from_files(docs_base_path)

batch_size = 64
temp_embeddings = []
temp_texts = []

for i, paragraph in enumerate(paragraphs):
    emb = model.encode(paragraph)
    temp_embeddings.append(emb)
    temp_texts.append(paragraph)

    # batch insert
    if (i+1) % batch_size == 0:
        entities = [
            temp_texts,      # paragraph_text field
            temp_embeddings  # embeddings field
        ]
        insert_result = collection.insert(entities)
        temp_embeddings = []
        temp_texts = []

# 마지막 배치 처리
if temp_embeddings:
    entities = [
        temp_texts, 
        temp_embeddings
    ]
    collection.insert(entities)

collection.flush()
print("모든 데이터 삽입 및 flush 완료.")
###############################################################################
# (6) 검색 (예: "CYP inhibition" 키워드로 TOP-K=3)
###############################################################################
collection.load()  # 검색을 위해 메모리에 로드
# 1) 검색할 쿼리
query_text = "CYP inhibition"
query_embedding = model.encode(query_text)

search_params = {
    "metric_type": "IP",
    "params": {"nprobe": 10}  # IVF_FLAT 인덱스 환경에서 nprobe=10
}
top_k = 10

# 2) 검색 시 output_fields에 paragraph_text 지정
results = collection.search(
    data=[query_embedding], 
    anns_field="embeddings",
    param=search_params,
    limit=top_k,
    output_fields=["paragraph_text"]  # ← 여기서 텍스트 필드 이름 지정!
)

# 3) 결과 출력 (텍스트+distance 같이)
print(f"Query: {query_text}")
for i, hits in enumerate(results):
    print(f"\n===== Result of query #{i+1} =====")
    for rank, hit in enumerate(hits, start=1):
        text_snippet = hit.entity.get("paragraph_text")
        distance = hit.distance
        print(f"[Rank {rank}] ID: {hit.id}, distance: {distance:.4f}")
        print(f"    => Text: {text_snippet[:150]}...")
    print("===============================")
