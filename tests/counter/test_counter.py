from src.pre_built.counter import count_ocurrences
from unittest.mock import patch, mock_open


def test_counter():
    with patch("builtins.open", mock_open(read_data="Javascript Javascript")):
        assert count_ocurrences("path", "JAVASCRIPT") == 2
