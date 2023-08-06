import json

import numpy as np

Signal = {
    "valence": None,
    "score": None,
    "state": None,
}

DEFAULT_STATE_DIM = 1


def get_state_as_array(signal, dtype=np.float64):
    state = signal["state"]
    if type(state) == str:
        state = json.loads(state)
    arr = np.array(state, dtype=dtype)
    signal["state"] = arr


def get_state_as_list(signal, dtype=np.float64):
    state = signal["state"]
    if type(state) == str:
        state = json.loads(state)
    arr = np.array(state, dtype=dtype)
    signal["state"] = arr.tolist()


def verify_signal(signal):
    assert type(signal) == dict
    assert len(signal) == 3

    if signal["state"] is None:
        raise Exception("signal state cannot be None")

    if type(signal["state"]) == str:
        verify_str_shape(signal["state"])

    if type(signal["state"]) == list:
        arr_list = signal["state"]
        verify_list_shape(arr_list)
        if all(isinstance(item, (int, float)) for item in arr_list):
            signal["state"] = json.dumps(arr_list)
            return
        else:
            raise Exception("signal state values must be int or float")

    if type(signal["state"]) == np.ndarray:
        try:
            arr_list = signal["state"].tolist()
            verify_list_shape(arr_list)
            signal["state"] = json.dumps(arr_list)
            return
        except Exception as e:
            raise Exception("error converting state signal from numpy array to byte string: {}".format(e))


def verify_str_shape(state):
    if state == "":
        raise Exception("signal state cannot be empty")
    state = json.loads(state)
    verify_list_shape(state)


def verify_list_shape(state, dtype=np.float64):
    arr = np.array(state, dtype=dtype)
    verify_np_shape(arr)


def verify_np_shape(state: np.ndarray):
    if state.ndim > DEFAULT_STATE_DIM:
        raise Exception("state signal should be of dimension {} got {}".format(DEFAULT_STATE_DIM, state.ndim))
