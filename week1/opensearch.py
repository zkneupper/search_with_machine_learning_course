#!/usr/bin/env python

"""The `opensearch.py` module defines the `get_opensearch()` function
that creates an OpenSearch client instance, makes that client available
in flask's global namespace `g` by setting `g.opensearch`, and returns
the OpenSearch client.

References:
> See opensearch-py docs:
> https://github.com/opensearch-project/opensearch-py
"""


import os
from dotenv import load_dotenv
from flask import g, current_app
from opensearchpy import OpenSearch


# Create an OpenSearch client instance and put it into Flask shared space for use by the application
def get_opensearch():
    if "opensearch" not in g:
        # Implement a client connection to OpenSearch so that the rest of the application can communicate with OpenSearch

        HOST = "localhost"
        PORT = 9200

        load_dotenv()

        auth = (
            os.environ.get("OPENSEARCH_USERNAME", None),
            os.environ.get("OPENSEARCH_PW", None),
        )

        # Create the client with SSL/TLS disabled, and hostname verification disabled.
        client = OpenSearch(
            hosts=[{"host": HOST, "port": PORT}],
            http_compress=True,  # enables gzip compression for request bodies
            http_auth=auth,
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

        g.opensearch = client

    return g.opensearch
