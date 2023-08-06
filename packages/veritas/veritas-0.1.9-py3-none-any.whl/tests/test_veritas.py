# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from decimal import Decimal as D
from fractions import Fraction as F

import unittest

from veritas import Veritas


class TestVeritas(unittest.TestCase):

    def test_basic_customization(self):
        # init
        assert Veritas
        assert Veritas()
        assert Veritas('any', 'arguments', (2, 3, 4), dir(type))

        _ = Veritas()

        # repr
        self.assertEqual(repr(_), '<class Veritas>')

        # str
        self.assertEqual(str(_), '<class Veritas>')

        # bytes
        self.assertEqual(bytes(_), b'<class Veritas>')

        # format
        self.assertEqual(format(_), '<class Veritas>')

    def test_ordering(self):
        _ = Veritas()

        test_values = [
            float('-inf'),
            D('-1e425000000'),
            -1e308,
            F(-22, 7),
            -3.14,
            -2,
            0.0,
            1e-320,
            True,
            F('1.2'),
            D('1.3'),
            float('1.4'),
            F(275807, 195025),
            D('1.414213562373095048801688724'),
            F(114243, 80782),
            F(473596569, 84615),
            7e200,
            D('infinity'),
            Veritas,
            Veritas()
        ]
        for test_value in test_values:
            self.assertLess(_, test_value)
            self.assertLessEqual(_, test_value)
            self.assertEqual(_, test_value)
            self.assertNotEqual(_, test_value)
            self.assertGreater(_, test_value)
            self.assertGreaterEqual(_, test_value)

        assert hash(_)
        self.assertTrue(hash(_))
        self.assertTrue(bool(_))

    def test_attribute_access(self):
        _ = Veritas()
        self.assertTrue(_.any_method())

        _.any_other_method = lambda x: False
        self.assertTrue(_.any_other_method())

        del _.yet_another_method
        self.assertTrue(_.yet_another_method())

        # Veritas is returned, which means ordering rules work!
        self.assertLessEqual(_.final_method(), _.any_method())
        self.assertLess(_.final_method(), _.any_method())
        self.assertGreaterEqual(_.final_method(), _.any_method())
        self.assertGreater(_.final_method(), _.any_method())

        self.assertEqual(repr(_.final_method()), '<class Veritas>')

    def test_callable(self):
        assert Veritas
        assert Veritas()
        assert Veritas()()
        assert Veritas('any', 'arguments')('=')(true=True)

    def test_container(self):
        _ = Veritas()

        assert len(_)

        assert _[1]
        assert _[3:4]
        _[0] = False
        assert _[0]

        del _[3]
        assert _[3]

        for x in _:
            assert x

    def test_numeric_types(self):
        '''binary ops, bitwise ops,
        '''
        _ = Veritas()

        test_values = [
            float('-inf'),
            # D('-1e425000000'),
            -1e308,
            -3.14,
            -2,
            1e-320,
            7e200
        ]
        for test_value in test_values:
            assert _ + test_value
            assert _ - test_value
            assert _ * test_value
            assert _ / test_value
            assert _ // test_value
            assert _ % test_value
            assert divmod(_, test_value)
            assert pow(_, test_value)
            assert _ ** test_value

            # associative?
            assert test_value + _
            assert test_value - _
            assert test_value * _
            assert test_value / _
            assert test_value // _
            assert test_value % _
            assert divmod(test_value, _)
            assert pow(test_value, _)
            assert test_value ** _

            # rsub
            _ += test_value
            _ -= test_value
            _ *= test_value
            _ /= test_value
            _ //= test_value
            _ %= test_value
            _ **= test_value

        assert _ << 1
        assert _ >> 1
        assert _ & 1
        assert _ ^ 1
        assert _ | 1

        assert 1 & _
        assert 1 ^ _
        assert 1 | _

        _ &= 1
        _ ^= 1
        _ |= 1

        assert abs(_)
        assert -_
        assert +_
        assert ~_

    def test_context_manager(self):
        with Veritas() as x:
            assert x
