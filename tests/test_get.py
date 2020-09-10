import pytest
import requests

from simple_ckan.core import CKANInstance


class TestCKANInstance:
    test_instance = CKANInstance("https://demo.ckan.org")

    def test_site_read(self):
        result = self.test_instance.action.get.site_read()
        assert result == True


class TestPackageList:
    test_instance = CKANInstance("https://demo.ckan.org")

    def test_package_list_no_args(self):
        result = self.test_instance.action.get.package_list()
        assert len(result) > 0

    def test_package_list_limit_10(self):
        limit = 10
        result = self.test_instance.action.get.package_list(limit=limit)
        assert len(result) == limit

    def test_package_list_limit_0(self):
        # If limit is set to zero, the argument is ignored
        limit = 0
        result = self.test_instance.action.get.package_list(limit=limit)
        assert len(result) > 0

    def test_package_list_negative_limit(self):
        limit = -10
        with pytest.raises(requests.exceptions.RequestException):
            self.test_instance.action.get.package_list(limit=limit)

    def test_package_list_negative_offset(self):
        limit = 10
        offset = -10
        with pytest.raises(requests.exceptions.RequestException):
            self.test_instance.action.get.package_list(limit=limit, offset=offset)
