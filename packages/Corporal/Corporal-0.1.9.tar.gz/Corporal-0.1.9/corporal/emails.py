# -*- coding: utf-8; -*-
"""
Custom email profiles
"""

from rattail.mail import Email

# bring in some common config from rattail
from rattail.emails import (ImporterEmail,
                            # ProblemReportEmail,
                            upgrade_failure,
                            upgrade_success,
                            user_feedback)
from rattail_corepos.emails import core_office_export_lane_op_updates
