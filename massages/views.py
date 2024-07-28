from django.shortcuts import render

# Create your views here.
import imaplib
import email
from email.header import decode_header
# from django.conf import settings
from massage_integration.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD,EMAIL_HOST,EMAIL_PORT,imap_server
# from .models import User_massages
from celery import shared_task
import base64
from bs4 import BeautifulSoup
import re

# print(EMAIL_HOST_PASSWORD)
mail = imaplib.IMAP4_SSL(imap_server,EMAIL_PORT)
print(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
#
# #
mail.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
mail.select('inbox')
print(mail.select('inbox'))