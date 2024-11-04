from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Emprestimo

@shared_task
def enviar_lembrete_devolucao():
    hoje = timezone.now().date()
    emprestimos = Emprestimo.objects.filter(data_devolucao=None)
    for emprestimo in emprestimos:
        if (hoje - emprestimo.data_emprestimo).days >= 14:
            send_mail(
                'Lembrete de Devolução',
                f'Olá, {emprestimo.usuario.username}, lembre-se de devolver o livro "{emprestimo.livro.titulo}".',
                'biblioteca@exemplo.com',
                [emprestimo.usuario.email],
            )
