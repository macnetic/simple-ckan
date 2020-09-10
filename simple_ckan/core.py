import urllib.parse

import requests

from .action import CKANAction


class CKANInstance(object):
    def __init__(
        self,
        baseurl,
        api_path=None,
        version=None,
        user_agent=None,
        session=None,
        get_only=False,
    ):
        self.version = version
        self.api_url(baseurl, api_path=api_path, version=self.version)
        self.get_only = get_only

        if not session:
            self.session = requests.Session()
        if not user_agent:
            # TODO write default user agent
            pass

        self.action = CKANAction(self)

    def query(self):
        pass

    def raw_query(self):
        pass

    # def sql_query(self):
    #     pass

    # TODO rename function to something like query()
    def call_action(self, action, data=None):
        """Query a CKAN Action API instance

        Args:
            action ([type]): [description]
            data ([type], optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        if action != "":
            url = "/".join((self.url, action))
        else:
            raise ValueError
        # url = urllib.parse.urljoin(self.url, action)

        if self.get_only:
            response = self.session.get(url, params=data)
        else:
            response = self.session.post(url, json=data)

        response.raise_for_status()

        # try:
        #     if self.get_only:
        #         response = self.session.get(url, params=data)
        #     else:
        #         response = self.session.post(url, json=data)

        #     response.raise_for_status()

        # except requests.RequestException as e:
        #     # TODO write exception handling
        #     print(e)
        #     pass

        response = response.json()

        if not response.get("success"):
            print("Request was received but not accepted")

        return response.get("result")

    # TODO refactor into a raw query function raw_query(), and a SQL query function sql_query()
    def sql_query(self, action, query):
        """Send an SQL query to a CKAN Action API instance.

        Args:
            action ([type]): [description]
            query ([type]): [description]

        Returns:
            [type]: [description]
        """
        url = urllib.parse.urljoin(self.url, action)

        query = " ".join(query.split()).encode("utf-8")

        if self.get_only:
            query = urllib.parse.quote(query)
            req = requests.Request("GET", url, params={"sql": ""})
            prep = req.prepare()
            prep.url = prep.url + query

            response = self.session.send(prep)
        else:
            response = self.session.post(url, json={"sql": query})

        response.raise_for_status()

        return response.json()

    def api_url(self, baseurl, api_path=None, version=None):
        self.baseurl = baseurl.rstrip("/")

        if api_path is None:
            if version is None:
                self.api_path = "/".join(("api", "action"))
            else:
                self.api_path = "/".join(("api", version, "action"))
        else:
            self.api_path = api_path

        self.url = urllib.parse.urljoin(self.baseurl, self.api_path)
