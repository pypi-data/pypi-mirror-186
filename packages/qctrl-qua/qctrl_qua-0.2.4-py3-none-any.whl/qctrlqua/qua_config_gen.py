# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""
Module for converting Q-CTRL optimized pulses into QUA configurations.
"""

from typing import (
    Dict,
    List,
    Optional,
    Union,
)

import numpy as np


def add_pulse_to_config(
    pulse_name: str,
    channel_name: str,
    i_signal: Union[List[float], np.ndarray],
    q_signal: Union[List[float], np.ndarray],
    config: Dict,
    intermediate_frequency: Optional[float] = None,
) -> Dict:
    """
    Add a pulse to a QUA config dictionary.

    Parameters
    ----------
    pulse_name : str
        The name of the pulse.
    channel_name : str
        The name of the channel, typically corresponding
        to a specific carrier frequency.
    i_signal : list or np.ndarray
        The I quadrature of the pulse at 1 ns sampling rate.
    q_signal : list or np.ndarray
        The Q quadrature of the pulse at 1 ns sampling rate.
    config : dict
        The main configuration dictionary,
        containing all parameters of the Operator-X (OPX).
    intermediate_frequency : float, optional
        The intermediate frequency of the channel in MHz. If provided, this
        value overrides the intermediate frequency of the `config` dictionary.
        Defaults to None, which means that the original value of the intermediary
        frequency is not modified if it's already present.

    Returns
    -------
    dict
        Updated `config` dictionary with the new pulses included.

    Raises
    ------
    ValueError
       If the maximum amplitude of I or Q of any pulse is more than 0.49.
    """

    # Copy the input config dictionary to avoid mutating it.
    config = config.copy()

    if np.max(np.abs(i_signal)) > 0.49 or np.max(np.abs(q_signal)) > 0.49:
        raise ValueError("max_amplitude must be below 0.49")
    if "version" not in config:
        config["version"] = 1
    if "controllers" not in config:
        config["controllers"] = {}
    if "digital_waveforms" not in config:
        config["digital_waveforms"] = {}
    if "integration_weights" not in config:
        config["integration_weights"] = {}
    if "mixers" not in config:
        config["mixers"] = {}
    if "waveforms" not in config:
        config["waveforms"] = {}
    if "pulses" not in config:
        config["pulses"] = {}
    if "elements" not in config:
        config["elements"] = {}
    if channel_name not in config["elements"]:
        config["elements"][channel_name] = {}
    if "operations" not in config["elements"][channel_name]:
        config["elements"][channel_name]["operations"] = {}
    if intermediate_frequency is not None:
        config["elements"][channel_name][
            "intermediate_frequency"
        ] = intermediate_frequency
    if "intermediate_frequency" not in config["elements"][channel_name]:
        config["elements"][channel_name]["intermediate_frequency"] = None

    config["waveforms"][pulse_name + "_I"] = {
        "type": "arbitrary",
        "samples": list(i_signal),
    }
    config["waveforms"][pulse_name + "_Q"] = {
        "type": "arbitrary",
        "samples": list(q_signal),
    }
    config["pulses"][pulse_name] = {
        "operation": "control",
        "length": len(i_signal),
        "waveforms": {"I": pulse_name + "_I", "Q": pulse_name + "_Q"},
    }
    config["elements"][channel_name]["operations"][pulse_name + "_op"] = pulse_name

    return config
