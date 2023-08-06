import os
import requests
from urllib.parse import urlparse


def get_token(url_path):
    from metaflow.metaflow_config import (
        METADATA_SERVICE_HEADERS,
        from_conf,
        METADATA_SERVICE_URL,
    )
    from metaflow.exception import MetaflowException

    # Infer auth host from metadata service URL, unless it has been
    # specified explicitly. Take the MDS host and replace first part of
    # the domain name with `auth.`. All our deployments follow this scheme
    # anyways.
    #
    auth_host = "auth." + urlparse(METADATA_SERVICE_URL).hostname.split(".", 1)[1]

    authServer = from_conf("OBP_AUTH_SERVER", auth_host)
    assert url_path.startswith("/")
    url = "https://" + authServer + url_path
    headers = METADATA_SERVICE_HEADERS
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        token_info = r.json()
        return token_info

    except requests.exceptions.HTTPError as e:
        raise MetaflowException(repr(e))
