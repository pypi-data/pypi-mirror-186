import paramanager as pm
import pytest


def test_pretty_print(capfd):
    proto_parameters = [pm.ProtoParameter("lovely", 0.0), pm.ProtoParameter("required", 0.0, required=True)]
    ps = pm.ParameterSet(proto_parameters,"Params")

    ps.pretty_print()

    out, err = capfd.readouterr()
    assert out == "\n[Params]\nlovely -> 0.0\nrequired -> NOT SET\n"



def test_required_parameter():
    proto_parameters = [pm.ProtoParameter("required", 0.0, required=True)]
    ps = pm.ParameterSet(proto_parameters)

    with pytest.raises(ValueError):
        ps.check_unset_parameters()

    with pytest.raises(ValueError):
        ps.read_argv(args=[])

    with pytest.raises(ValueError):
        ps.read_argv(args=["-required", "is_not_float"])

    ps.read_argv(args=[], check_unset_parameters=False)
    ps.read_argv(args=["-required", "0.0"])


def test_get_all():
    proto_parameter = [
        pm.ProtoParameter("a", 0.0),
        pm.ProtoParameter("b", 1.0),
        pm.ProtoParameter("c", 2.0)
    ]

    ps = pm.ParameterSet(proto_parameter)

    assert ps.get_all("a", "b", "c") == [0.0, 1.0, 2.0]
    assert ps.get_all("d", "c", "a") == [None, 2.0, 0.0]
