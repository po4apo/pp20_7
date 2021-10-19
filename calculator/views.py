import json

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from calculator.forms import CalculatorForm, MemoryForm


def get_choices_from_cookie(request):
    choices = []
    for item in request.session.get('data', [{'answer': 'Значения '}]):
        choices.append((item, item['answer']))
    return choices


def show_main(request):
    answer = ''
    if request.method == 'GET':
        calculator_form = CalculatorForm(request.POST)
        memory_form = MemoryForm(request.POST, choices=get_choices_from_cookie(request))
        return render(request, 'main.html', {'calculator_form': calculator_form,
                                             'memory_form': memory_form,
                                             'answer': answer})

    elif request.method == 'POST':
        calculator_form = CalculatorForm(request.POST)
        choices = []
        for item in request.session.get('data', [{'answer': 'Значения '}]):
            choices.append((item, item['answer']))
        memory_form = MemoryForm(request.POST, choices=choices)

        if "_calculator" in request.POST:
            if calculator_form.is_valid():
                data = calculator_form.cleaned_data
                print(data)
                answer = (eval(f"{data['num1']}{data['operator']}{data['num2']}"))
                data['answer'] = answer
                got_data = request.session.get('data', [])

                if len(got_data) == 4:
                    del (got_data[0])
                    got_data.append(data)
                else:
                    got_data.append(data)
                request.session['data'] = got_data
                print(got_data)
                memory_form = MemoryForm(request.POST, choices=get_choices_from_cookie(request))


        elif "_memory" in request.POST:
            if memory_form.is_valid():
                print(memory_form.cleaned_data)
                memory_data = eval(memory_form.cleaned_data['list'])
                answer = memory_data['answer']
                del memory_data['answer']
                calculator_form.data = memory_data

        return render(request, 'main.html', {'calculator_form': calculator_form,
                                             'memory_form': memory_form,
                                             'answer': answer}, )


