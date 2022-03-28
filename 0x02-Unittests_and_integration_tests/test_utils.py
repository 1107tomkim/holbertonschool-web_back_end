#!/usr/bin/env python3
""" Unit tests for utils.py """
from parameterized import parameterized
from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """Test that the method returns what its supposed to"""

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test for access nested map func"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test for error failures"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """Test for json funcs"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test to see if return is working"""
        with mock.patch("requests.get") as req:
            req().json.return_value = payload
            self.assertEqual(get_json(url), payload)


class TestMemoize(TestCase):
    """Tests for Memoize"""

    def test_memoize(self):
        """Test to make sure memoize sets attributes"""
        class TestClass:
            """Test class for memoize function"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test1 = TestClass()
        test1.a_method = mock.MagicMock(return_value=42)
        self.assertEqual(test1.a_property, 42)
        self.assertEqual(test1.a_property, 42)
        test1.a_method.assert_called_once()

        with mock.patch.object(TestClass, "a_method",
                               return_value=42) as mock_method:
            test2 = TestClass()
            self.assertEqual(test2.a_property, 42)
            self.assertEqual(test2.a_property, 42)
            mock_method.assert_called_once()
