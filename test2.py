from io import StringIO
from unittest import main, TestCase
from army import Army
from Diplomacy import diplomacy_read, diplomacy_eval, diplomacy_print, diplomacy_solve, diplomacy_create_army

class TestDiplomacy (TestCase):


    def test_solve_1(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC London\n")

    # def test_solve_2(self):
    #     r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\n")
    #     w = StringIO()
    #     diplomacy_solve(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "A [dead]\nB [dead]\n")

    # def test_solve_3(self):
    #     r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\nD Austin Move London\n")
    #     w = StringIO()
    #     diplomacy_solve(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD [dead]\n")

    # def test_solve_4(self):
    #     r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\n")
    #     w = StringIO()
    #     diplomacy_solve(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "A [dead]\nB [dead]\nC [dead]\n")

    # def test_solve_5(self):
    #     r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\n")
    #     w = StringIO()
    #     diplomacy_solve(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "A [dead]\nB Madrid\nC [dead]\nD Paris\n")

    # def test_solve_6(self):
    #     r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
    #     w = StringIO()
    #     diplomacy_solve(r, w)
    #     self.assertEqual(
    #         w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")


if __name__ == "__main__":  # pragma: no cover
    main()
