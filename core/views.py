from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    #return HttpResponse('<h1>Hello World!</h1>')
    #return HttpResponse('<h1>Hello {}!</h1>'.format(nome))
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'.format(nome, idade))

def soma(request, num1, num2):
    soma = num1 + num2
    return HttpResponse('<h1>Soma de {} e {} = {}</h1>'.format(num1, num2, soma))

def subtracao(request, num1, num2):
    subtracao = num1 - num2
    return HttpResponse('<h1>Subtração de {} e {} = {}</h1>'.format(num1, num2, subtracao))

def multiplicacao(request, num1, num2):
    multiplicacao = num1 * num2
    return HttpResponse('<h1>Multiplicação de {} e {} = {}</h1>'.format(num1, num2, multiplicacao))

def divisao(request, num1, num2):
    divisao = num1 / num2
    return HttpResponse('<h1>Divisão de {} e {} = {}</h1>'.format(num1, num2, divisao))