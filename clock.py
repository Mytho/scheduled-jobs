#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()

scheduler.add_job(
    lambda: requests.get('https://challenge-backend.herokuapp.com/ping'),
    trigger='cron',
    minute='*/20',
    hour='8-21')

scheduler.add_job(
    lambda: requests.get('https://groceries-api.herokuapp.com/status'),
    trigger='cron',
    minute='*/20',
    hour='7-22')

scheduler.start()
