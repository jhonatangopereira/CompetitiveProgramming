def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
      return 0

    A = area (x1, y1, x2, y2, x3, y3)
    A1p = area (xp, yp, x2, y2, x3, y3)
    A2p = area (x1, y1, xp, yp, x3, y3)
    A3p = area (x1, y1, x2, y2, xp, yp)
    A1q = area (xq, yq, x2, y2, x3, y3)
    A2q = area (x1, y1, xq, yq, x3, y3)
    A3q = area (x1, y1, x2, y2, xq, yq)

    if (A == A1p + A2p + A3p and A != A1q + A2q + A3q):
        return 1
    if (A != A1p + A2p + A3p and A == A1q + A2q + A3q):
        return 2
    if (A == A1p + A2p + A3p and A == A1q + A2q + A3q):
        return 3
    return 4
