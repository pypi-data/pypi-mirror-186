import argparse
import random

import numpy as np
import time
from six.moves import range


class ExpFilter :
    FI = 1.0
    FV = None
    reset = True

    def __init__(self, FI : float = 1.0):
        self.FV = 0.0
        self.reset = True
        self.FI = FI

    def Reset(self):
        self.reset = True

    def XtoC(self, X : float):
        if self.reset is True :
            self.FV = X
            self.reset = False

        else:
            self.FV = (self.FV * (1 - self.FI)) + ( X * self.FI)

        return self.FV

    def SetFI(self, FI : float = 1):
        self.FI = FI

class Dahlin :
    G = 1.0
    TC = 30
    LAMBDA = 1
    Em1 = 0.0
    now = time.time()
    then = now
    reset = True
    T = 0.0

    def __init__(self, TC: float = 15.0, LAMBDA : float = .1, GAIN : float = 1):
        self.G = GAIN
        self.TC = TC
        self.LAMBDA = LAMBDA
        self.Em1 = 0.0
        self.now = time.time()
        self.then = self.now
        self.reset = True

    def Reset(self):
        self.Em1 = 0.0
        self.reset = True


    def XtoC(self, X : float ):
        self.now = time.time()

        if self.reset is True :
            self.then = self.now
            self.reset = False

        seconds = self.now - self.then
        print("Seconds", seconds)
        if seconds == 0:
            T = float(.0001)
        else:
            T = float(seconds)

        self.then = self.now

        L = 1 - np.exp(-T / self.TC)
        Q = 1 - np.exp(-self.LAMBDA * T)
        K = Q / (L * self.G)
        En = X
        X = K * ( En - (1-L) * self.Em1)
        self.Em1 = En
        return X

    def Time(self):
        return self.now



def twiddle(evaluator, tol=0.001, params=3, error_cmp=None, initial_guess=None):
    """
    A coordinate descent parameter tuning algorithm.

    https://en.wikipedia.org/wiki/Coordinate_descent

    Params:

        evaluator := callable that will be passed a series of number parameters, which will return
            an error measure

        tol := tolerance threshold, the smaller the value, the greater the tuning

        params := the number of parameters to tune

        error_cmp := a callable that takes two error measures (the current and last best)
            and returns true if the first is less than the second

        initial_guess := parameters to begin tuning with
    """

    def _error_cmp(a, b):
        # Returns true if a is closer to zero than b.
        return abs(a) < abs(b)

    if error_cmp is None:
        error_cmp = _error_cmp

    if initial_guess is None:
        p = [0] * params
    else:
        p = list(initial_guess)
    dp = [1] * params
    best_err = evaluator(*p)
    steps = 0
    while sum(dp) > tol:
        steps += 1
        print('steps:', steps, 'tol:', tol, 'best error:', best_err)
        for i, _ in enumerate(p):

            # first try to increase param
            p[i] += dp[i]
            err = evaluator(*p)

            if error_cmp(err, best_err):
                # Increasing param reduced error, so record and continue to increase dp range.
                best_err = err
                dp[i] *= 1.1
            else:
                # Otherwise, increased error, so undo and try decreasing dp
                p[i] -= 2. * dp[i]
                err = evaluator(*p)

                if error_cmp(err, best_err):
                    # Decreasing param reduced error, so record and continue to increase dp range.
                    best_err = err
                    dp[i] *= 1.1

                else:
                    # Otherwise, reset param and reduce dp range.
                    p[i] += dp[i]
                    dp[i] *= 0.9

    return p


