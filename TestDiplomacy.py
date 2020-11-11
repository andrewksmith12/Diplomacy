#!/usr/bin/env python3

# -------------------------------
# projects/diplomacy/TestDiplomacy.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_read, diplomacy_eval, diplomacy_print, diplomacy_solve

# -----------
# TestDiplomacy
# -----------


class TestDiplomacy (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = diplomacy_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "20 30\n"
        i, j = diplomacy_read(s)
        self.assertEqual(i,  20)
        self.assertEqual(j, 30)

    def test_read_3(self):
        s = "500 9990\n"
        i, j = diplomacy_read(s)
        self.assertEqual(i,  500)
        self.assertEqual(j, 9990)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = diplomacy_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_2(self):
        v = diplomacy_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = diplomacy_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = diplomacy_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = diplomacy_eval(100, 100)
        self.assertEqual(v, 26)
    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        diplomacy_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        diplomacy_print(w, 2654, 5727, 238)
        self.assertEqual(w.getvalue(), "2654 5727 238\n")

    def test_print_3(self):
        w = StringIO()
        diplomacy_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("2654 5727\n1198 3578\n2822 5647\n1430 8390\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2654 5727 238\n1198 3578 217\n2822 5647 238\n1430 8390 262\n")

    def test_solve_3(self):
        r = StringIO("587 6536\n2570 6440\n1168 9797\n8916 9620\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "587 6536 262\n2570 6440 262\n1168 9797 262\n8916 9620 260\n")

    def test_solve_4(self):
        r = StringIO("587 6536\n2570 6440\n1168 9797\n\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "587 6536 262\n2570 6440 262\n1168 9797 262\n")
# ----
# main
# ----


if __name__ == "__main__":  # pragma: no cover
    main()

""" #pragma: no cover
$ coverage run --branch TestDiplomacy.py >  TestDiplomacy.out 2>&1


$ cat TestDiplomacy.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestDiplomacy.out



$ cat TestDiplomacy.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Diplomacy.py          12      0      2      0   100%
TestDiplomacy.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
