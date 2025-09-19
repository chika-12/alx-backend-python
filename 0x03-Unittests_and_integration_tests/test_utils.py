#!/usr/bin/env python3
import unittest
from utils import *
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
         MyClass is a demonstration class that shows how to use docstrings
         for documenting Python code.
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


if __name__ == "__main__":
    unittest.main()
