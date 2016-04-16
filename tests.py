import cProfile
import unittest
from datetime import datetime

import mock

from kazy.kazy import main
from kazy.colours import MAIN_COLOURS


class PerformanceTest(unittest.TestCase):
    def test_performance(self):
        with mock.patch("sys.stdin") as mo:
            with mock.patch("kazy.kazy.parse_args", return_value=[
                {"selector": "a", "colour": MAIN_COLOURS["red"]},
                {"selector": "d", "colour": MAIN_COLOURS["cyan"]},
                {"selector": "f", "colour": MAIN_COLOURS["blue"]},
            ]):
                mo.__iter__.return_value = ["abcdefgh" * 100 + "\n" for x in range(100)]
                start = datetime.now()
                cProfile.run("main()", sort="tottime")
                took = datetime.now() - start
                print("Took: {}".format(took))


if __name__ == "__main__":
    unittest.main()
