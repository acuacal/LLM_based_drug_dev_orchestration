from docling.document_converter import DocumentConverter
from glob import glob
import json

pdf_path_list = glob("./data/**/*.pdf",recursive=True)
md_rootpath = "./data/md"
json_rootpath = "./data/json"

for i,pdf_path in enumerate(pdf_path_list):
    # if i==1:
    #     break
    source = pdf_path
    converter = DocumentConverter()
    result = converter.convert(source)
    # JSON 형식으로 변환
    json_output = result.document.export_to_dict()
    with open(f"{json_rootpath}/{pdf_path.split('/')[-1].replace('.pdf','.json')}",'w') as f:
        json.dump(json_output,f)
    print(f"json file saved to {json_rootpath}/{pdf_path.split('/')[-1].replace('.pdf','.json')}")

    # 또는 Markdown 형식으로 변환
    markdown_output = result.document.export_to_markdown()
    with open(f"{md_rootpath}/{pdf_path.split('/')[-1].replace('.pdf','.md')}",'w') as f:
        f.write(markdown_output)
    print(f"md file saved to {md_rootpath}/{pdf_path.split('/')[-1].replace('.pdf','.md')}")