#from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "paginas/modelo.html"







"""
from django.views.generic import TemplateView
→ Isso está importando a classe TemplateView do módulo de views genéricas do Django.
Views genéricas são atalhos que o Django fornece para criar páginas comuns (como exibir um template, criar um objeto, listar objetos, etc.) sem você ter que escrever tudo do zero.

python
Copiar
Editar
class IndexView(TemplateView):
→ Aqui você está criando uma subclasse chamada IndexView, que herda de TemplateView.
Ou seja, IndexView é uma view baseada em classe que vai simplesmente renderizar um template.

python
Copiar
Editar
template_name = "index.html"
→ Essa variável diz qual template HTML será renderizado quando alguém acessar essa view.
Neste caso, será o arquivo index.html (que normalmente fica na pasta de templates do seu app ou projeto Django).

O que esse código faz na prática?
Ele define uma página que, quando acessada, irá exibir o conteúdo do template index.html.
Você não precisa escrever manualmente uma função que renderiza o template — o TemplateView já cuida disso.
"""