import requests
import jwt

BASE_URL = "https://my.energo-pro.ge/owback"


class MyEPGeorgiaApi:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def _get_auth_headers(self):
        return {
            "Authorization": f"{self.login_state['tokenType']} {self.login_state['accessToken']}"
        }

    def _ensure_authed(self) -> None:
        if self._validate_token():
            return

        r = requests.post(f"{BASE_URL}/api/auth/signin",
                          json={"username": self.username, "password": self.password})
        r.raise_for_status()
        self.login_state = r.json()

        r = requests.post(f"{BASE_URL}/hasCompany", headers=self._get_auth_headers(), json={})
        r.raise_for_status()
        self.company_state = r.json()

    def _validate_token(self) -> bool:
        if hasattr(self, "login_state") and hasattr(self, "company_state"):
            try:
                self._parse_token()
            except Exception:
                return False
            return True

        return False

    def _find_account_uuid_by_number(self, account: str) -> str:
        for _, entry in enumerate(self.company_state["customersList"]):
            if entry["customerNumber"] == account:
                return entry["uuid"]
        return None

    def latest_measurement(self, account: str) -> str:
        self._ensure_authed()
        uuid = self._find_account_uuid_by_number(account)
        if not uuid:
            return None

        r = requests.get(f"{BASE_URL}/get/userTransactions/{uuid}", headers=self._get_auth_headers())
        r.raise_for_status()
        history = r.json()

        return max(map(lambda e: float(e["reading"]), history))
