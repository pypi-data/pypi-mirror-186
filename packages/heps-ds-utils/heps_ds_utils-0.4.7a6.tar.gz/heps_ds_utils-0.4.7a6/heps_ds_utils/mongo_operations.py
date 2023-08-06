"""This module enables Hepsiburada Data Science to communicate with Mongo"""
import time

import pandas as pd
from colorama import Fore, init
from pymongo import MongoClient

init(autoreset=True)


class MongoOperations:
    """This class is created to enable Hepsiburada Data Science to communicate with Mongo"""

    _implemented_returns = ["dataframe", "records", "list", None]

    def __init__(self, **kwargs) -> None:
        self.ip = kwargs.get("ip")
        self.port = kwargs.get("port")
        self.connection_string = kwargs.get("connection_string")
        self.client = self.create_client(
            self.ip, self.port, self.connection_string
        )

    def create_client(
        self, ip: str = None, port: int = None, connection_string: str = None
    ):
        """Creates a client via ip & port or connection string.

        Args:
            ip (str, optional): Ip of Mongo.
            port (int, optional): Port to connect Mongo.
            connection_string (str, optional): Alternative way to connect Mongo

        Returns:
            Mongo Client: Client of the connection.
        """
        if (ip is None or port is None) and connection_string is None:
            raise RuntimeError(Fore.RED + "Mongo client is not defined!!")
        else:
            if connection_string:
                self.client = MongoClient(connection_string)
            else:
                self.client = MongoClient(host=ip, port=port)

        return self.client

    def show_databases(self, in_detail: bool = False):
        """Shows available databases.

        Args:
            in_detail (bool, optional): To show in detail or not.
                                        Defaults to False.
        """
        print("Available Databases:")
        if in_detail:
            databases = self.client.list_databases()
        else:
            databases = self.client.list_database_names()

        for database in databases:
            print(database)

    def show_collections(self, database_name: str, in_detail: bool = False):
        """Shows available collections.

        Args:
            database_name (str): Name of database
            in_detail (bool, optional): To show documents with detailly or not.
                                        Default is False.
        """
        print("Available Collections:")
        database = self.get_database(database_name)
        if in_detail:
            collections = database.list_collections()
        else:
            collections = database.list_collection_names()

        for collection in collections:
            print(collection)

    def create_database(self, database_name: str):
        """Creates database database with respect to input name.
           Creates database if it does not exist.

        Args:
            database_name (str): Database name to be created.

        Returns:
            Mongo Database: Group of Mongo to store collections.
        """
        if database_name not in self.client.list_database_names():
            database = self.client[database_name]
            database.create_collection("default")
            print(Fore.GREEN + f"{database_name} named database is created.")

        else:
            database = self.client[database_name]
            print(
                Fore.YELLOW + f"{database_name} named database already exist."
            )

        return database

    def create_collection(
        self, database_name: str, collection_name: str, **kwargs
    ):
        """Gets collection with respect to input name.
           Creates collection if it does not exist.

        Args:
            database_name (str): Database name as a parent of collection.
            collection_name (str): Collection name to be created.

        Returns:
            Mongo collection: Group of Mongo to store documents.
        """

        database = self.get_database(database_name)
        if collection_name not in database.list_collection_names():
            collection = database.create_collection(collection_name, **kwargs)
            print(
                Fore.GREEN + f"{collection_name} named collection is created."
            )
        else:
            collection = database[collection_name]
            print(
                Fore.YELLOW
                + f"{collection_name} named collection already exist."
            )

        return collection

    def get_database(self, database_name: str):
        """Gets database database with respect to input name.

        Args:
            database_name (str): Database name to be obtained.

        Returns:
            Mongo Database: Group of Mongo to store collections.
        """

        if database_name not in self.client.list_database_names():
            raise RuntimeError(
                Fore.RED
                + f"{database_name} does not exist. Call create_dabatase() function to create it."
            )
        else:
            database = self.client[database_name]
            return database

    def get_collection(self, database_name: str, collection_name: str):
        """Gets collection with respect to input name.

        Args:
            database_name (str): Database name as a parent of collection.
            collection_name (str): Collection name to be created.

        Returns:
            Mongo collection: Group of Mongo to store documents.
        """

        database = self.get_database(database_name)
        if collection_name not in database.list_collection_names():
            raise RuntimeError(
                Fore.RED
                + f"{collection_name} does not exist. Call create_collection() function to create it."
            )
        else:
            collection = database[collection_name]
            return collection

    def get_count(self, database_name: str, collection_name: str, filter={}):
        """Counts the document number in that collection.

        Args:
            database_name (str): Name of the database
            collection_name (str): Name of the collection
            filter (dict, optional): Filters documents that will be counted.
                                     Default is {}.
        Returns:
            int: Returns the document count of the collection.
        """
        collection = self.get_collection(database_name, collection_name)
        return collection.count_documents(filter=filter)

    def find_document(
        self, database_name: str, collection_name: str, **kwargs
    ):
        """Finds document from the collection.

        Args:
            database_name (str): Name of database
            collection_name (str): Name of collection
        Returns:
            Mongo document: Set of field-value pairs.
        """
        collection = self.get_collection(database_name, collection_name)

        filter = kwargs.get("filter")
        projection = kwargs.get("projection")
        sort = kwargs.get("sort")
        # 0 prevent limiting
        limit = kwargs.get("limit", 0)
        # List of dictionaries
        return_type = kwargs.get("return_type", "records")
        allow_null = kwargs.get("allow_null", False)
        if return_type not in MongoOperations._implemented_returns:
            raise NotImplementedError(
                Fore.RED + f"Return type {return_type} not implemented !!"
            )

        if type(sort) == tuple:
            sort = [sort]
        try:
            result = collection.find(
                filter=filter, sort=sort, limit=limit, projection=projection
            )
        except (ValueError, TypeError) as request_error_message:
            raise RuntimeError(
                Fore.RED + f"Command failed with error {request_error_message}"
            ) from request_error_message

        documents = [doc for doc in result]

        if not allow_null and len(documents) == 0:
            raise RuntimeError(
                Fore.RED
                + "Obtained data is empty!! To skip this control set allow_null=True "
            )

        if return_type == "dataframe":
            return pd.DataFrame.from_dict(documents)
        return documents

    def insert_document(self, database_name: str, collection_name: str, data):
        """Inserts document to the collection.

        Args:
            database_name (str): Name of database
            collection_name (str): Name of collection
            data (records or dict): To insert one data only one dict should be passed.
                                 To insert many data list of dicts should be passed.
        """

        collection = self.get_collection(database_name, collection_name)

        if type(data) == pd.DataFrame:
            data = data.to_dict("records")
        elif type(data) == dict:
            data = [data]

        if len(data) == 0:
            print(Fore.RED + "Input data is empty!!")

        if type(data) == list:
            try:
                result = collection.insert_many(data)
            except (ValueError, TypeError) as request_error_message:
                raise RuntimeError(
                    Fore.RED
                    + f"Command failed with error {request_error_message}"
                ) from request_error_message

            count = len(result.inserted_ids)
            print(Fore.GREEN + f"{count} documents inserted.")
        else:
            print(
                Fore.RED
                + "Could not insert data because type "
                + f"{type(data)} is not implemented!!"
            )
        # Time was required to insert document into cluster
        time.sleep(0.01)

    def update_document(
        self,
        database_name: str,
        collection_name: str,
        filter: dict,
        new_values: dict,
    ):
        """Updates document with respect to filter and new values.

        Args:
            database_name (str): Name of database
            collection_name (str): Name of collection
            filter (dict): Condition to select documents
            new_values (dict): New values to update the document.
        """
        collection = self.get_collection(database_name, collection_name)
        try:
            result = collection.update_many(filter, new_values)
        except (ValueError, TypeError) as request_error_message:
            raise RuntimeError(
                Fore.RED + f"Command failed with error {request_error_message}"
            ) from request_error_message

        count = result.modified_count
        if count == 0:
            print(Fore.YELLOW + "No documents updated!!")

        else:
            print(Fore.GREEN + f"{count} documents updated.")
        time.sleep(0.01)

    def delete_document(
        self, database_name: str, collection_name: str, filter: dict
    ):
        """Deletes document with respect to filter.

        Args:
            database_name (str): Name of database
            collection_name (str): Name of collection
            filter (dict): Filter to select documents to be deleted.
        """
        collection = self.get_collection(database_name, collection_name)
        try:
            count = collection.delete_many(filter).deleted_count
        except (ValueError, TypeError) as request_error_message:
            raise RuntimeError(
                Fore.RED + f"Command failed with error {request_error_message}"
            ) from request_error_message

        if count == 0:
            print(Fore.YELLOW + "No documents deleted!!")
        else:
            print(Fore.GREEN + f"{count} documents deleted.")
        time.sleep(0.01)

    def drop_database(self, database_name: str):
        """Drops the input database.

        Args:
            database (str): Name of database to be dropped.
        """
        if database_name not in self.client.list_database_names():
            print(
                Fore.YELLOW
                + f"{database_name} named database "
                + "has no collection or does not exist."
            )
        else:
            self.client.drop_database(database_name)
            print(Fore.GREEN + f"{database_name} named database is deleted.")

    def drop_collection(self, database_name: str, collection_name: str):
        """Drops the input collection

        Args:
            database (str): Group of Mongo collections.
            collection_name (str): Name of collection to be dropped.
        """
        database = self.get_database(database_name)
        if collection_name not in database.list_collection_names():
            print(
                Fore.YELLOW
                + f"{collection_name} named collection "
                + "already does not exist."
            )
        else:
            database.drop_collection(collection_name)
            print(
                Fore.GREEN + f"{collection_name} named collection is deleted."
            )

    @property
    def ip(self):
        """This function is to get Mongo client ip."""
        return self._ip

    @ip.setter
    def ip(self, provided_ip):
        """This function is to set Mongo client ip."""
        self._ip = provided_ip

    @property
    def port(self):
        """This function is to get Mongo client port."""
        return self._port

    @port.setter
    def port(self, provided_port):
        """This function is to set Mongo client port."""
        self._port = provided_port

    @property
    def connection_string(self):
        """This function is to get Mongo client connection string."""
        return self._connection_string

    @connection_string.setter
    def connection_string(self, provided_string):
        """This function is to set Mongo client connection string."""
        self._connection_string = provided_string