class PID(object):
    """
    Simple PID control.
    """

    def __init__(self, p=0, i=0, d=0, **kwargs):

        self._get_time = kwargs.pop('get_time', None) or time.time

        # initialze gains
        self.Kp = p
        self.Ki = i
        self.Kd = d

        # The value the controller is trying to get the system to achieve.
        self._target = 0

        # initialize delta t variables
        self._prev_tm = self._get_time()

        self._prev_feedback = 0

        self._error = None

    def reset(self):
        # initialize delta t variables
        self._prev_tm = self._get_time()

        self._prev_feedback = 0

        self._error = None

    @property
    def error(self):
        return self._error

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, v):
        self._target = float(v)

    def __call__(self, feedback, curr_tm=None):
        """ Performs a PID computation and returns a control value.

            This is based on the elapsed time (dt) and the current value of the process variable
            (i.e. the thing we're measuring and trying to change).

        """

        # Calculate error.
        error = self._error = self._target - feedback

        # Calculate time differential.
        if curr_tm is None:
            curr_tm = self._get_time()
        dt = curr_tm - self._prev_tm

        # Initialize output variable.
        alpha = 0

        # Add proportional component.
        alpha -= self.Kp * error

        # Add integral component.
        alpha -= self.Ki * (error * dt)

        # Add differential component (avoiding divide-by-zero).
        if dt > 0:
            alpha -= self.Kd * ((feedback - self._prev_feedback) / float(dt))

        # Maintain memory for next loop.
        self._prev_tm = curr_tm
        self._prev_feedback = feedback
        return alpha


class ComputerSL:

    def __init__(self, X1,X2, Y1,Y2):
        self.s = (Y2 - Y1) / (X2 - X1)
        self.i =  Y1 - (self.s * X1)

    def Y(self, X):
        c = (X * self.s) + self.i
        return c

    def X(self, Y):
        c = None
        if self.s != 0.0 :
            c = (Y -self.i) / self.s

        return c


class HistoryDelay :
    """
    This is a history array, it will work with either number storage IE steps, or if tau is not None, then it will work off of Tau
    It is meant as to not store more than necessary if tau is given.. if steps are used, then storage will be in steps and the use must ensure
    then number of steps is suffecient to store what is needed.
    No Block rate is needed, this works of actual seconds.
    """
    history = []
    historyLimit = 40
    tau = None

    def __init__(self, steps : int = 40, tau : float = None):
        self.historyLimit = 40
        self.history = []
        self.tau = tau

    def Insert(self, v):
        tm = time.time()
        pair = (tm,v)
        self.history.insert(0,pair)
        if self.tau is None :
            if len(self.history) > self.historyLimit :
                self.history.pop(len(self.history) -1 )
        else:
            for i1 in  range(0, len(self.history)) :
                tm1, v1 = self.history[i1]
                df1 = tm - tm1
                if df1 > self.tau :
                    i2 = i1 + 1
                    if i2 < len(self.history) :
                        del self.history[len(self.history) - i2 : ]
                    return


    def ComputeSumToPosition(self, seconds,  multi : float = 1):
        sum = 0.0
        tm = time.time()
        for i in range(0, len(self.history)) :

            t, v = self.history[i]
            df = tm - t

            if df <= seconds :
                sum = sum + (v * multi)

            else:
                if i >= 1 :

                    t1, v1 = self.history[i - 1]

                    df2 = df
                    df1 = tm - t1

                    nv  = ComputerSL(df1,df2,v,v1)
                    computedV = nv.Y(seconds)
                    sum = sum + ( computedV * multi)
                    return sum

        return sum

    def ComputeListToPosition(self, seconds, Q : float =  1):
        tm = time.time()
        sum = 0.0

        lastT = 0.0
        N = 0

        for i in range(0, len(self.history)):

            t, v = self.history[i]
            df = tm - t

            N = i
            if df <= seconds:
                lastT = v * Q
                sum = sum + lastT


            else:
                if i >= 1:
                    t1, v1 = self.history[i - 1]

                    df2 = df
                    df1 = tm - t1
                    nv = ComputerSL(df1, df2, v, v1)
                    computedV = nv.Y(seconds)
                    lastT =  ( computedV * Q)
                    return sum, lastT, i

        return sum, lastT, N

