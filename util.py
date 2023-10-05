# 텍스트
# 이미지
# 테이블
# 레이아웃 : 슬라이드

import io
import requests
from pptx import Presentation
from pptx.util import Cm, Pt

import io
import requests
import traceback

def generate_text(prompt):
    messages = [
        {"role": "system", "content": "english teacher"},
        {"role": "user", "content": prompt} ]
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = { 
        'Content-Type': 'application/json',  
        'Authorization': 'Bearer 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'}
    body = {
        "model": "gpt-3.5-turbo", 
        "messages": messages, 
        "temperature": 0.5, # 창의 
        "max_tokens": 1000 #
    }
    
    res = requests.post(url, json=body, headers=headers).json()
    try: return res['choices'][0]['message']['content']
    except: 
        print(res, traceback.format_exc()); return ""

# PText("sdfg",size=Pt(90),bold=False, level=1),

print(generate_text("panda3d에서 texture 사용법 알려줘"))