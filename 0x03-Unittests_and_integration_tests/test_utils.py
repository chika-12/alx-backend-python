#!/usr/bin/env python3
import unittest
from utils import *
from typing import Mapping, Sequence, Any
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
        TestAccessNestedMap is a demonstration class that shows how test
        cases for the access_nested_map works
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping[str, any],
            path: Sequence[str], expected: any
            ) -> None:
        """
           Access a value in a nested map using a sequence of keys.

           Args:
             nested_map (Mapping): The dictionary or mapping to traverse.
             path (Sequence): The keys representing the path to the value.

           Returns:
              Any: The value found at the end of the path.

           Raises:
              KeyError: If a key in the path does not exist in the map.
         """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping[str, any],
            path: Sequence[str]
            ) -> None:
        """
        Access value in nested map and raises exception if input
        doesn't match specification.
        Args:
            nested_map path
        Returns:
            Any: The value found at the end of the path.
        Raises:
            KeyError
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
        Test for a new class get_json
    """

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """
            Gets json from remote url
        """
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response
        url = "example.com"
        result = get_json(url)
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
