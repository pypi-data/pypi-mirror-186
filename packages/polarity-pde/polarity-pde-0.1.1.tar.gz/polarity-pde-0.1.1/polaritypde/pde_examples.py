import numpy as np
from .pdeRK import pdeRK
from scipy.integrate import odeint
import ode_examples as ode


def diffusion(concs, dx):
    concs_ = np.r_[concs[0], concs, concs[-1]]  # Dirichlet boundary conditions
    d = concs_[:-2] - 2 * concs_[1:-1] + concs_[2:]
    return d / (dx ** 2)


class GOR:
    def __init__(self, D, a1, a2, a3, p0, xsteps=100, Tmax=1000, deltat=0.01, deltax=0.1):
        # Species
        self.U = np.zeros([int(xsteps)])
        self.time = 0

        # Diffusion
        self.D = D

        # Dosage
        self.p0 = p0

        # Membrane exchange
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

        # Misc
        self.xsteps = int(xsteps)
        self.Tmax = Tmax  # s
        self.deltat = deltat  # s
        self.deltax = deltax  # um

    def dxdt(self, X):
        U = X[0]
        V = self.p0 - np.mean(U)
        dUdt = (self.a1 * (U ** 2) * V) + (self.a2 * U * V) - (self.a3 * U) + (self.D * diffusion(U, self.deltax))
        return [dUdt]

    def initiate(self):
        # Initial equilibration
        Tmax = self.Tmax / 10
        soln, time, solns, times = pdeRK(dxdt=self.dxdt, X0=[self.U], Tmax=Tmax, deltat=self.deltat,
                                         t_eval=np.arange(0, Tmax + 0.0001, Tmax))
        self.U = soln[0]

        # Polarise
        self.U *= 2 * np.r_[np.zeros([self.xsteps // 2]), np.ones([self.xsteps // 2])]

    def run(self, save_gap=None):
        if save_gap is None:
            save_gap = self.Tmax

        # Run
        soln, time, solns, times = pdeRK(dxdt=self.dxdt, X0=[self.U], Tmax=self.Tmax, deltat=self.deltat,
                                         t_eval=np.arange(0, self.Tmax + 0.0001, save_gap))
        self.U = soln[0]

        return soln, time, solns, times


class OT:
    def __init__(self, D=0.1, a1=1, a2=0.7, s=1, p0=10, xsteps=100, Tmax=1000, deltat=0.01, deltax=0.1):
        # Species
        self.U = np.zeros([int(xsteps)])
        self.time = 0

        # Diffusion
        self.D = D

        # Dosage
        self.p0 = p0

        # Membrane exchange
        self.a1 = a1
        self.a2 = a2
        self.s = s

        # Misc
        self.xsteps = int(xsteps)
        self.Tmax = Tmax  # s
        self.deltat = deltat  # s
        self.deltax = deltax  # um

    def dxdt(self, X):
        U = X[0]
        V = self.p0 - np.mean(U)
        dUdt = self.a1 * (V - (U + V) / ((self.a2 * self.s * (U + V) + 1) ** 2)) + (self.D * diffusion(U, self.deltax))
        return [dUdt]

    def initiate(self):
        # Solve ODE, high state
        o = ode.OT(a1=self.a1, a2=self.a2, s=self.s, p0=self.p0)
        soln = odeint(o.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]

        # Polarise
        self.U = 2 * np.r_[np.zeros([self.xsteps // 2]), soln * np.ones([self.xsteps // 2])]

    def initiate2(self):
        # Solve ODE, high state
        o = ode.OT(a1=self.a1, a2=self.a2, s=self.s, p0=self.p0)
        soln = odeint(o.dxdt, [self.p0], t=np.linspace(0, 10000, 100000))[-1]

        # Polarise
        self.U = soln * np.r_[0.99 * np.ones([self.xsteps // 2]), 1.01 * np.ones([self.xsteps // 2])]

    def run(self, save_gap=None):
        if save_gap is None:
            save_gap = self.Tmax

        # Run
        soln, time, solns, times = pdeRK(dxdt=self.dxdt, X0=[self.U], Tmax=self.Tmax, deltat=self.deltat,
                                         t_eval=np.arange(0, self.Tmax + 0.0001, save_gap))
        self.U = soln[0]

        return soln, time, solns, times


class PAR:
    def __init__(self, Da=0.28, Dp=0.15, konA=0.00858, koffA=0.0054, konP=0.0474, koffP=0.0073, kPA=2, kAP=0.19,
                 alpha=1, beta=2, xsteps=100, psi=0.174, Tmax=1000, deltat=0.01, L=134.6, pA=1.56, pP=1):
        # Species
        self.A = np.zeros([int(xsteps)])
        self.P = np.zeros([int(xsteps)])
        self.time = 0

        # Dosages
        self.pA = pA
        self.pP = pP

        # Diffusion
        self.Da = Da  # input is um2 s-1
        self.Dp = Dp  # um2 s-1

        # Membrane exchange
        self.konA = konA  # um s-1
        self.koffA = koffA  # s-1
        self.konP = konP  # um s-1
        self.koffP = koffP  # s-1

        # Antagonism
        self.kPA = kPA  # um4 s-1
        self.kAP = kAP  # um2 s-1
        self.alpha = alpha
        self.beta = beta

        # Misc
        self.L = L
        self.xsteps = int(xsteps)
        self.Tmax = Tmax  # s
        self.deltat = deltat  # s
        self.deltax = self.L / xsteps  # um
        self.psi = psi  # um-1

    def dxdt(self, X):
        A = X[0]
        P = X[1]
        ac = self.pA - self.psi * np.mean(A)
        pc = self.pP - self.psi * np.mean(P)
        dA = ((self.konA * ac) - (self.koffA * A) - (self.kAP * (P ** self.alpha) * A) + (
                self.Da * diffusion(A, self.deltax)))
        dP = ((self.konP * pc) - (self.koffP * P) - (self.kPA * (A ** self.beta) * P) + (
                self.Dp * diffusion(P, self.deltax)))
        return [dA, dP]

    def initiate(self):
        """
        Initiating the system polarised

        """

        # Solve ode, no antagonism
        o = ode.PAR(konA=self.konA, koffA=self.koffA, konP=self.konP, koffP=self.koffP, alpha=self.alpha,
                    beta=self.beta,
                    psi=self.psi, pA=self.pA, pP=self.pP, kAP=0, kPA=0)
        soln = odeint(o.dxdt, (0, 0), t=np.linspace(0, 10000, 100000))[-1]

        self.A = soln[0]
        self.P = soln[1]

        # Polarise
        self.A *= 2 * np.r_[np.ones([self.xsteps // 2]), np.zeros([self.xsteps // 2])]
        self.P *= 2 * np.r_[np.zeros([self.xsteps // 2]), np.ones([self.xsteps // 2])]

    def run(self, save_gap=None, kill_uni=False, kill_stab=False):
        """

        :param save_gap: gap in model time between save points
        :param kill_uni: terminate once polarity is lost. Generally can assume models never regain polarity once lost
        :param kill_stab: terminate when patterns are stable. I'd advise against for phase-space diagrams, can get
            fuzzy boundaries
        :return:
        """
        if save_gap is None:
            save_gap = self.Tmax

        # Kill when uniform
        if kill_uni:
            def killfunc(X):
                if sum(X[0] > X[1]) == len(X[0]) or sum(X[0] > X[1]) == 0:
                    return True
                return False
        else:
            killfunc = None

        # Run
        soln, time, solns, times = pdeRK(dxdt=self.dxdt, X0=[self.A, self.P], Tmax=self.Tmax, deltat=self.deltat,
                                         t_eval=np.arange(0, self.Tmax + 0.0001, save_gap), killfunc=killfunc,
                                         stabilitycheck=kill_stab)
        self.A = soln[0]
        self.P = soln[1]

        return soln, time, solns, times


class PARflow:
    def __init__(self, Da=0.28, Dp=0.15, konA=0.00858, koffA=0.0054, konP=0.0474, koffP=0.0073, kPA=2, kAP=0.19,
                 alpha=1, beta=2, xsteps=100, psi=0.174, Tmax=1000, deltat=0.01, L=134.6, pA=1.56, pP=1, v=0):
        # Species
        self.A = np.zeros([int(xsteps)])
        self.P = np.zeros([int(xsteps)])
        self.time = 0

        # Dosages
        self.pA = pA
        self.pP = pP

        # Diffusion
        self.Da = Da  # input is um2 s-1
        self.Dp = Dp  # um2 s-1

        # Flow
        self.v = v

        # Membrane exchange
        self.konA = konA  # um s-1
        self.koffA = koffA  # s-1
        self.konP = konP  # um s-1
        self.koffP = koffP  # s-1

        # Antagonism
        self.kPA = kPA  # um4 s-1
        self.kAP = kAP  # um2 s-1
        self.alpha = alpha
        self.beta = beta

        # Misc
        self.L = L
        self.xsteps = int(xsteps)
        self.Tmax = Tmax  # s
        self.deltat = deltat  # s
        self.deltax = self.L / xsteps  # um
        self.psi = psi  # um-1

    def flow(self, concs):
        """
        Rough generic flow profile, not completely accurate

        """

        # v = np.arange(self.xsteps) / self.xsteps
        x = np.array(range(self.xsteps)) * (100 / self.xsteps)
        v = (x / np.exp(0.00075 * (x ** 2)))[::-1]
        v /= max(v)
        v[0] = 0
        return - np.diff(np.r_[concs, concs[-1]] * np.r_[v, 0])

    def dxdt(self, X):
        A = X[0]
        P = X[1]
        ac = self.pA - self.psi * np.mean(A)
        pc = self.pP - self.psi * np.mean(P)
        dA = ((self.konA * ac) - (self.koffA * A) - (self.kAP * (P ** self.alpha) * A) + (
                self.Da * diffusion(A, self.deltax)) - (self.v / self.deltax) * self.flow(A))
        dP = ((self.konP * pc) - (self.koffP * P) - (self.kPA * (A ** self.beta) * P) + (
                self.Dp * diffusion(P, self.deltax)))
        return [dA, dP]

    def initiate(self):
        """
        Initiating the system polarised

        """

        # Solve ode, no antagonism
        o = ode.PAR(konA=self.konA, koffA=self.koffA, konP=self.konP, koffP=self.koffP, alpha=self.alpha,
                    beta=self.beta,
                    psi=self.psi, pA=self.pA, pP=self.pP, kAP=0, kPA=0)
        soln = odeint(o.dxdt, (0, 0), t=np.linspace(0, 10000, 100000))[-1]

        self.A = soln[0]
        self.P = soln[1]

        # Polarise
        self.A *= 2 * np.r_[np.ones([self.xsteps // 2]), np.zeros([self.xsteps // 2])]
        self.P *= 2 * np.r_[np.zeros([self.xsteps // 2]), np.ones([self.xsteps // 2])]

    def initiate2(self):
        """
        Initiating the system (near) uniform, A dominant

        """

        # Solve ode
        o = ode.PAR(konA=self.konA, koffA=self.koffA, konP=self.konP, koffP=self.koffP, alpha=self.alpha,
                    beta=self.beta,
                    psi=self.psi, pA=self.pA, pP=self.pP, kAP=0, kPA=0)
        soln = odeint(o.dxdt, (o.pA / o.psi, 0), t=np.linspace(0, 10000, 100000))[-1]

        # Set concentrations
        self.A[:] = soln[0]
        self.P[:] = soln[1]

        # Polarise
        self.A *= np.linspace(1.01, 0.99, self.xsteps)
        self.P *= np.linspace(0.99, 1.01, self.xsteps)

    def run(self, save_gap=None, kill_uni=False, kill_stab=False):
        """
        :param save_gap: gap in model time between save points
        :param kill_uni: terminate once polarity is lost. Generally can assume models never regain polarity once lost
        :param kill_stab: terminate when patterns are stable. I'd advise against for phase-space diagrams, can get
            fuzzy boundaries
        :return:
        """
        if save_gap is None:
            save_gap = self.Tmax

        # Kill when uniform
        if kill_uni:
            def killfunc(X):
                if sum(X[0] > X[1]) == len(X[0]) or sum(X[0] > X[1]) == 0:
                    return True
                return False
        else:
            killfunc = None

        # Run
        soln, time, solns, times = pdeRK(dxdt=self.dxdt, X0=[self.A, self.P], Tmax=self.Tmax, deltat=self.deltat,
                                         t_eval=np.arange(0, self.Tmax + 0.0001, save_gap), killfunc=killfunc,
                                         stabilitycheck=kill_stab)
        self.A = soln[0]
        self.P = soln[1]

        return soln, time, solns, times


class WP:
    def __init__(self, D=0.1, k0=0.067, gamma=1, K=1, delta=1, p0=2.3, xsteps=100, Tmax=1000, deltat=0.01, deltax=0.1):
        # Species
        self.U = np.zeros([int(xsteps)])
        self.time = 0

        # Diffusion
        self.D = D

        # Dosage
        self.p0 = p0

        # Membrane exchange
        self.k0 = k0
        self.gamma = gamma
        self.K = K
        self.delta = delta

        # Misc
        self.xsteps = int(xsteps)
        self.Tmax = Tmax  # s
        self.deltat = deltat  # s
        self.deltax = deltax  # um

    def dxdt(self, X):
        U = X[0]
        V = self.p0 - np.mean(U)
        dU = V * (self.k0 + (self.gamma * (U ** 2)) / ((self.K ** 2) + (U ** 2))) - (self.delta * U) + (
                self.D * diffusion(U, self.deltax))
        return [dU]

    def initiate(self):
        # Initial equilibration
        Tmax = self.Tmax / 10
        soln, time, solns, times = pdeRK(dxdt=self.dxdt, X0=[self.U], Tmax=Tmax, deltat=self.deltat,
                                         t_eval=np.arange(0, Tmax + 0.0001, Tmax))
        self.U = soln[0]

        # Polarise
        self.U *= 2 * np.r_[np.zeros([self.xsteps // 2]), np.ones([self.xsteps // 2])]

    def run(self, save_gap=None):
        if save_gap is None:
            save_gap = self.Tmax

        # Run
        soln, time, solns, times = pdeRK(dxdt=self.dxdt, X0=[self.U], Tmax=self.Tmax, deltat=self.deltat,
                                         t_eval=np.arange(0, self.Tmax + 0.0001, save_gap))
        self.U = soln[0]

        return soln, time, solns, times
