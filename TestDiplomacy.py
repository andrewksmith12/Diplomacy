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
from Diplomacy import diplomacy_read, diplomacy_eval, diplomacy_print, diplomacy_solve, diplomacy_create_army

# -----------
# TestDiplomacy
# -----------


class TestDiplomacy (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "A Madrid Support B\n"
        i, j, a, o = diplomacy_read(s)
        self.assertEqual(i,  'A')
        self.assertEqual(j, 'Madrid')
        self.assertEqual(a,  'Support')
        self.assertEqual(o, 'B')

    def test_read_2(self):
        s = "C Paris Hold\n"
        i, j, a, o = diplomacy_read(s)
        self.assertEqual(i,  'C')
        self.assertEqual(j, 'Paris')
        self.assertEqual(a,  'Hold')
        self.assertEqual(o,  '')

    def test_read_3(self):
        s = "B London Move Madrid\n"
        i, j, a, o = diplomacy_read(s)
        self.assertEqual(i,  'B')
        self.assertEqual(j, 'London')
        self.assertEqual(a,  'Move')
        self.assertEqual(o,  'Madrid')

    # ----
    # create army
    # ----

    def test_create_1(self):
        a = diplomacy_create_army("A", "London", "Move", "Madrid")
        self.assertEqual(a.name, "A")
        self.assertEqual(a.location, "London")
        self.assertEqual(a.action, "Move")
        self.assertEqual(a.destination, "Madrid")

    def test_create_2(self):
        a = diplomacy_create_army("A", "London", "Support", "B")
        self.assertEqual(a.name, "A")
        self.assertEqual(a.location, "London")
        self.assertEqual(a.action, "Support")
        self.assertEqual(a.supporting, "B")

    def test_create_3(self):
        a = diplomacy_create_army("B", "Paris", "Hold", "")
        self.assertEqual(a.name, "B")
        self.assertEqual(a.location, "Paris")
        self.assertEqual(a.action, "Hold")

    # ----
    # eval
    # ----

    # def test_eval_1(self):
    #     v = diplomacy_eval(1, 1)
    #     self.assertEqual(v, 1)

    # def test_eval_2(self):
    #     v = diplomacy_eval(100, 200)
    #     self.assertEqual(v, 125)

    # def test_eval_3(self):
    #     v = diplomacy_eval(201, 210)
    #     self.assertEqual(v, 89)

    # def test_eval_4(self):
    #     v = diplomacy_eval(900, 1000)
    #     self.assertEqual(v, 174)

    # def test_eval_5(self):
    #     v = diplomacy_eval(100, 100)
    #     self.assertEqual(v, 26)


    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        diplomacy_print(w, 'A', '[dead]')
        self.assertEqual(w.getvalue(), "A [dead]\n")

    def test_print_2(self):
        w = StringIO()
        diplomacy_print(w, 'B', 'London')
        self.assertEqual(w.getvalue(), "B London\n")

    def test_print_3(self):
        w = StringIO()
        diplomacy_print(w, 'D', 'Madrid')
        self.assertEqual(w.getvalue(), "D Madrid\n")

    # -----
    # solve
    # -----

    def test_solve_0(self):
        r = StringIO("A Madrid Hold\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A Madrid\n")

    def test_solve_1(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC London\n")

    def test_solve_2(self):
        r = StringIO("\nA Madrid Hold\nB Barcelona Move Madrid\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\n")

    def test_solve_3(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\nD Austin Move London\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD [dead]\n")

    def test_solve_4(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\n")

    def test_solve_5(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC [dead]\nD Paris\n")

    def test_solve_6(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")



# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()
