import unittest
from checkers import Checker


class CheckerNumber(unittest.TestCase):

    def test_number_letters(self):
        self.assertFalse(Checker().number("asdfsa"))
        self.assertFalse(Checker().number("10a"))
        self.assertFalse(Checker().number("10a1234"))

    def test_number_separators(self):
        self.assertFalse(Checker().number("10.0.9"))
        self.assertFalse(Checker().number("10,0,9"))

    def test_number_digits(self):
        self.assertTrue(Checker().number("3"))
        self.assertTrue(Checker().number("04"))
        self.assertTrue(Checker().number("10"))
        self.assertTrue(Checker().number("38237845745"))

    def test_number_native(self):
        self.assertTrue(Checker().number(".0"))
        self.assertTrue(Checker().number(".34"))
        self.assertTrue(Checker().number(".345464356756478"))
        self.assertTrue(Checker().number("10.0"))
        self.assertTrue(Checker().number("10234523.3242"))

    def test_number_coma(self):
        self.assertFalse(Checker().number(",0"))
        self.assertFalse(Checker().number(",34"))
        self.assertTrue(Checker().number("10,0"))
        self.assertTrue(Checker().number("10234523,3242"))

    def test_number_thousands(self):
        self.assertTrue(Checker().number("10.234.523"))
        self.assertTrue(Checker().number("10.234.523,3242"))
        self.assertTrue(Checker().number("10,234,523"))
        self.assertTrue(Checker().number("10,234,523.3242"))


class CheckerEmail(unittest.TestCase):

    def test_email(self):
        self.assertTrue(Checker().email("test@gmail.com"))
        self.assertTrue(Checker().email("test.test@gmail.com"))
        self.assertTrue(Checker().email("test_test@gmail.com"))
        self.assertTrue(Checker().email("test@erfweatrerg.com"))
        self.assertTrue(Checker().email("sadfsag34t@a3245r3wrfewres.co"))
        self.assertTrue(Checker().email("sadfsag34t@3245r3wrfewres.co"))
        self.assertFalse(Checker().email("testgmail.com"))
        self.assertFalse(Checker().email("@testgmail.com"))
        self.assertFalse(Checker().email("sadfsag34t@3245r3wrfewresco"))

    def test_non_email(self):
        self.assertFalse(Checker().email("10/10/12"))
        self.assertFalse(Checker().email("10.10.12"))
        self.assertFalse(Checker().email("2012.10.12"))
        self.assertFalse(Checker().email("2012-10-12"))
        self.assertFalse(Checker().email("Fevcs Easdff"))
        self.assertFalse(Checker().date("100,23"))
        self.assertFalse(Checker().date("asdfsa"))
        self.assertFalse(Checker().date("10a"))
        self.assertFalse(Checker().date("10a1234"))
        self.assertFalse(Checker().date("10.0.9"))
        self.assertFalse(Checker().date("10,0,9"))
        self.assertFalse(Checker().date("3"))
        self.assertFalse(Checker().date("04"))
        self.assertFalse(Checker().date("10"))
        self.assertFalse(Checker().date("38237845745"))
        self.assertFalse(Checker().date(".0"))
        self.assertFalse(Checker().date(".34"))
        self.assertFalse(Checker().date(".345464356756478"))
        self.assertFalse(Checker().date("10.0"))
        self.assertFalse(Checker().date("10234523.3242"))
        self.assertFalse(Checker().date(",0"))
        self.assertFalse(Checker().date(",34"))
        self.assertFalse(Checker().date("10,0"))
        self.assertFalse(Checker().date("10234523,3242"))
        self.assertFalse(Checker().date("10.234.523"))
        self.assertFalse(Checker().date("10.234.523,3242"))
        self.assertFalse(Checker().date("10,234,523"))
        self.assertFalse(Checker().date("10,234,523.3242"))


