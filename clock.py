#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


if __name__ == '__main__':
    self.scheduler = BlockingScheduler()
    for url in ['https://challenge-backend.herokuapp.com/ping',
                'https://groceries-api.herokuapp.com/status']:
        self.scheduler.add_job(
            lambda: requests.get(url),
            trigger='cron',
            minute='*/20',
            hour='7-22')
    self.scheduler.start()
