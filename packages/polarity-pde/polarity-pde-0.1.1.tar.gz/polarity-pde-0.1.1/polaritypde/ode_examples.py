import numpy as np
from scipy.integrate import odeint


class GOR:
    """
    PARAMETER SETS

    JILKINE 2011

    a1   = ?
    a2   = ?
    a3   = 0.01733
    p0   = ?


    HUBATSCH 2019

    a1   = 0.0067
    a2   = 0.0033
    a3   = 0.01
    p0   = ?

    """

    def __init__(self, a1=0.0067, a2=0.0033, a3=0.01, p0=1):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.p0 = p0

    def dxdt(self, X, t):
        U = X[0]
        V = self.p0 - X[0]
        dU = (self.a1 * (U ** 2) * V) + (self.a2 * U * V) - (self.a3 * U)
        return [dU]

    def jacobian(self, X, step=0.00001):
        U = X[0]
        V = self.p0 - X[0]
        dUdU = (self.a1 * ((U + step) ** 2) * V) + (self.a2 * (U + step) * V) - (self.a3 * (U + step))
        return dUdU / step

    # def bistability(self):
    #     """
    #     0: monostable
    #     1: bistable
    #
    #     """
    #     sol1 = odeint(self.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]
    #     sol2 = odeint(self.dxdt, [0], t=np.linspace(0, 10000, 100000))[-1]
    #
    #     # Distance measure
    #     dist = abs(sol1 - sol2)
    #
    #     if dist > 0.0001:
    #         return 1
    #     else:
    #         return 0
    #
    # def lsa(self):
    #     """
    #     0: monostable, stable
    #     1: monostable, unstable
    #     2: bistable, both stable
    #     3: bistable, sol1 unstable
    #     4: bistable, sol2 unstable
    #     5: bistable, both unstable
    #
    #     """
    #
    #     sol1 = odeint(self.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]
    #     sol2 = odeint(self.dxdt, [0], t=np.linspace(0, 10000, 100000))[-1]
    #
    #     # Distance measure
    #     dist = abs(sol1 - sol2)
    #
    #     if dist < 0.0001:
    #         # Monostable
    #         point = (sol1 + sol2) / 2
    #         dUdU = self.jacobian(point, step=0.001)
    #         if dUdU < 0:
    #             # Stable
    #             return 0
    #         else:
    #             # Unstable
    #             return 1
    #
    #     else:
    #         # Bistable
    #         dUdU1 = self.jacobian(sol1, step=0.001)
    #         dUdU2 = self.jacobian(sol2, step=0.001)
    #
    #         if dUdU1 < 0 and dUdU2 < 0:
    #             # Both stable
    #             return 2
    #         elif not dUdU1 < 0 and dUdU2 < 0:
    #             # sol1 unstable
    #             return 3
    #         elif dUdU1 < 0 and not dUdU2 < 0:
    #             # sol2 unstable
    #             return 4
    #         else:
    #             # Both unstable
    #             return 5


class OT:
    """
    PARAMETER SETS

    JILKINE 2011

    a1   = 25
    a2   = 0.7
    s    = 1
    p0   = 2


    HUBATSCH 2019

    a1   = 1
    a2   = 0.7
    s    = 1
    p0   = ?

    """

    def __init__(self, a1=1, a2=0.7, s=1, p0=2):
        self.a1 = a1
        self.a2 = a2
        self.s = s
        self.p0 = p0

    def dxdt(self, X, t):
        U = X[0]
        V = self.p0 - U
        dUdt = self.a1 * (V - (U + V) / ((self.a2 * self.s * (U + V) + 1) ** 2))
        return [dUdt]

    def jacobian(self, X, step=0.0001):
        U = X[0]
        V = self.p0 - U
        dUdU = self.a1 * (V - ((U + step) + V) / ((self.a2 * self.s * ((U + step) + V) + 1) ** 2))
        return dUdU / step

    # def bistability(self):
    #     """
    #     0: monostable
    #     1: bistable
    #
    #     """
    #     sol1 = odeint(self.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]
    #     sol2 = odeint(self.dxdt, [0], t=np.linspace(0, 10000, 100000))[-1]
    #
    #     # Distance measure
    #     dist = abs(sol1 - sol2)
    #
    #     if dist > 0.0001:
    #         return 1
    #     else:
    #         return 0
    #
    # def lsa(self):
    #     """
    #     0: monostable, stable
    #     1: monostable, unstable
    #     2: bistable, both stable
    #     3: bistable, sol1 unstable
    #     4: bistable, sol2 unstable
    #     5: bistable, both unstable
    #
    #     """
    #
    #     sol1 = odeint(self.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]
    #     sol2 = odeint(self.dxdt, [0], t=np.linspace(0, 10000, 100000))[-1]
    #
    #     # Distance measure
    #     dist = abs(sol1 - sol2)
    #
    #     if dist < 0.0001:
    #         # Monostable
    #         point = (sol1 + sol2) / 2
    #         dUdU = self.jacobian(point, step=0.001)
    #         if dUdU < 0:
    #             # Stable
    #             return 0
    #         else:
    #             # Unstable
    #             return 1
    #
    #     else:
    #         # Bistable
    #         dUdU1 = self.jacobian(sol1, step=0.001)
    #         dUdU2 = self.jacobian(sol2, step=0.001)
    #
    #         if dUdU1 < 0 and dUdU2 < 0:
    #             # Both stable
    #             return 2
    #         elif not dUdU1 < 0 and dUdU2 < 0:
    #             # sol1 unstable
    #             return 3
    #         elif dUdU1 < 0 and not dUdU2 < 0:
    #             # sol2 unstable
    #             return 4
    #         else:
    #             # Both unstable
    #             return 5


