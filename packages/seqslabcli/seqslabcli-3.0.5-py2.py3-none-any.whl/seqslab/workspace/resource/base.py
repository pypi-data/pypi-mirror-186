import requests
import logging
from tenacity import retry, wait_fixed, stop_after_attempt
from seqslab.auth.commands import BaseAuth
from seqslab import trs, drs, wes, workspace
import json
from typing import List, Dict
from functools import lru_cache
from nubia import context


class BaseResource:
    logger = logging.getLogger()

    TRS_BASE_URL = f"https://{trs.API_HOSTNAME}/trs/{trs.__version__}"
    TRS_WORKSPACE_URL = f"{TRS_BASE_URL}/service-info/workspaces/?backend={{backend}}"

    DRS_BASE_URL = f"https://{drs.API_HOSTNAME}/ga4gh/drs/{drs.__version__}"
    DRS_WORKSPACE_URL = f"{DRS_BASE_URL}/service-info/workspaces/?backend={{backend}}"

    WES_BASE_URL = f"https://{wes.API_HOSTNAME}/wes/{wes.__version__}"
    WES_WORKSPACE_URL = f"{WES_BASE_URL}/service-info/workspaces/?backend={{backend}}"
    WES_CONTAINER_REGISTRY_URL = f"{WES_BASE_URL}/service-info/workspaces/{{name}}/container-registries/?backend={{" \
                                 f"backend}}"

    MGMT_BASE_URL = f"https://{workspace.API_HOSTNAME}/management/{workspace.__version__}"
    MGMT_WORKSPACE_URL = f"{MGMT_BASE_URL}/workspaces/?backend={{backend}}"
    MGMT_STATUS_URL = f"{MGMT_BASE_URL}/workspaces/status/{{task_id}}/?backend={{backend}}"

    @staticmethod
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
    @lru_cache(maxsize=16)
    def list_workspaces(**kwargs) -> List[dict]:
        token = BaseAuth.get_token().get("tokens").get("access")
        with requests.get(url=kwargs.get("system"),
                          headers={"Authorization": f"Bearer {token}"},
                          params={"expand": kwargs.get('expand'),
                                  "force": kwargs.get('force')}) as response:
            if response.status_code not in [requests.codes.ok]:
                raise requests.HTTPError(f"{json.loads(response.content)}")
            return response.json()

    @staticmethod
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=False)
    def create_workspaces(name, location, **kwargs) -> dict:
        ctx = context.get_context()
        backend = ctx.args.backend
        token = BaseAuth.get_token().get("tokens").get("access")
        with requests.put(url=BaseResource.MGMT_WORKSPACE_URL.format(backend=backend),
                          headers={"Authorization": f"Bearer {token}"},
                          data={
                              "workspace": name,
                              "location": location
                          }) as response:
            if response.status_code not in [202]:
                raise requests.HTTPError(json.loads(response.content))
            return response.json()

    @staticmethod
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
    def status(task_id, **kwargs) -> dict:
        ctx = context.get_context()
        backend = ctx.args.backend
        token = BaseAuth.get_token().get("tokens").get("access")
        with requests.get(url=BaseResource.MGMT_STATUS_URL.format(task_id=task_id, backend=backend),
                          headers={"Authorization": f"Bearer {token}"}) as response:
            if response.status_code not in [requests.codes.ok]:
                raise requests.HTTPError(json.loads(response.content))
            return response.json()

    @staticmethod
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
    @lru_cache(maxsize=16)
    def container_registry(workspace, **kwargs) -> dict:
        ctx = context.get_context()
        backend = ctx.args.backend
        token = BaseAuth.get_token().get("tokens").get("access")
        url = BaseResource.WES_CONTAINER_REGISTRY_URL.format(name=workspace, backend=backend)
        with requests.get(url=url,
                          headers={"Authorization": f"Bearer {token}"}) as response:
            if response.status_code not in [requests.codes.ok]:
                raise requests.HTTPError(json.loads(response.content))
            return json.loads(response.content)
