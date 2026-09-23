# SPDX-FileCopyrightText: 2025-present Sean Enderby <sean.enderby@gmail.com>
#
# SPDX-License-Identifier: MIT

class DesignType:
    pass

class RBIBDType(DesignType):
    def __init__(self, v: int, k: int, lambd: int=1):
        self._v = v
        self._k = k
        self._lambd = lambd

    def __repr__(self):
        if self._lambd == 1:
            return f"({self._v}, {self._k})-RBIBD"

        return f"({self._v}, {self._k}, {self._lambd})-RBIBD"

class RGDDType(DesignType):
    def __init__(self, k: int, g: int, n: int, lambd: int=1):
        self._k = k
        self._g = g
        self._n = n
        self._lambd = lambd

    def __repr__(self):
        if self._lambd == 1:
            return f"{self._k}-RGDD of type {self._g}^{self._n}"

        return f"({self._k}, {self._lambd})-RGDD of type {self._g}^{self._n}"

class RTDType(DesignType):
    def __init__(self, k: int, n: int, lambd: int=1):
        self._k = k
        self._n = n
        self._lambd = lambd

    def __repr__(self):
        if self._lambd == 1:
            return f"RTD({self._k}, {self._n})"

        return f"RTD_{self._lambd}({self._k}, {self._n})"

class RITDType(DesignType):
    def __init__(self, k: int, n: int, h: int, lambd: int=1):
        self._k = k
        self._n = n
        self._h = h
        self._lambd = lambd

    def __repr__(self):
        if self._lambd == 1:
            return f"RITD({self._k}, {self._n}, {self._h})"

        return f"RITD_{self._lambd}({self._k}, {self._n}, {self._h})"

class PartialType(DesignType):
    def __init__(self):
        pass

    def __repr__(self):
        return "Partial Design"
