# -*- coding: utf-8 -*-

import pytest
from config import *


def test_db_active():
    subscriptionsTable = dynamoDB.Table('Subscriptions')
    assert subscriptionsTable.table_status == 'ACTIVE'
