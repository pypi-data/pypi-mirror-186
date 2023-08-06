"""This module implemented for Hepsiburada Data Science Team to interact with ElasticSearch.

Raises:
    NotImplementedError: Raises when the required method is not implemented.
    RuntimeError: Raises when ip is not set.
    RuntimeError: Raises when port is not set.
    RuntimeError: Raises when the index is empty.
    RuntimeError: Raises when the query is failed.
"""

import os
import time

import pandas as pd
from colorama import Fore, init
from elasticsearch import Elasticsearch, RequestError, helpers

init(autoreset=True)


class ElasticOperations(Elasticsearch):
    """This class is created to enable Hepsiburada Data Science to communicate with ElasticSearch"""

    _implemented_return_methods = ["raw", "hits", "total", "value", None]

    def __init__(self, **kwargs) -> None:

        self.ip = kwargs.get("ip")
        self.port = kwargs.get("port")
        self.batch_length = kwargs.get("batch_length", 30_000)
        kwargs.pop("ip", None)
        kwargs.pop("port", None)
        kwargs.pop("batch_length", None)
        self.client = self.create_client(self.ip, self.port, **kwargs)

    def create_client(self, ip, port, **kwargs):
        """Creates a elasticsearch client to run operations."""
        self.client = Elasticsearch([ip], port=port, **kwargs)
        return self.client

    def create_index(self, indexName):
        """Creates an index."""
        if self.client.indices.exists(index=indexName):
            print(Fore.YELLOW, f"Index {indexName} already exists.")
        else:
            self.client.indices.create(index=indexName)
            print(Fore.GREEN + f"Index {indexName} is created.")

    def delete_index(self, indexName):
        """Deletes the index."""
        if not self.client.indices.exists(index=indexName):
            print(Fore.YELLOW + f"Index {indexName} does not exist.")
        else:
            self.adjust_readonly(indexName, False)
            self.client.indices.delete(index=indexName)
            print(Fore.GREEN + f"Index {indexName} is deleted.")

    def get_count(self, indexName):
        """Returns the count of the given index."""

        self.client.indices.refresh(indexName)
        count = int(
            self.client.cat.count(indexName, params={"format": "json"})[0][
                "count"
            ]
        )
        return count + 1

    def set_max_result_window(self, indexName):
        """Sets the max_result_window of the index to assign readonly or nonreadonly."""
        count = self.get_count(indexName)

        label = {
            "index.blocks.read_only_allow_delete": "false",
            "index.max_result_window": count,
        }

        self.client.indices.put_settings(label, index=indexName)

    def check_read_only(self, indexName):
        """Checks the given index is read only or not"""

        self.client.indices.refresh(index=indexName)
        result = self.client.indices.get(index=indexName)[indexName]

        try:
            is_read_only = result["settings"]["index"]["blocks"]["read_only"]

            if is_read_only == "true":
                return True
            else:
                return False
        except KeyError:
            return None

    def nonreadonly(self, indexName):
        """Converts index from read only to non-read only"""

        self.set_max_result_window(indexName)

        is_read_only = self.check_read_only(indexName)

        if is_read_only is False:
            print(Fore.YELLOW + f"{indexName} was already not read only.")

        label = {"index.blocks.read_only": "false"}

        self.client.indices.put_settings(label, index=indexName)

    def readonly(self, indexName):
        """Converts index from read only to non-read only"""

        self.set_max_result_window(indexName)

        is_read_only = self.check_read_only(indexName)

        if is_read_only:
            print(Fore.YELLOW + f"{indexName} was already read only.")

        label = {"index.blocks.read_only": "true"}

        self.client.indices.put_settings(label, index=indexName)

    def adjust_readonly(self, indexName, read_only: bool):
        """Converts given index from read only to non-read only or vice versa."""

        self.set_max_result_window(indexName)

        is_read_only = self.check_read_only(indexName)

        if is_read_only and read_only:
            print(Fore.YELLOW + f"{indexName} was already read only.")

        elif not read_only and is_read_only is False:
            print(Fore.YELLOW + f"{indexName} was already not read only.")

        if read_only:
            label = {"index.blocks.read_only": "true"}
        else:
            label = {"index.blocks.read_only": "false"}

        self.client.indices.put_settings(label, index=indexName)

    def recreate_index(self, indexName):
        """Deletes and recreates the assigned index."""
        if not self.client.indices.exists(index=indexName):
            print(Fore.YELLOW + f"Index {indexName} does not exist.")
        else:
            self.adjust_readonly(indexName, False)
            self.client.indices.delete(index=indexName, ignore=[400, 404])
            self.client.indices.create(index=indexName)
            print(Fore.GREEN + f"Index {indexName} is recreated.")

    def send_data_to_elastic(self, indexName, data, timeout=30, verbose=False):
        """Uploads data batch by batch to elastic."""
        self.adjust_readonly(indexName, False)
        start_time = time.time()

        iteration_count = len(data) // self.batch_length + 1
        for idx in range(iteration_count):
            batch = data[
                idx * self.batch_length : (idx + 1) * self.batch_length
            ]
            helpers.bulk(
                self.client,
                batch,
                index=indexName,
                doc_type="_doc",
                request_timeout=timeout,
            )
            if verbose:
                print(
                    Fore.GREEN
                    + f"Batch {idx} is completed at {time.time() - start_time}"
                )
                start_time = time.time()

        self.adjust_readonly(indexName, True)

    def get_data_from_elastic(self, indexName):
        """Downloads data from given index."""

        count = self.get_count(indexName)
        size = count if count <= self.batch_length else self.batch_length
        count -= self.batch_length
        res = self.client.search(
            index=indexName,
            body={
                "query": {"match_all": {}},
                "sort": [{"_id": {"order": "asc"}}],
            },
            size=size,
        )

        result_data = [document["_source"] for document in res["hits"]["hits"]]

        for _ in range(count // self.batch_length + 1):
            if count <= 0:
                break

            size = count if count <= self.batch_length else self.batch_length
            body = {
                "query": {"match_all": {}},
                "search_after": [res["hits"]["hits"][-1]["_id"]],
                "sort": [{"_id": {"order": "asc"}}],
            }
            res = self.client.search(index=indexName, body=body, size=size)

            result_data.extend(
                [document["_source"] for document in res["hits"]["hits"]]
            )
            count -= self.batch_length

        main_df = pd.DataFrame.from_dict(result_data)
        return main_df

    def run_query(self, indexName, body, **kwargs):
        """Runs search query with respect to given body."""

        return_method = kwargs.get("return_method", None)
        allow_null = kwargs.get("allow_null", False)
        kwargs.pop("return_method", None)
        kwargs.pop("allow_null", None)

        if return_method not in ElasticOperations._implemented_return_methods:
            raise NotImplementedError(
                Fore.RED + f"Return type {return_method} not implemented !!"
            )
        count = self.get_count(indexName)
        if not allow_null and count <= 1:
            raise RuntimeError(
                Fore.RED
                + "Input index is empty!!"
                + " To skip this control set allow_null=True"
            )

        size = kwargs.get("size", count)
        kwargs.pop("size", None)

        try:
            res = self.client.search(
                index=indexName, body=body, size=size, **kwargs
            )
        except RequestError as request_error_message:
            raise RuntimeError(
                Fore.RED + f"query failed with error {request_error_message}"
            ) from request_error_message

        if not allow_null and len(res["hits"]["hits"]) <= 0:
            raise RuntimeError(
                Fore.RED
                + "Result query is empty !!"
                + " To skip this control set allow_null=True"
            )

        if return_method == "hits":
            return res["hits"]

        elif return_method == "total":
            return res["hits"]["total"]

        elif return_method == "value":
            return res["hits"]["total"]["value"]
        elif return_method == "raw":
            return res
        else:
            return res["hits"]["hits"]

    @property
    def ip(self):
        """This function is to get elastic client ip."""
        return self._ip

    @ip.setter
    def ip(self, provided_ip):
        """This function is to set elastic client ip."""
        if provided_ip is not None:
            self._ip = str(provided_ip)
        elif os.environ.get("ELASTIC_CLIENT_IP"):
            self._ip = os.environ.get("ELASTIC_CLIENT_IP")
        else:
            self._ip = None
            raise RuntimeError(Fore.RED + "Elastic client ip is not defined!")

    @property
    def port(self):
        """This function is to get elastic client port."""
        return self._port

    @port.setter
    def port(self, provided_port):
        """This function is to set elastic client port."""
        if provided_port is not None:
            self._port = int(provided_port)
        elif os.environ.get("ELASTIC_CLIENT_PORT"):
            self._port = os.environ.get("ELASTIC_CLIENT_PORT")
        else:
            self._port = None
            raise RuntimeError(
                Fore.RED + "Elastic client port is not defined!"
            )
