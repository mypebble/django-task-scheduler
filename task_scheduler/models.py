from django.db import models
from django.utils.translation import ugettext_lazy as _


class ScheduledTaskStatus(models.Model):
    """Report on the progress of a scheduled task.

    This lets us examine the status of scheduled tasks in the admin panel.
    """

    STATUS_OK = 'ok'
    STATUS_RUNNING = 'now'
    STATUS_FAIL = 'fail'

    RUN_STATUS = (
        (STATUS_OK, _('OK')),
        (STATUS_RUNNING, _('In Progress')),
        (STATUS_FAIL, _('Failure')),
    )

    task_name = models.TextField()
    last_runtime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=RUN_STATUS)

    def __unicode__(self):
        return (
            u'{obj.task_name} last ran on {obj.last_runtime} with status '
            u'{obj.status}'.format(obj=self))
