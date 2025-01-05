from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import os
import openai


@csrf_exempt
def consult(req):
    
    reqDate = req.body.decode('utf-8')
    # print(os.getenv("OPENAI_API_KEY").strip())
    open_api_key = os.getenv("OPENAI_API_KEY")
    prompt = """너는 우울한 사람들 상담하는 심리 상담사야. 상담내용을 긍정적인 내용으로 바꾸면 돼. 혹시 장원영의 럭키비키식 사고 알고 있으면 그렇게 해.
    그리고 만약에 상관없는 질문이 오면 대답 할 수 없다고 하면 돼"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": reqDate}
        ]
    )
    print(response['choices'][0]['message']['content'])
    consult = response['choices'][0]['message']['content']
    
    return JsonResponse( { "consult": consult } )
