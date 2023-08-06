import requests
from .base import TRSregister
from tenacity import retry, wait_fixed, stop_after_attempt
from seqslab.auth.commands import BaseAuth
from nubia import context


class AzureTRSregister(TRSregister):

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(5), reraise=True)
    def workspace(self, name: str) -> dict:
        try:
            ctx = context.get_context()
            backend = ctx.args.backend
            token = BaseAuth.get_token().get("tokens").get("access")
        except KeyError:
            raise KeyError(f"No tokens, Please signin first!")
        url = self.WES_RESOURCES_URL.format(name=name, backend=backend)
        with requests.get(url, headers={"Authorization": f"Bearer {token}"}) as response:
            if response.status_code not in [requests.codes.ok]:
                raise requests.HTTPError(f"{response.status_code}: Can not access your workspace")
            return response.json()
