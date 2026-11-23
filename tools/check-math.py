#!/usr/bin/env python3
"""Numerically check the arithmetic claims the mathematics dossiers make.

Not a proof checker — a sanity check that the numbers on the page hold where they
can be tested, and that the published constants quoted are the right ones.

    python3 tools/check-math.py
"""
import sys
from math import pi

try:
    from sympy import isprime, primerange
except ImportError:
    print("sympy is required: pip install sympy")
    sys.exit(2)

FAILS = []


def check(name, ok, detail=""):
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}{(' — ' + detail) if detail else ''}")
    if not ok:
        FAILS.append(name)


def collatz_steps(n, cap=100_000):
    s = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        s += 1
        if s > cap:
            return None
    return s


def main():
    print("Collatz — every n below 1,000,000 reaches 1")
    check("no non-terminating start under 1e6",
          all(collatz_steps(n) is not None for n in range(1, 1_000_000)))

    print("\nGoldbach — every even n from 4 to 100,000 is a sum of two primes")
    primes = set(primerange(2, 100_000))
    bad = [n for n in range(4, 100_000, 2)
           if not any(n - p in primes for p in primes if p < n)]
    check("no counterexample below 1e5", not bad, f"{len(bad)} found" if bad else "")

    print("\nTwin primes — the page's claim that the largest pair below 1e6 is (999959, 999961)")
    ps = list(primerange(2, 1_000_000))
    tw = [(a, b) for a, b in zip(ps, ps[1:]) if b - a == 2]
    check("largest pair below 1e6", tw[-1] == (999959, 999961), f"found {tw[-1]}")
    check("pair count below 1e6 is 8,169", len(tw) == 8169, f"found {len(tw)}")

    print("\nLegendre — a prime lies between n² and (n+1)² for every n < 2,000")
    bad = [n for n in range(1, 2000) if not any(isprime(x) for x in range(n * n + 1, (n + 1) ** 2))]
    check("no counterexample below 2000", not bad, f"n = {bad[:3]}" if bad else "")

    print("\nMoving sofa — the two constants quoted on the page")
    hammersley = pi / 2 + 2 / pi
    check("Hammersley pi/2 + 2/pi rounds to 2.2074", round(hammersley, 4) == 2.2074,
          f"{hammersley:.7f}")
    check("Gerver's 2.2195 is above Hammersley's", 2.2195 > round(hammersley, 4))

    print("\nOdd perfect numbers — none below 100,000")
    def sigma(n):
        s, m, p = 1, n, 2
        while p * p <= m:
            if m % p == 0:
                e = 0
                while m % p == 0:
                    m //= p
                    e += 1
                s *= (p ** (e + 1) - 1) // (p - 1)
            p += 1
        if m > 1:
            s *= (m + 1)
        return s
    check("none below 1e5", not [n for n in range(3, 100_000, 2) if sigma(n) == 2 * n])

    print()
    if FAILS:
        print(f"{len(FAILS)} check(s) failed")
        return 1
    print("all arithmetic checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
