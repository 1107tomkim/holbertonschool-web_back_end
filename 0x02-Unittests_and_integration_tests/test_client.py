#!/usr/bin/env python3
"""Unittest for client.py"""
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, PropertyMock
from urllib.error import HTTPError
from fixtures import *


class TestGithubOrgClient(TestCase):
    """Testing for the class object"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json",
           MagicMock(return_value={'key': 'value'}))
    def test_org(self, org_name):
        """test for test_org"""
        cls = GithubOrgClient(org_name)
        self.assertEqual(cls.org, {'key': 'value'})

    def test_public_repos_url(self):
        """test for test public repos url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value={"repos_url": "url"}):
            cls = GithubOrgClient('org_name')
            self.assertEqual(cls._public_repos_url, 'url')

    @patch('client.get_json')
    def test_public_repos(self, license):
        """test for public repos"""
        with patch('client.GithubOrgClient.public_repos',
                   new_callable=PropertyMock) as mock_repo:
            cls = GithubOrgClient('org_name')
            license.return_value = {'repos_url': 'url'}
            mock_repo.return_value = cls.org.get('repos_url')
            self.assertEqual(cls.public_repos, 'url')
            license.assert_called_once()
            mock_repo.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """test to see if test has license"""
        cls = GithubOrgClient('org_name')
        self.assertEqual(cls.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """integration testing for the class object"""

    @classmethod
    def setUpClass(cls):
        """tests to return payload"""
        cls.get_patcher = patch("requests.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """Teardown for integration tests"""
        cls.get_patcher.stop()
