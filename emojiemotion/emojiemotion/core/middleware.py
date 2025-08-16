import logging
import requests
import ipaddress
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)

class IPWhitelistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips_url = 'https://pre-iam-dot-test-django-site.ey.r.appspot.com/api/active-ips/'

    def __call__(self, request):
        client_ip = self.get_client_ip(request)
        logger.info(f"[IPWhitelist] Client IP: {client_ip}")

        if not client_ip:
            logger.warning("[IPWhitelist] No valid client IP found.")
            return HttpResponseForbidden("No valid IP address found.")

        if not self.is_ipv4(client_ip):
            logger.warning(f"[IPWhitelist] Skipping invalid or non-IPv4 client IP: {client_ip}")
            return HttpResponseForbidden("Invalid IP address.")

        try:
            response = requests.get(self.allowed_ips_url, timeout=3)
            if response.status_code != 200:
                logger.error(f"[IPWhitelist] IP API responded with status {response.status_code}")
                return HttpResponseForbidden("IP check service unavailable.")

            data = response.json()
            allowed_ips = data.get("active_ips", [])
            allowed_ips = [ip.strip() for ip in allowed_ips if self.is_ipv4(ip)]

            # logger.info(f"[IPWhitelist] Fetched allowed IPs: {allowed_ips}")

        except Exception as e:
            logger.error(f"[IPWhitelist] Failed to fetch allowed IPs: {e}")
            return HttpResponseForbidden("Access temporarily unavailable due to IP check failure.")

        if client_ip not in allowed_ips:
            logger.warning(f"[IPWhitelist] Access denied for IP: {client_ip}")
            return HttpResponseForbidden("Your IP address is not allowed.")

        logger.info(f"[IPWhitelist] Access granted: IP {client_ip} is allowed.")
        return self.get_response(request)

    def get_client_ip(self, request):
        """
        Returns the real client IP address, prioritizing the X-Forwarded-For header.
        This is essential when behind a proxy (like GCP App Engine or Cloud Run).
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        remote_addr = request.META.get('REMOTE_ADDR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = remote_addr.strip() if remote_addr else None

        logger.info(f"[IPWhitelist] Determined Client IP: {ip}")
        return ip

    def is_ipv4(self, ip):
        """
        Checks if an IP address is an IPv4 address.
        """
        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.version == 4:
                return True
            else:
                logger.warning(f"[IPWhitelist] Ignoring IPv6: {ip}")
                return False
        except ValueError:
            logger.warning(f"[IPWhitelist] Invalid IP address: {ip}")
            return False
