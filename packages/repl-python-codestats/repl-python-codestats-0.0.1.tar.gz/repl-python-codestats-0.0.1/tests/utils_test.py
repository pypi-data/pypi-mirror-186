"""Test
=======
"""
import random
import sys

import pytest
from keyring import get_keyring

from repl_python_codestats.utils import get_api_key


class Test:
    """Test."""

    @pytest.mark.skipif(
        sys.platform == "linux",
        reason="no backend is installed in linux be default",
    )
    def test_get_api_key(self, caplog) -> None:
        """Test get api key.

        :param caplog:
        :rtype: None
        """
        expected = str(random.randint(0, 65536))  # nosec: B311
        keyring = get_keyring()
        service_name, user_name = "test", "codestats"
        api_key_name = "/".join([service_name, user_name])
        keyring.set_password(service_name, user_name, expected)
        rst = get_api_key(service_name, user_name)
        assert rst == expected
        keyring.delete_password(service_name, user_name)
        rst = get_api_key(service_name, user_name)
        expected = api_key_name + "has no password!"
        rst = caplog.records[-1].message
        assert rst == expected
