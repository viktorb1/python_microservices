from django.shortcuts import render
from django.http import HttpResponse

from dramatiq import Message
from dramatiq.broker import get_broker