import operator
class  F25 (HistoryDelay) :
    G = None
    TC = None
    LAMBDA = None
    TAU = None
    TC = None

    e_m_1 = 0.0
    y_m_1 = 0.0
    lastTime = None

    def __init__(self, G : float,  LAMBDA : float, TC : float, TAU : float,  steps: int = 40):
        super().__init__(steps, (TC + TAU))
        self.G = G
        self.TC = TC
        self.LAMBDA = LAMBDA
        self.TAU = TAU
        self.e_m_1 = 0.0
        self.y_m_1 = 0.0
        self.lastTime = None

    def Control(self, value : float ):
        if self.lastTime is None :
            self.lastTime = time.time()

        nowTime = time.time()

        dfTime = nowTime - self.lastTime
        self.lastTime = nowTime
        if dfTime == 0:
            T = float(.0001)
        else:
            T = float(dfTime)

        M = self.TAU / T

        Q = 1 - np.exp(-self.LAMBDA * T)
        L = 1 - np.exp(-T / self.TC)
        K = Q / (L * self.G)

        APrime = -(1 - L)
        SMY, YNEM1, N  = self.ComputeListToPosition( self.TAU, -Q)
        Y = YNEM1 * (-M*Q) + SMY + K * ( value + APrime * self.e_m_1)
        self.e_m_1 = value
        self.Insert(Y)
        return Y


    def Reset(self):
        self.lastTime = None
        self.e_m_1 = 0.0
        self.y_m_1 = 0.0



from stdcomQt.arguments import arguments

class MapToZones() :

    edge_allow_0 = True
    middle_allow_0 = False
    start_s = int(1)
    end_s =  int(20)
    left_s = int(1)
    right_s = int(20)
    offset = float(0)
    total_s_width = float(100)
    min_d_width = float(6)
    d_count = int(10)

    THRESHOLD = float(.0000001)
    MAXVAL = float(1.0E38)

    def __init__(self, args):
        a = arguments(args)
        self.edge_allow_0 = bool (a.getDefault("edge_allow_0", self.edge_allow_0))
        self.middle_allow_0 = bool(a.getDefault("middle_allow_0", self.middle_allow_0))
        self.start_s = float(a.getDefault("start_s", self.start_s ))
        self.end_s = float(a.getDefault("end_s", self.end_s ))
        self.left_s  = float(a.getDefault("left_s", self.left_s ))
        self.right_s = float(a.getDefault("right_s",self.right_s))
        self.offset =  float(a.getDefault("offset", self.offset))
        self.total_s_width = float(a.getDefault("total_s_width", self.total_s_width))
        self.min_d_width = float(a.getDefault("min_d_width", self.min_d_width ))
        self.d_count = int (a.getDefault("d_count", self.d_count))

    def CheckBound(self, left, right, start, end, invert):
        if invert == 1:
            left += self.THRESHOLD
            right -= self.THRESHOLD
        else:
            left -= self.THRESHOLD
            right += self.THRESHOLD
        if left <= start:  # out on start side
            if right >= (end + 1):  # & on end side */
                return 5
            elif right <= start:
                return 3  # completely out on start side */
            else:
                return 1  # partially out on start side */
        elif left >= (end + 1):  # out on end side */
            if right <= start:  # & on start side */
                return 5
            elif right >= (end + 1):
                return 4  # completely out on end side */
            else:
                return 2  # partially out on end side */
        else:
            if right <= start:
                return 1  # partially out on start side */
            elif right >= (end + 1):
                return 2  # partially out on end side */
            else:
                return 0  # in bounds */

    def ZeroCheck(self, src):
        data = []
        for x in range(0, len(src)):
            if (src[x] < 0.0):
                src[x] = 0.0
        return src

    def Control(self, src):
        self.inv = 1

        self.num_s = abs(self.end_s - self.start_s) + 1

        if (self.left_s > self.right_s):
            self.inv = -1

        interm = abs(self.right_s - self.left_s)
        interm += 1
        self.s_width = self.total_s_width / interm
        self.step = self.inv * self.min_d_width / self.s_width
        self.right_edge = self.left_s + self.inv * (self.offset / self.s_width)
        if self.inv == -1:
            self.right_edge += 1.

        dest = [0.0] * self.d_count

        right = left = 0
        src = self.ZeroCheck(src)
        s = 0
        lcstart_s = self.start_s
        for x in range(0, len(src)):
            if (src[x] > 0):
                break
            s += 1
            lcstart_s += 1

        s -= lcstart_s

        lcend_s = self.end_s

        p =  s + lcend_s


        while src[int(p)] <= 0.0:
            lcend_s -= 1
            p -= 1

        right_edge = self.right_edge
        left_edge = right_edge

        for x in range(0, self.d_count):
            left_edge = right_edge  # next d in s space * /
            right_edge += self.step

            bounds = self.CheckBound(left_edge, right_edge, lcstart_s, lcend_s, self.inv)

            if bounds == 0:  # completely in bounds
                left = left_edge
                right = right_edge

            elif bounds == 1:  # partially out on start side
                if self.inv == 1:
                    left = lcstart_s
                    right = right_edge
                else:
                    left = left_edge
                    right = lcstart_s

            elif bounds == 2:  # partially out on end side
                if self.inv == 1:
                    left = left_edge
                    right = lcend_s + 1
                else:
                    left = lcend_s + 1
                    right = right_edge

            elif bounds == 3:  # completely out on start side
                left = lcstart_s
                right = lcstart_s + 1

            elif bounds == 4:  # completely out on end side
                left = lcend_s
                right = lcend_s + 1

            elif bounds == 5:  # completely out of bounds
                left = lcstart_s
                right = lcend_s + 1

            if left > right:  # inverted so right edge is less than left
                temp = left  # swap to do summation * /
                left = right
                right = temp

            j = int(left)
            k = int(right)
            min = self.MAXVAL
            max = 0.0
            sum = 0.0
            divisor = abs(right - left)

            if src[j] <= 0.:
                divisor -= (j + 1 - left)  # reduce divisor by width of this partial s elem * /

            else:
                value = src[ int(j + s)]  # sum or max / min an edge * /
                sum += (j + 1 - left) * value
            # .....................................................................

            if (j == k):  # d lies completely within a single s * /
                divisor = (k + 1) - left
            else:
                value = src[ int(k + s)]

                if src[ int(k)] <= 0.:
                    divisor -= (right - k)  # reduce divisor by width of this partial s elem * /

                else:  # sum or max a partial edge * /
                    sum += (right - k) * value

                m = j + 1

                for m in range(j + 1, k):
                    if (src[ int(m)] <= 0.):
                        divisor -= 1.

                    else:
                        sum += src[int(m)]
            if bounds == 3 or bounds == 4:
                dest[int(x)] = 0.

            else:
                if divisor > self.THRESHOLD and sum > 0.:  # check valid divisor * /
                    dest[int(x)] = sum / divisor  # * new  average in d * /
                else:
                    dest[int(x)] = dest[int(x - 1)]  # use the adjacent value

        return dest


