import unittest
import rain_risk


class TestRainRisk(unittest.TestCase):

    def test_simple(self):
        result = rain_risk.solve((0, 0), (1, 10), ["F10", "N3", "F7", "R90", "F11"])
        self.assertEqual(result, 286)

    def test_simple2(self):
        result = rain_risk.solve((0, 0), (1, 10), ["F10", "R90", "R90", "R90", "R90"])
        self.assertEqual(result, 110)

    def test_simple3(self):
        result = rain_risk.solve((0, 0), (1, 10), ["F10", "L90", "L90", "L90", "L90", "F10"])
        self.assertEqual(result, 220)

    def test_simple4(self):
        result = rain_risk.solve((0, 0), (1, 10), ["F10", "L180", "L180", "F10"])
        self.assertEqual(result, 220)

    def test_simple5(self):
        result = rain_risk.solve((0, 0), (1, 10), ["F10", "L360", "F10"])
        self.assertEqual(result, 220)

    def test_simple6(self):
        result = rain_risk.solve((0, 0), (1, 10), ["F10", "R360", "F10"])
        self.assertEqual(result, 220)

    def test_simple7(self):
        result = rain_risk.solve((0, 0), (1, 10), ["F10", "R90", "L90", "R180", "L180", "F10"])
        self.assertEqual(result, 220)

    def test_north(self):
        result = rain_risk.solve((0, 0), (1, 10), ["N3", "F10"])
        self.assertEqual(result, 140)

    def test_south(self):
        result = rain_risk.solve((0, 0), (1, 10), ["S3", "F10"])
        self.assertEqual(result, 120)

    def test_west(self):
        result = rain_risk.solve((0, 0), (1, 10), ["W3", "F10"])
        self.assertEqual(result, 80)

    def test_east(self):
        result = rain_risk.solve((0, 0), (1, 10), ["E3", "F10"])
        self.assertEqual(result, 140)

    def test_simple8(self):
        result = rain_risk.solve((1, 0), (0, 10), ["F10", "R90", "R90", "R90", "R90"])
        self.assertEqual(result, 101)

    def test_simple9(self):
        result = rain_risk.solve((0, 0), (0, 10), ["R90", "F10"])
        self.assertEqual(result, 100)

    def test_simple10(self):
        result = rain_risk.solve((0, 0), (1, 10), ["L90", "F10"])
        self.assertEqual(result, 110)

if __name__ == "__main__":
    unittest.main()
