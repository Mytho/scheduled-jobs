#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


class JobRunner(object):

    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.add_ping('https://groceries-api.herokuapp.com/status')
        self.add_ping('https://challenge-backend.herokuapp.com/ping')
        self.scheduler.start()

    def add_ping(self, url):
        def fn():
            requests.get(url)
        self.scheduler.add_job(fn, trigger='cron', minute='*/20', hour='7-22')



if __name__ == '__main__':
    JobRunner(BlockingScheduler())