class PAR:
    def __init__(self, konA=0.00858, koffA=0.0054, konP=0.0474, koffP=0.0073, kPA=2, kAP=0.19,
                 alpha=1, beta=2, psi=0.174, pA=1.56, pP=1):
        self.konA = konA
        self.koffA = koffA
        self.konP = konP
        self.koffP = koffP
        self.alpha = alpha
        self.beta = beta
        self.psi = psi
        self.pA = pA
        self.pP = pP
        self.kAP = kAP
        self.kPA = kPA

    def dxdt(self, X, t):
        A = X[0]
        P = X[1]
        Acyt = self.pA - self.psi * A
        Pcyt = self.pP - self.psi * P
        dA = (self.konA * Acyt) - (self.koffA * A) - (self.kAP * (P ** self.alpha) * A)
        dP = (self.konP * Pcyt) - (self.koffP * P) - (self.kPA * (A ** self.beta) * P)
        return [dA, dP]

    def jacobian(self, X, step=0.0001):
        A = X[0]
        P = X[1]
        Acyt = self.pA - self.psi * A
        Pcyt = self.pP - self.psi * P
        dPdA = (self.konP * Pcyt) - (self.koffP * P) - (self.kPA * ((A + step) ** self.beta) * P)
        dAdP = (self.konA * Acyt) - (self.koffA * A) - (self.kAP * ((P + step) ** self.alpha) * A)
        dAdA = (self.konA * Acyt) - (self.koffA * (A + step)) - (self.kAP * (P ** self.alpha) * (A + step))
        dPdP = (self.konP * Pcyt) - (self.koffP * (P + step)) - (self.kPA * (A ** self.beta) * (P + step))
        return np.r_[np.c_[dAdA, dAdP], np.c_[dPdA, dPdP]] / step


class WP:
    """
    PARAMETER SETS

    MORI 2008 / JILKINE 2011 / TRONG 2014

    k0      = 0.0067
    gamma   = 1
    K       = 1
    delta   = 1
    p0      = ?


    GETZ 2018

    k0      = 0.03
    gamma   = 1
    K       = 1
    delta   = 1
    p0      = 2.8


    HUBATSCH 2019

    k0      = 0.00074
    gamma   = 0.11
    K       = 1
    delta   = 0.11
    p0      = ?

    """

    def __init__(self, k0, gamma, K, delta, p0):
        self.k0 = k0
        self.gamma = gamma
        self.K = K
        self.delta = delta
        self.p0 = p0

    def dxdt(self, X, t):
        U = X[0]
        V = self.p0 - U
        dU = V * (self.k0 + (self.gamma * (U ** 2)) / ((self.K ** 2) + (U ** 2))) - (self.delta * U)
        return [dU]

    def jacobian(self, X, step=0.0001):
        U = X[0]
        V = self.p0 - U
        dUdU = V * (self.k0 + (self.gamma * ((U + step) ** 2)) / ((self.K ** 2) + ((U + step) ** 2))) - (
                self.delta * (U + step))
        return dUdU / step

    # def bistability(self):
    #     """
    #     0: monostable
    #     1: bistable
    #
    #     """
    #     sol1 = odeint(self.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]
    #     sol2 = odeint(self.dxdt, [0], t=np.linspace(0, 10000, 100000))[-1]
    #
    #     # Distance measure
    #     dist = abs(sol1 - sol2)
    #
    #     if dist > 0.0001:
    #         return 1
    #     else:
    #         return 0
    #
    # def lsa(self):
    #     """
    #     0: monostable, stable
    #     1: monostable, unstable
    #     2: bistable, both stable
    #     3: bistable, sol1 unstable
    #     4: bistable, sol2 unstable
    #     5: bistable, both unstable
    #
    #     """
    #
    #     sol1 = odeint(self.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]
    #     sol2 = odeint(self.dxdt, [0], t=np.linspace(0, 10000, 100000))[-1]
    #
    #     # Distance measure
    #     dist = abs(sol1 - sol2)
    #
    #     if dist < 0.0001:
    #         # Monostable
    #         point = (sol1 + sol2) / 2
    #         dUdU = self.jacobian(point, step=0.001)
    #         if dUdU < 0:
    #             # Stable
    #             return 0
    #         else:
    #             # Unstable
    #             return 1
    #
    #     else:
    #         # Bistable
    #         dUdU1 = self.jacobian(sol1, step=0.001)
    #         dUdU2 = self.jacobian(sol2, step=0.001)
    #
    #         if dUdU1 < 0 and dUdU2 < 0:
    #             # Both stable
    #             return 2
    #         elif not dUdU1 < 0 and dUdU2 < 0:
    #             # sol1 unstable
    #             return 3
    #         elif dUdU1 < 0 and not dUdU2 < 0:
    #             # sol2 unstable
    #             return 4
    #         else:
    #             # Both unstable
    #             return 5
