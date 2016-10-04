"""Base classes for Joinos v2's background tasks
"""
import logging
import json
import traceback

from datetime import datetime

from django.conf import settings
from django.db import transaction

from .models import ScheduledTaskStatus


logger = logging.getLogger(__name__)


class ScheduledTask(object):
    """Run a scheduled task at pre-defined dates and times.

    To use this, extend the ScheduledTask class and set up the run_days and
    run_times options with the pre-set dates/times for running this task.

    The potential values for run_days are:
      - monday
      - tuesday
      - wednesday
      - thursday
      - friday
      - saturday
      - sunday

    The run times are set using simple time values, for example:
      - 1am
      - 7pm

    Each value must be a list of possible values.

    Each value will also take * which will ensure this always runs whenever
    the scheduled task is executed.
    """

    run_days = []
    run_times = []

    def __init__(self):
        """Set the initial value for dry_run.
        """
        self.dry_run = False

    def wrapped_run(self, when, dry_run=False):
        """Keeps the running wrapped and state saved
        """
        self.dry_run = dry_run

        task_status, created = ScheduledTaskStatus.objects.update_or_create(
            task_name=self.__class__.__name__,
            defaults={
                'status': 'now',
            })
        logger.info('Running {}'.format(self.__class__.__name__))
        try:
            self.run(when)
        except Exception as ex:
            logger.error(ex)
            traceback.print_exc()
            task_status.status = 'fail'
        else:
            task_status.status = 'ok'
        task_status.save()

    def run(self, when):
        raise NotImplementedError('ScheduledTask.run() not implemented')

    def can_run(self, when):
        w = [when.format('dddd').lower(), when.format('ha')]
        return ((self.run_days == '*' or w[0] in self.run_days)
                and (self.run_times == '*' or w[1] in self.run_times))