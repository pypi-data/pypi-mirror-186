import time

from .thirdparty_packages import requests
try:
    from config import ThirdServicesConfig
    DNSLOG_SERVER = ThirdServicesConfig.DNSLOG_SERVER
except ImportError:
    DNSLOG_SERVER = ""


class GTLog(object):
    gtlog_addr = DNSLOG_SERVER

    def __init__(self):
        self.domain = []
        self.payload = []

    def get_random_domain(self):
        if not self.gtlog_addr:
            raise RuntimeError("DNSLOG server not configure)")
        for _ in range(2):
            try:
                rs = requests.get('{}/api/get_domain'.format(self.gtlog_addr))
            except:
                pass
            else:
                if rs.status_code == 200:
                    domain = rs.text
                    self.domain.append(domain)
                    return domain
            time.sleep(5)
        raise RuntimeError(f"Get Domain from {self.gtlog_addr} failed.")

    def verify_dnslog(self, domain=None, delay=5):
        if not self.gtlog_addr:
            raise RuntimeError("DNSLOG server not configure)")
        if domain is None:
            domain = self.domain[-1]
        for _ in range(3):
            time.sleep(delay)
            try:
                rs = requests.get('{}/api/verify_dnslog/{}'.format(self.gtlog_addr, domain))
            except:
                pass
            else:
                if rs.status_code == 200 and rs.json().get("status"):
                    return True
        return False

    def get_ldap_payload(self):
        if not self.gtlog_addr:
            raise RuntimeError("DNSLOG server not configure)")
        for _ in range(2):
            try:
                rs = requests.get('{}/api/get_ldap'.format(self.gtlog_addr))
            except:
                pass
            else:
                if rs.status_code == 200:
                    payload = rs.text
                    self.payload.append(payload)
                    return payload
            time.sleep(5)
        raise RuntimeError(f"Get Ldap Payload from {self.gtlog_addr} failed.")

    def verify_ldaplog(self, payload=None, delay=5):
        if not self.gtlog_addr:
            raise RuntimeError("DNSLOG server not configure)")
        if payload is None:
            payload = self.payload[-1]
        for _ in range(3):
            time.sleep(delay)
            try:
                rs = requests.get('{}/api/verify_ldap/{}'.format(self.gtlog_addr, payload))
            except:
                pass
            else:
                if rs.status_code == 200 and rs.json().get("status"):
                    return True
        return False
