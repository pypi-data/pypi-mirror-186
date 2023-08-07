# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
══════════════════════════════
@Time    : 2022-12-05 14:12:16
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's types
══════════════════════════════
"""


import types
import builtins

builtins_data = builtins.__dict__.values()

# Function type.
Function = types.FunctionType

# Method type of class.
Method = types.MethodType

# All error type, include warn type.
errors = {
    obj
    for obj in builtins_data
    if type(obj) == type
        and obj != type
        and BaseException in obj.mro()
}
errors = tuple(errors)

# All warn type.
warns = (
    obj
    for obj in errors
    if Warning in obj.mro()
)
warns = tuple(warns)

# Generator type
Generator = types.GeneratorType