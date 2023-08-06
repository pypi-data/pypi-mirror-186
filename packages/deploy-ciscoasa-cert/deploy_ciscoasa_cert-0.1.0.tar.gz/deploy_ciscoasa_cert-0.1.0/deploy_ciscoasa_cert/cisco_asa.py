"""
deploy_ciscoasa_cert / cisco_asa.py
Billy Zoellers, Dean Dorton

Cisco ASA REST API wrapper
"""
import requests
from loguru import logger


class CiscoASAREST:
    """
    Python client SDK for Cisco ASA REST API
    """

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        verify: bool = False,
    ):
        """
        Create an instance of CiscoASAREST
        """
        # Store input parameters
        self.verify = verify
        self.api_path = f"https://{host}/api"
        self.auth = (username, password)
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "REST API Agent",
        }

        # Disable warnings if not verifying SSL certificates
        if not self.verify:
            requests.packages.urllib3.disable_warnings()

        # Create an HTTPS session
        self.sess = requests.session()

    def req(self, resource: str, method: str = "get", **kwargs):
        """
        Generic HTTP request function
        """
        # Issue HTTP request
        resp = self.sess.request(
            url=f"{self.api_path}/{resource}",
            method=method,
            headers=self.headers,
            auth=self.auth,
            verify=self.verify,
            **kwargs,
        )

        # Ensure the request succeeded
        resp.raise_for_status()

        # Return body if exists
        if resp.text:
            return resp.json()

        return {}
