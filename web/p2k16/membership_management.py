import string
from typing import Optional

import flask

from p2k16 import P2k16UserException, P2k16TechnicalException, app
from p2k16.models import User, Group, GroupMember, MembershipPayment
from p2k16.database import db
import datetime

def paid_members():
    return User.query.\
        join(MembershipPayment, MembershipPayment.user_id == User.id).\
        filter(MembershipPayment.end_date >= datetime.datetime.utcnow()).\
        all()

def active_member(user=None) -> bool:
    """
    Verify that user is an active member of Bitraf either by paying or some other mechanism
    :param user: User object
    :return: bool
    """
    return User.query.join(MembershipPayment).filter(User.id == user.id, MembershipPayment.end_date >= datetime.datetime.utcnow()).scalar() is not None