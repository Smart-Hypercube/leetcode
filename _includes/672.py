def r1(l):
    l = l[:]
    try:
        l[0] = not l[0]
        l[1] = not l[1]
        l[2] = not l[2]
        l[3] = not l[3]
    except:
        pass
    return l

def r2(l):
    l = l[:]
    try:
        l[1] = not l[1]
        l[3] = not l[3]
    except:
        pass
    return l

def r3(l):
    l = l[:]
    try:
        l[0] = not l[0]
        l[2] = not l[2]
    except:
        pass
    return l

def r4(l):
    l = l[:]
    try:
        l[0] = not l[0]
        l[3] = not l[3]
    except:
        pass
    return l

class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        lights = [True, True, True, True][:n]
        s = set()
        if m%2 == 0:
            s.add(tuple(lights))
            if m >= 2:
                s.add(tuple(r2(r1(lights))))
                s.add(tuple(r3(r1(lights))))
                s.add(tuple(r4(r1(lights))))
                s.add(tuple(r3(r2(lights))))
                s.add(tuple(r4(r2(lights))))
                s.add(tuple(r4(r3(lights))))
                if m >= 4:
                    s.add(tuple(r4(r3(r2(r1(lights))))))
        else:
            s.add(tuple(r1(lights)))
            s.add(tuple(r2(lights)))
            s.add(tuple(r3(lights)))
            s.add(tuple(r4(lights)))
            if m >= 3:
                s.add(tuple(r3(r2(r1(lights)))))
                s.add(tuple(r4(r2(r1(lights)))))
                s.add(tuple(r4(r3(r1(lights)))))
                s.add(tuple(r4(r3(r2(lights)))))
        return len(s)
