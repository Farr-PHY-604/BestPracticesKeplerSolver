from pylab import *

def E_from_t(t, P, e, tol=1e-8):
    """Returns the eccentric anomaly given a time, period and eccentricity.

    :param t: The time.

    :param P: The period.

    :param e: The eccentricity.

    :param tol: (Optional; default 1e-8).  Accuracy to which E will be determined.

    :return: The eccentric anomaly.
    """

    assert e >= 0
    assert e < 1

    assert P > 0

    # Mean anomaly
    M = 2*pi*t/P

    # Kepler's equation
    def f(E):
        return E - e*sin(E) - M

    E0 = 0
    E1 = 2*pi

    F0 = f(E0)
    F1 = f(E1)

    while E1 > E0 + tol:
        EM = 0.5*(E0 + E1)
        FM = f(EM)

        if F0*FM > 0: # Check if F0 and Fm are same sign
            E0 = EM
            F0 = FM
        else:
            E1 = EM
            F1 = FM

    return EM
