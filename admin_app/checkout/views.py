from dramatiq import Message, get_broker, set_broker
from rest_framework import exceptions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Product, OrderItem
from checkout.serializers import LinkSerializer
import decimal
from django.db import transaction
import stripe
from django.forms.models import model_to_dict
from core.models import Link, Order


# Create your views here.
class LinkAPIView(APIView):
    def get(self, _, code=""):
        link = Link.objects.filter(code=code).first()
        serializer = LinkSerializer(link)
        return Response(serializer.data)


class OrderAPIView(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        link = Link.objects.filter(code=data["code"]).first()

        if not link:
            raise exceptions.APIException("Invalid code!")

        order = Order()
        order.code = link.code
        order.user_id = link.user.id
        order.ambassador_email = link.user.email
        order.first_name = data["first_name"]
        order.last_name = data["last_name"]
        order.email = data["email"]
        order.address = data["address"]
        order.country = data["country"]
        order.city = data["city"]
        order.zip = data["zip"]
        order.save()

        line_items = []

        for item in data["products"]:
            product = Product.objects.filter(pk=item["product_id"]).first()
            quantity = decimal.Decimal(item["quantity"])

            order_item = OrderItem()
            order_item.order = order
            order_item.product_title = product.title
            order_item.price = product.price
            order_item.quantity = quantity
            order_item.ambassador_revenue = (
                decimal.Decimal(0.1) * product.price * quantity
            )
            order_item.admin_revenue = decimal.Decimal(0.9) * product.price * quantity
            order_item.save()

            line_items.append(
                {
                    "quantity": quantity,
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(100 * product.price),
                        "product_data": {
                            "name": product.title,
                            "description": product.description,
                            "images": [product.image],
                        },
                    },
                }
            )

        stripe.api_key = "sk_test_51N036vFkNsK3rQNn9MEgqFLrJHU7PqFV9pLGRZPp96DJ77TQFwcFnWVji036XDb7FZ8XUmxMmWNSUEyiHxCVtMLJ00UXvivMam"

        source = stripe.checkout.Session.create(
            success_url="http://localhost:3001/success?source={CHECKOUT_SESSION_ID}",
            cancel_url="http://localhost:3001/error",
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
        )

        order.transaction_id = source["id"]
        order.save()

        return Response(source)


class OrderConfirmAPIView(APIView):
    def post(self, request):
        order = Order.objects.filter(transaction_id=request.data["source"]).first()

        if not order:
            raise exceptions.APIException("Order not found!")

        order.complete = True
        order.save()

        message = Message(
            queue_name="email",
            actor_name="send_emails",
            args=(order,),
            kwargs={},
            options={},
        )

        broker = get_broker()
        broker.enqueue(message)

        return Response({"message": "success"})


from faker import Faker
from random import randrange


class TestingView(APIView):
    def get(self, request):
        faker = Faker()
        order = Order.objects.create(
            user_id=25,
            code="code",
            ambassador_email="b@b.com",
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            complete=True,
        )

        for _ in range(randrange(1, 5)):
            price = randrange(10, 100)
            quantity = randrange(1, 5)
            OrderItem.objects.create(
                order_id=order.id,
                product_title=faker.name(),
                price=price,
                quantity=quantity,
                admin_revenue=0.9 * price * quantity,
                ambassador_revenue=0.1 * price * quantity,
            )

        o = model_to_dict(order)
        o["name"] = order.name
        o["ambassador_revenue"] = str(order.ambassador_revenue)
        o["admin_revenue"] = str(order.admin_revenue)

        message = Message(
            queue_name="email",
            actor_name="send_emails",
            args=(o,),
            kwargs={},
            options={},
        )

        broker = get_broker()
        broker.enqueue(message)

        return Response({"message": "success"})
