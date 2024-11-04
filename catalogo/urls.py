from django.urls import path
from . import views

urlpatterns = [
    path('emprestimo/<int:livro_id>/', views.realizar_emprestimo, name='realizar_emprestimo'),
    path('devolucao/<int:emprestimo_id>/', views.realizar_devolucao, name='realizar_devolucao'),
    path('relatorio_livros_populares/', views.relatorio_livros_populares, name='relatorio_livros_populares'),
]
