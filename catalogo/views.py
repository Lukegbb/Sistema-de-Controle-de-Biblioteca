from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Livro, Emprestimo
from django.db.models import Count

@login_required
def realizar_emprestimo(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if livro.status == 'DISPONIVEL':
        livro.status = 'EMPRESTADO'
        livro.save()
        Emprestimo.objects.create(usuario=request.user, livro=livro)
    return redirect('lista_livros')

@login_required
def realizar_devolucao(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    emprestimo.data_devolucao = timezone.now()
    emprestimo.livro.status = 'DISPONIVEL'
    emprestimo.livro.save()
    emprestimo.save()
    return redirect('lista_emprestimos')

def relatorio_livros_populares(request):
    livros_populares = Livro.objects.annotate(total_emprestimos=Count('emprestimo')).order_by('-total_emprestimos')[:10]
    return render(request, 'catalogo/relatorio_livros_populares.html', {'livros_populares': livros_populares})
