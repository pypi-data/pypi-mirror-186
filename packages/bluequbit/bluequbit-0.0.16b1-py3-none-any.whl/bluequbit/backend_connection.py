import json
import logging
import os
from pathlib import Path

import requests
import requests_toolbelt
import urllib3

from .exceptions import BQBaseException, BQUnauthorizedException
from .http_adapter import TimeoutHTTPAdapter
from .version import __version__

logger = logging.getLogger("bluequbit-python-sdk")


class BackendConnection:
    def __init__(self, api_token=None):
        config_dir = Path.home() / ".config" / "bluequbit"
        config_location = config_dir / "config.json"

        if api_token is None:
            if not config_location.is_file():
                raise BQBaseException(
                    0,
                    "Please specify an API key to BQClient(). You can find your API key once you log in to https://dev.app.bluequbit.io",
                )
            else:
                with open(config_location, encoding="utf-8") as f:
                    self._api_config = json.load(f)
        else:
            api_config = {
                "token": api_token,
                "main_endpoint": "https://dev.app.bluequbit.io/api/v1",
                "ssl_verify": True,
            }
            self._api_config = api_config
            config_dir.mkdir(exist_ok=True, parents=True)
            self.update_config_file(api_config, config_location)

        try:
            self._token = self._api_config["token"]
        except KeyError:
            raise BQBaseException(
                0,
                "Incorrect config file: 'token' key is not present in the config file "
                + str(config_location),
            )

        try:
            self._default_headers = {"Authorization": f"SDK {self._token}"}
            self._default_headers["User-Agent"] = requests_toolbelt.user_agent(
                "bluequbit", __version__
            )

            self._main_endpoint = "https://dev.app.bluequbit.io/api/v1"
            if "main_endpoint" in self._api_config:
                self._main_endpoint = self._api_config["main_endpoint"]
            self._verify = True
            if "ssl_verify" in self._api_config:
                self._verify = self._api_config["ssl_verify"]
            self._session = None
            self._authenticated = True
            response = self.send_request(
                req_type="GET",
                path="/jobs",
                params={"limit": 1},
            )
            if not self._verify:
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            if not response.ok:
                self._authenticated = False
                self._session = None
                if response.status_code == 401:
                    raise BQUnauthorizedException()
                raise BQBaseException(0, "Couldn't reach BlueQubit " + response.text)
        except:
            self._authenticated = False
            self._session = None
            raise

    @staticmethod
    def update_config_file(content, config_location):
        with open(config_location, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
        logger.info("Configuration file %s successfully updated.", config_location)

    def send_request(self, req_type, path, params=None, json_req=None):
        if not self._authenticated:
            raise BQBaseException(
                0,
                "BQClient was not initialized. Please provide correct API token to BQClient(<token>).",
            )
        url = self._main_endpoint + path

        if params is not None:
            for key, value in params.items():
                if isinstance(value, str):
                    params[key] = value.replace("\\", "\\\\")

        req = requests.Request(method=req_type, url=url, json=json_req, params=params)
        if self._session is None:
            self._session = self._create_session()
        prepared = self._session.prepare_request(req)
        resp = self._session.send(request=prepared, verify=self._verify)
        return resp

    def _create_session(self):
        session = requests.Session()
        adapter = TimeoutHTTPAdapter()
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        session.headers = self._default_headers

        if "BLUEQUBIT_DEBUG" in os.environ:
            session.hooks["response"].append(_log_requests)

        return session


if "BLUEQUBIT_DEBUG" in os.environ:
    from requests_toolbelt.utils import dump

    def _log_requests(response, *args, **kwargs):
        data = dump.dump_all(response)
        _log_requests.response_len += len(data)
        logger.info("HTTP %s %s ", response.request.url, _log_requests.response_len)

    _log_requests.response_len = 0
