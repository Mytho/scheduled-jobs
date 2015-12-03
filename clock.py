#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()

for url in ['https://challenge-backend.herokuapp.com/ping',
            'https://groceries-api.herokuapp.com/status']:
    scheduler.add_job(
        lambda: requests.get(url),
        trigger='cron',
        minute='*/20',
        hour='7-22')

scheduler.start()
