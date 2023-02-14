from unittest import TestCase
from unittest.mock import patch, MagicMock
from security import create_access_token, get_username_from_token


class TestInit(TestCase):

    @patch("security.jwt")
    def test_create_access_token(self, mock_jwt):
        encoded = "test"
        mock_jwt.encode.return_value = encoded

        actual = create_access_token("rado21")

        self.assertEqual(encoded, actual)
        mock_jwt.encode.assert_called_once()

    @patch("security.jwt")
    def test_get_username_from_token(self, mock_jwt):
        token = "123"
        decoded = "decoded"
        payload = MagicMock()
        mock_jwt.decode.return_value = payload
        payload.get.return_value = decoded

        actual = get_username_from_token(token)

        self.assertEqual(decoded, actual)

        mock_jwt.decode.assert_called_once_with(token,
                                                "afeb1279e3b7f013775608f6497d19a6d4513eb1408b42d574b5d1f2a578f379",
                                                algorithms=["HS256"])
        payload.get.assert_called_once_with("sub")
