from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Qwen2.5-7B-Instruct 모델 및 토크나이저 로드
model_name = "Qwen/Qwen2.5-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 프롬프트 생성 함수
def generate_prompt(user_input):
    system_message = "You are a helpful chemist's assistant."
    prompt = f"<|im_start|>system\n{system_message}<|im_end|>\n<|im_start|>user\n{user_input}<|im_end|>\n<|im_start|>assistant\n"
    return prompt

# 샘플 입력
user_input = "벤젠 고리에 아민기를 붙이고 싶다"
prompt = generate_prompt(user_input)

inputs = tokenizer(prompt, return_tensors="pt")
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=200)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# 출력 파싱 (간단한 예시)
ideas = response.split("\n")[:3]  # 첫 3줄만 추출

from pydantic import BaseModel, Field
from typing import List

class ChemicalIdea(BaseModel):
    idea: str = Field(..., min_length=5, max_length=200)

class ChemicalIdeaList(BaseModel):
    ideas: List[ChemicalIdea] = Field(..., min_items=1, max_items=3)

# 파싱된 아이디어 검증
validated_ideas = ChemicalIdeaList(ideas=[ChemicalIdea(idea=idea.strip()) for idea in ideas])