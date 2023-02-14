from unittest import TestCase
from unittest.mock import patch, MagicMock
from db.models import Direction
from notifications import send_notification


class TestInit(TestCase):

    @patch("notifications.messaging")
    def test_send_notification(self, mock_messaging):
        target, direction, token = 22.3, Direction.OVER, "123"
        expected_data = {
            "target": str(target),
            "direction": direction
        }
        message_mock = MagicMock()
        mock_messaging.Message.return_value = message_mock
        notification_mock = MagicMock()
        mock_messaging.Notification.return_value = notification_mock

        send_notification(target, direction, token)

        mock_messaging.Message.assert_called_once_with(notification=notification_mock, token=token, data=expected_data)
        mock_messaging.send.assert_called_once_with(message_mock)
