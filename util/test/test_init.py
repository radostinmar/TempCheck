from unittest import TestCase
from unittest.mock import patch
from util import get_up_to_date, Period


class TestInit(TestCase):

    @patch("util.datetime")
    def test_get_up_to_date_with_period_day(self, mock_datetime):
        self.period_test(mock_datetime, Period.DAY, days=1)

    @patch("util.datetime")
    def test_get_up_to_date_with_period_week(self, mock_datetime):
        self.period_test(mock_datetime, Period.WEEK, weeks=1)

    @patch("util.datetime")
    def test_get_up_to_date_with_period_month(self, mock_datetime):
        self.period_test(mock_datetime, Period.MONTH, days=30)

    @patch("util.datetime")
    def test_get_up_to_date_with_period_year(self, mock_datetime):
        self.period_test(mock_datetime, Period.YEAR, days=365)

    def period_test(self, mock_datetime, period, **kwargs):
        mock_current_time = mock_datetime.datetime.utcnow.return_value
        mock_timedelta = mock_datetime.timedelta.return_value
        mock_up_to = mock_current_time.__sub__.return_value

        actual = get_up_to_date(period)

        self.assertEqual(mock_up_to, actual)
        mock_datetime.datetime.utcnow.assert_called_once()
        mock_current_time.__sub__.assert_called_once_with(mock_timedelta)
        mock_datetime.timedelta.assert_called_once_with(**kwargs)
