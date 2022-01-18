import requests
from flask import current_app as app

from models import FlagStatus, SubmitResult

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


RESPONSES = {
    FlagStatus.QUEUED: ['timeout', 'game not started', 'try again later', 'game over', 'is not up',
                        'no such flag'],
    FlagStatus.ACCEPTED: ['accepted', 'congrat'],
    FlagStatus.REJECTED: ['bad', 'wrong', 'expired', 'unknown', 'your own',
                          'too old', 'not in database', 'already submitted', 'invalid flag','any team','duplicated','corrupted'],
}
# The RuCTF checksystem adds a signature to all correct flags. It returns
# "invalid flag" verdict if the signature is invalid and "no such flag" verdict if
# the signature is correct but the flag was not found in the checksystem database.
#
# The latter situation happens if a checker puts the flag to the service before putting it
# to the checksystem database. We should resent the flag later in this case.


TIMEOUT = 5


def submit_flags(flags, config):
    for flag in flags:
        
        r = requests.post(config['SYSTEM_URL'],
                        json={'team_token': config["TEAM_TOKEN"], 'flag': flag.flag}, timeout=TIMEOUT)

        unknown_responses = set()
        response = r.text

        response_lower = response.lower()
        for status, substrings in RESPONSES.items():
            if any(s in response_lower for s in substrings):
                found_status = status
                break
        else:
            found_status = FlagStatus.QUEUED
            if response not in unknown_responses:
                unknown_responses.add(response)
                logger.info('Unknown checksystem response (flag will be resent): %s', response)

        yield SubmitResult(flag.flag, found_status, response)
