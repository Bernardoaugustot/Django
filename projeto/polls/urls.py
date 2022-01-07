from django.urls import path

from . import views

app_name = "polls"
# urlpatterns são as regras de caminhos que temos dentro do site, path recebe (caminho, onde vai abrir, nome exibido)

urlpatterns = [
    #Ppath('') esta dizendo que quando nenhum slug for informado ele vai cair nessa pag como defaul.
    #as_view() é quem é responsavel pelas chamadas da URL quando estamos trabalhando no modelo de Class (oque estamos afaznedo aqui)
    path('', views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail")
]
