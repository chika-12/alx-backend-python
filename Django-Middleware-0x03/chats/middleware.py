from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
  file_handler = logging.FileHandler("requests.log")
  formatter = logging.Formatter("%(message)s")
  file_handler.setFormatter(formatter)
  logger.addHandler(file_handler)


class RequestLoggingMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    response = self.get_response(request)
    user = request.user if request.user.is_authenticated else 'Anonymous' 
    logg_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
    print(logg_message)
    #print(request.user.first_name)
    logger.info(logg_message)
    return response

class RestrictAccessByTimeMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
  
  def __call__(self, request):
    start_hour = 9
    end_hour = 17

    current_hour = datetime.now().hour

    if current_hour < start_hour or current_hour > end_hour:
      data = {"detail": "Access restricted outside working hours."}
      json_resp = JSONRenderer().render(data)
      return HttpResponse(json_resp, content_type="application/json", status=status.HTTP_403_FORBIDDEN)
    response = self.get_response(request)
    return(response)

  