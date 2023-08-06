import logging
import os
import requests
import json

log = logging.getLogger(__name__)


def notify(recipient: str, message: str, wait: bool = False, retry_times: int = 3) -> bool:
    """Send Message to recipient. If recipient looks like a supported mobile number, then send SMS, otherwise if looks like a email, then send email. If wait, then wait until send is successful or fail after retry.

    Return true if sent successfully. Otherwise return false.
    """
    # TODO: add async and retry on failure.
    try:
        if '@' not in recipient and not recipient.startswith("+"):
            log.error(
                f"The recipient {recipient} does not look like a email or sms. Giving up.")
            return False

        resp = requests.post(
            url=os.environ['NOTIFY_URL'],
            data=json.dumps({
                "recipient": recipient,
                "body": message,
                "sender": os.environ['NOTIFY_TOKEN']
            })
        )
        if resp.status_code//100 == 2:
            return True
        else:
            log.error(
                f"Failed to send notification. {resp.status_code}, {resp.text}")
            return False
    except Exception as e:
        log.error(
            f"Failed to send {message[0:20]} to {recipient}. Exception {e}. Giving up.")
        return False


if __name__ == "__main__":
    assert True == notify(
        recipient='help@bdating.io',
        message='Please visit https://www.bdating.io')
    assert True == notify(
        recipient='+61431009880',
        message='Please visit https://www.bdating.io')
    assert True == notify(
        recipient='+6143', # this library does not care
        message='Please visit https://www.bdating.io')
    assert False == notify(
        recipient='abcde',
        message='Please visit https://www.bdating.io')
