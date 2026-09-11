import pytest
from ml_systems_blueprints.contracts import require_columns
def test_contract():
    assert require_columns({"x":1},["x"])
    with pytest.raises(ValueError): require_columns({},["x"])
