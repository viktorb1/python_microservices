import dramatiq
from django.core.mail import send_mail


@dramatiq.actor(queue_name="email")
def send_emails(order):
    send_mail(
        subject="An Order has been completed",
        message="Order #"
        + str(order["id"])
        + " with a total of $"
        + str(order["admin_revenue"])
        + "has been completed",
        from_email="from@email.com",
        recipient_list=["admin@admin.com"],
    )

    send_mail(
        subject="An Order has been completed",
        message="You earned $"
        + str(order["ambassador_revenue"])
        + " from the link #"
        + str(order["code"]),
        from_email="from@email.com",
        recipient_list=[order["ambassador_email"]],
    )