class CheckerFullName(unittest.TestCase):

    def test_full_name(self):
        self.assertTrue(Checker().full_name("Fevcs Easdff"))
        self.assertTrue(Checker().full_name("fevcs easdff"))
        self.assertTrue(Checker().full_name("Fevcs Easdff Afasdf"))
        self.assertFalse(Checker().full_name("Feas"))
        self.assertFalse(Checker().full_name("F"))

    def test_non_full_name(self):
        self.assertFalse(Checker().full_name("test@gmail.com"))
        self.assertFalse(Checker().full_name("10/10/12"))
        self.assertFalse(Checker().full_name("10.10.12"))
        self.assertFalse(Checker().full_name("2012.10.12"))
        self.assertFalse(Checker().full_name("2012-10-12"))
        self.assertFalse(Checker().date("100,23"))
        self.assertFalse(Checker().date("asdfsa"))
        self.assertFalse(Checker().date("10a"))
        self.assertFalse(Checker().date("10a1234"))
        self.assertFalse(Checker().date("10.0.9"))
        self.assertFalse(Checker().date("10,0,9"))
        self.assertFalse(Checker().date("3"))
        self.assertFalse(Checker().date("04"))
        self.assertFalse(Checker().date("10"))
        self.assertFalse(Checker().date("38237845745"))
        self.assertFalse(Checker().date(".0"))
        self.assertFalse(Checker().date(".34"))
        self.assertFalse(Checker().date(".345464356756478"))
        self.assertFalse(Checker().date("10.0"))
        self.assertFalse(Checker().date("10234523.3242"))
        self.assertFalse(Checker().date(",0"))
        self.assertFalse(Checker().date(",34"))
        self.assertFalse(Checker().date("10,0"))
        self.assertFalse(Checker().date("10234523,3242"))
        self.assertFalse(Checker().date("10.234.523"))
        self.assertFalse(Checker().date("10.234.523,3242"))
        self.assertFalse(Checker().date("10,234,523"))
        self.assertFalse(Checker().date("10,234,523.3242"))


class CheckerDate(unittest.TestCase):

    def test_date(self):
        self.assertTrue(Checker().date("13/10/12"))
        self.assertTrue(Checker().date("11/21/22"))
        self.assertTrue(Checker().date("11/21/2022"))
        self.assertTrue(Checker().date("2012-10-12"))

    def test_wrong_date(self):
        self.assertFalse(Checker().date("10.100.12"))
        self.assertFalse(Checker().date("2012.40.12"))
        self.assertFalse(Checker().date("10/100/12"))
        self.assertFalse(Checker().date("2012/40/12"))
        self.assertFalse(Checker().date("40/12/2012"))
        self.assertFalse(Checker().date("2012-10-42"))

    def test_non_date(self):
        self.assertFalse(Checker().date("Fevcs Easdff"))
        self.assertFalse(Checker().date("fevcs easdff"))
        self.assertFalse(Checker().date("Fevcs Easdff Afasdf"))
        self.assertFalse(Checker().date("Feas"))
        self.assertFalse(Checker().date("F"))
        self.assertFalse(Checker().date("test@gmail.com"))
        self.assertFalse(Checker().date("100,23"))
        self.assertFalse(Checker().date("asdfsa"))
        self.assertFalse(Checker().date("10a"))
        self.assertFalse(Checker().date("10a1234"))
        self.assertFalse(Checker().date("10.0.9"))
        self.assertFalse(Checker().date("10,0,9"))
        self.assertFalse(Checker().date("3"))
        self.assertFalse(Checker().date("04"))
        self.assertFalse(Checker().date("10"))
        self.assertFalse(Checker().date("38237845745"))
        self.assertFalse(Checker().date(".0"))
        self.assertFalse(Checker().date(".34"))
        self.assertFalse(Checker().date(".345464356756478"))
        self.assertFalse(Checker().date("10.0"))
        self.assertFalse(Checker().date("10234523.3242"))
        self.assertFalse(Checker().date(",0"))
        self.assertFalse(Checker().date(",34"))
        self.assertFalse(Checker().date("10,0"))
        self.assertFalse(Checker().date("10234523,3242"))
        self.assertFalse(Checker().date("10.234.523"))
        self.assertFalse(Checker().date("10.234.523,3242"))
        self.assertFalse(Checker().date("10,234,523"))
        self.assertFalse(Checker().date("10,234,523.3242"))
