from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import time
import logging
from datetime import datetime
from django.core.cache import cache
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
  file_handler = logging.FileHandler("requests.log")
  formatter = logging.Formatter("%(message)s")
  file_handler.setFormatter(formatter)
  logger.addHandler(file_handler)

# 1
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

#2
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

#3
class OffensiveLanguageMiddleware:
  """For rate limiting. Limiting the number of
      messages for per minute"""
  

  def __init__(self, get_response):
    self.get_response = get_response
    self.request_ip_address = {}
  
  def __call__(self, request):
    if request.method == "POST" and request.path.startswith("/api/messages/"):
      ip  = self.ip_address_extractor(request)
      now = time.time()
      key = f"rate_limit:{ip}"
      timestamps = cache.get(key, [])
      timestamps = [ts for ts in timestamps if now - ts < 60]

      if len(timestamps) >= 5:
        data = {"detail": "Rate limit exceeded: Max 5 messages per minute."}
        json_rep = JSONRenderer().render(data)
        return HttpResponse(json_rep,content_type="application/json", status=status.HTTP_429_TOO_MANY_REQUESTS)
      
      timestamps.append(now)
      cache.set(key, timestamps, timeout=60)

    return self.get_response(request)
  
  def ip_address_extractor(self, request):
    """IP address extractor"""

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:

      ip = x_forwarded_for.split(",")[0]

    else:

      ip = request.META.get("REMOTE_ADDR")
    return ip

class RolepermissionMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
    self.jwt_authenticator = JWTAuthentication()
    self.role = ["admin", "moderator"]
  def __call__(self, request):
    if request.method == "GET" and request.path.startswith("/api/users/"):

      if not request.user.is_authenticated:
        try:
          auth_result = self.jwt_authenticator.authenticate(request)
          if auth_result is not None:
           user, token = auth_result
           request.user = user  # attach user to request
        except AuthenticationFailed:
          data = {"details": "Authentication required"}
          json_data = JSONRenderer().render(data)
          return HttpResponse(json_data, content_type="application/json", status=status.HTTP_401_UNAUTHORIZED)
      
      if request.user.role not in self.role:
        data = {"details": "You don't have permission to perform this action"}
        json_data = JSONRenderer().render(data)
        return HttpResponse(json_data, content_type="application/json", status=status.HTTP_403_FORBIDDEN)
    return self.get_response(request)