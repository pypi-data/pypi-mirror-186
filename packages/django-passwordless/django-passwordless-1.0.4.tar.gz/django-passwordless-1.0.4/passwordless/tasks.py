from celery import shared_task


@shared_task
def celery_send_email(id):
    from .models import AuthRequest

    ar = AuthRequest.objects.get(id=id)
    ar.send_otp()
