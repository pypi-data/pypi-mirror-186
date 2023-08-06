import numpy as np
from avenieca.utils import verify_signal, get_state_as_list, get_state_as_array


def test_get_state_as_array():
    signal = {
        "valence": None,
        "score": None,
        "state": "[9.1, 2.1, 0.3]"
    }
    get_state_as_array(signal)
    assert True, np.array_equal(signal["state"], np.array([9.1, 2.1, 0.3]))

    signal = {
        "valence": None,
        "score": None,
        "state": [9.1, 2.1, 0.3]
    }
    get_state_as_array(signal)
    assert True, np.array_equal(signal["state"], np.array([9.1, 2.1, 0.3]))


def test_get_state_as_list():
    signal = {
        "valence": None,
        "score": None,
        "state": "[9.1, 2.1, 0.3]"
    }
    get_state_as_list(signal)
    assert signal["state"] == [9.1, 2.1, 0.3]

    signal = {
        "valence": None,
        "score": None,
        "state": np.array([9.1, 2.1, 0.3])
    }
    get_state_as_list(signal)
    assert signal["state"] == [9.1, 2.1, 0.3]


def test_verify_signal():
    signal = {
        "valence": None,
        "score": None,
        "state": "[9.1, 2.1, 0.3]"
    }
    verify_signal(signal)
    assert signal["state"] == "[9.1, 2.1, 0.3]"

    signal = {
        "valence": None,
        "score": None,
        "state": np.array([9.1, 2.1, 0.3])
    }
    verify_signal(signal)
    assert signal["state"] == "[9.1, 2.1, 0.3]"

    signal = {
        "valence": None,
        "score": None,
        "state": [9.1, 2.1, 0.3]
    }
    verify_signal(signal)
    assert signal["state"] == "[9.1, 2.1, 0.3]"
