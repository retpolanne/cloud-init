"""Integration test for the ssh module.

This test specifies a remote location for ssh authorized keys though the
``ssh`` module and then checks if those keys were added successfully to
the system."""

import pytest

from tests.integration_tests.releases import CURRENT_RELEASE

USER_DATA = """\
#cloud-config
ssh_authorized_keys_url: "http://localhost:8080/user.keys"
"""  # noqa


@pytest.mark.ci
@pytest.mark.user_data(USER_DATA)
class TestSshUrlProvided:

    @pytest.mark.parametrize(
        "expected_out",
        (
            ("teste")
        )
    )
    def test_ssh_provided_keys_from_url(self, expected_out, class_client):
        out = class_client.read_from_file(".ssh/authorized_keys").strip()
        assert expected_out in out
