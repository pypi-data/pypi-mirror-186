# import typing
import unittest
import logging

from tkmilan.spec import Limit

logger = logging.getLogger(__name__)


class Test_Spec_Limit(unittest.TestCase):
    def test_int_finite(self):
        lim_imin = Limit(1, 10, fn=int, imin=True, imax=False)
        with self.subTest(limit=str(lim_imin)):
            self.assertTrue('1' in lim_imin)
            self.assertTrue('5' in lim_imin)
            self.assertFalse('10' in lim_imin)
        lim_imax = Limit('1', '10', fn=int, imin=False, imax=True)
        with self.subTest(limit=str(lim_imax)):
            self.assertFalse('1' in lim_imax)
            self.assertTrue('5' in lim_imax)
            self.assertTrue('10' in lim_imax)
        lim_inone = Limit('1', '10', fn=int, imin=False, imax=False)
        with self.subTest(limit=str(lim_inone)):
            self.assertFalse('1' in lim_inone)
            self.assertTrue('5' in lim_inone)
            self.assertFalse('10' in lim_inone)

    def test_int_infinite(self):
        lim_nomin = Limit(None, 10, fn=int)
        with self.subTest(limit=str(lim_nomin)):
            self.assertTrue('-100' in lim_nomin)
            self.assertTrue('5' in lim_nomin)
            self.assertFalse('+100' in lim_nomin)
        lim_nomax = Limit('1', None, fn=int)
        with self.subTest(limit=str(lim_nomax)):
            self.assertFalse('-100' in lim_nomax)
            self.assertTrue('5' in lim_nomax)
            self.assertTrue('+100' in lim_nomax)


if __name__ == '__main__':
    import sys
    logs_lvl = logging.DEBUG if '-v' in sys.argv else logging.INFO
    logging.basicConfig(level=logs_lvl, format='%(levelname)5.5s:%(funcName)s: %(message)s', stream=sys.stderr)
    unittest.main()
