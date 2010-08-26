"""
A django application to monitor and control icecream scheduler
"""
from django.conf import settings

#
# TODO: import environment ICECREAM_SCHEDULER_HOST=
#
ICECC_SCHEDULER = getattr(settings, 'ICECC_SCHEDULER', 'localhost')
