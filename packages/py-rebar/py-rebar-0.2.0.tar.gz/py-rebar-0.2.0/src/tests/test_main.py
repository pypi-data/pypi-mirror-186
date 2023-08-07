"""Unit tests for __main__.py."""
import pytest
from unittest.mock import patch

import pyrebar.__main__ as pymain


@pytest.mark.framework
@patch.object(pymain, "__name__", "__main__")
@patch.object(pymain, "main")
@patch.object(pymain.sys, "exit")
def test_main(mock_exit, mock_main):
    """Unit test the __main__ to be sure the application is executed."""
    mock_main.return_value = 42

    pymain.run_main()

    mock_main.assert_called()
    mock_exit.assert_called_with(42)
