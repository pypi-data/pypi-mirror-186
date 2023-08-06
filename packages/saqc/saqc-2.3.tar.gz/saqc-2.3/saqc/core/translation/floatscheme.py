#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from dios.dios.dios import DictOfSeries
from saqc.constants import UNFLAGGED
from saqc.core.flags import Flags
from saqc.core.translation.basescheme import MappingScheme


class FloatScheme(MappingScheme):

    """
    Acts as the default Translator, provides a changeable subset of the
    internal float flags
    """

    _MAP: dict[float, float] = {
        -np.inf: -np.inf,
        **{k: k for k in np.arange(0, 256, dtype=float)},
    }

    def __init__(self):
        super().__init__(self._MAP, self._MAP)


class AnnotatedFloatScheme(FloatScheme):
    def toExternal(self, flags: Flags, **kwargs):
        tflags = super().toExternal(flags, raw=True)

        out = DictOfSeries()

        for field in tflags.columns:
            df = pd.DataFrame(
                {
                    "flag": tflags[field],
                    "func": "",
                }
            )

            history = flags.history[field]
            for col in history.columns:
                valid = (history.hist[col] != UNFLAGGED) & history.hist[col].notna()

                # extract from meta
                meta = history.meta[col]
                f = meta["func"]
                args = ", ".join(map(str, meta["args"]))
                kwargs = ", ".join(f"{k}={v}" for k, v in meta["kwargs"].items())
                df.loc[valid, "func"] = f"{f}({','.join(filter(None, [args, kwargs]))})"
                out[field] = df

        return out
