import pytest

from petab.v2 import Problem


def test_load_remote():
    """Test loading remote files"""
    yaml_url = (
        "https://raw.githubusercontent.com/PEtab-dev/petab_test_suite"
        "/main/petabtests/cases/v2.0.0/sbml/0001/_0001.yaml"
    )
    petab_problem = Problem.from_yaml(yaml_url)

    assert (
        petab_problem.measurement_df is not None
        and not petab_problem.measurement_df.empty
    )

    assert petab_problem.validate() == []

    yaml_url = yaml_url.replace("2.0.0", "1.0.0")
    with pytest.raises(
        ValueError, match="Provided PEtab files are of unsupported version"
    ):
        Problem.from_yaml(yaml_url)
