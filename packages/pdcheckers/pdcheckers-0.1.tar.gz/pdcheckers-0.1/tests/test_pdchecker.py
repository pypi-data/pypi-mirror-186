import unittest
import pandas as pd
from pdcheckers import PdChecker


class PdCheckerUT(unittest.TestCase):

    TEST_DF = pd.read_csv('data/mock_data_dirty.csv', error_bad_lines=False)

    def test_email(self):
        df_r_email = PdChecker(self.TEST_DF).pd_sniffer("email")
        self.assertEqual(df_r_email.shape, (2, 2))
        self.assertEqual(df_r_email["column"][0], "email")
        self.assertGreater(df_r_email["perc"][0], 0.75)

    def test_full_name(self):
        df_full_name = self.TEST_DF.copy()
        df_full_name["full_name"] = df_full_name["first_name"]\
            + " " + df_full_name["last_name"]
        df_r_full_name = PdChecker(df_full_name).pd_sniffer("full_name")
        self.assertEqual(df_r_full_name.shape, (4, 2))
        self.assertEqual(df_r_full_name["column"][0], "full_name")
        self.assertGreater(df_r_full_name["perc"][0], 0.75)

    def test_number(self):
        df_r_number = PdChecker(self.TEST_DF).pd_sniffer("number")
        self.assertEqual(df_r_number.shape, (5, 2))
        self.assertEqual(df_r_number["column"][0], "ip_address")
        self.assertGreater(df_r_number["perc"][0], 0.10)

    def test_date(self):
        df_r_date = PdChecker(self.TEST_DF).pd_sniffer("date")
        self.assertEqual(df_r_date.shape, (2, 2))
        self.assertEqual(df_r_date["column"][0], "date")
        self.assertGreater(df_r_date["perc"][0], 0.75)
