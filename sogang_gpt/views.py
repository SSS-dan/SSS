# importing render and redirect
from django.shortcuts import render, redirect
# importing the openai API
import openai
# import the generated API key from the secret_key file
from .secret_key import API_KEY

# loading the API key from the secret_key file
openai.api_key = API_KEY


# this is the home view for handling home page logic
def home(request):
    # if the session does not have a messages key, create one
    if 'messages' not in request.session:
        request.session['messages'] = [
            {"role": "system",
             "content": "너는 서강대학교 학생들에게 학교생활에 대한 도움을 주는 AI 도우미, Sogang GPT야."},
            {"role": "user",
             "content": "안녕, 넌 누구니?"},
            {"role": "assistant",
                "content": "안녕하세요, 저는 서강 GPT입니다. 학교 생활에 대해 어떤 게 궁금하신가요?"},
            {"role": "user",
                "content": "FA 제도에 대해서 알려줘."},
            {"role": "assistant",
                "content": "FA(Failure because of Absences) 제도란 한 학기동안 학생이 수강하는 과목에 대하여 결석허용한계를 \
                정하고 이를 초과해서 결석하는 경우에 해당과목을 낙제 처리하는 제도로 학생들로 하여금 수업참여에 대한 의무감을 심어주고, \
                대학 교육에 대한 학교와 학생, 학교와 학부모간의 신뢰도를 높이기 위해 운영하고 있는 제도이다. 결석 허용한계를 초과할 경우 \
                그 과목의 성적은 FA로 기록되며 과목낙제가 된다.\n"
                           "FA 제도에 대한 자세한 내용은 아래 링크를 참고해주세요.\n"
                           '<a href="https://www.sogang.ac.kr/bachelor/haksa/abs01.html" taget="_blank" title="서강대학교 학사규정">서강대학교 학사규정</a>'},
            {"role": "user",
                "content": "그럼 결석 허용한계는?"},
            {"role": "assistant",
                "content": "1. 매 과목당 결석 허용 횟수는 한 학기를 통산하여 주당 수업시간 수의 2배까지다. 즉 한 학기에 주당 3시간 과목은 6시간, 주당 2시간 과목은 4시간까지 결석이 허용된다 \
                    3회의 지각은 1회 결석으로 환산된다."},



        ]
    if request.method == 'POST':
        # get the prompt from the form
        prompt = request.POST.get('prompt')
        # get the temperature from the form
        temperature = float(request.POST.get('temperature', 0.1))
        # append the prompt to the messages list
        request.session['messages'].append({"role": "user", "content": prompt})
        # set the session as modified
        request.session.modified = True
        # call the openai API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=request.session['messages'],
            temperature=temperature,
            max_tokens=1000,
        )
        # format the response
        formatted_response = response['choices'][0]['message']['content']
        # append the response to the messages list
        request.session['messages'].append({"role": "assistant", "content": formatted_response})
        request.session.modified = True
        # redirect to the home page
        context = {
            'messages': request.session['messages'],
            'prompt': '',
            'temperature': temperature,
        }
        return render(request, 'gpt.html', context)
    else:
        # if the request is not a POST request, render the home page
        context = {
            'messages': request.session['messages'],
            'prompt': '',
            'temperature': 0.1,
        }
        return render(request, 'gpt.html', context)


def new_chat(request):
    # clear the messages list
    request.session.pop('messages', None)
    return redirect('home')


# this is the view for handling errors
def error_handler(request):
    return render(request, 'assistant/404.html')
