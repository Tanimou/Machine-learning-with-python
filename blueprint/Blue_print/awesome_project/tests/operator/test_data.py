import urllib

import pytest
from awesome_project.operator import data


def test_get_data():
    with pytest.raises(urllib.error.URLError):
        data.get_data('fake_url', 'fake_location')