if __name__ == '__main__':

    databoxes = [ 1,2,3,4,5,6,7,8,9,10]
    parameters= [ "start_s=1", "end_s=10", "left_s=1", "right_s=10", "offset=3", "total_s_width=120", "min_d_width=2", "d_count=40"  ]

    mapclass = MapToZones(parameters)

    key = mapclass.Control(databoxes)
    for i, item in enumerate(key, start=1):
        print(i, item)



    sleepTime = 5.0
    f25 = F25( -1, .018, 1, 40, 40)
    spt = 0
    value = 40
    hl = [0] * 9
    T1 = []
    Q1 = []
    t = []
    for i in range(0,50):
        v = f25.Control(value)
        hl.insert(0,v)
        hl.pop(len(hl) - 1)
        value = value + hl[len(hl) - 1]
        print(i, ":" ,v,":", value)
        time.sleep(sleepTime)
        t.append(i * sleepTime)
        T1.append(value)
        Q1.append(v)

    import matplotlib.pyplot as plt
    import pandas as pd

    n = 50
    tm = np.linspace(0, n - 1, n)
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.grid()
    plt.plot([0, tm[-1] / 60.0], [50, 50], 'k-', label=r'$T_1$ SP')
    plt.plot(t, T1, 'r.', label=r'$T_1$ PV')
    plt.ylabel(r'Eng Value ($^oC$)')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.grid()
    plt.plot(t, Q1, 'b-', label=r'$Q_1$')
    plt.ylabel(r'Actuator (%)');
    plt.xlabel('Time (Seconds)')
    plt.legend()
    plt.show()


