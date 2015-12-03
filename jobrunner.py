#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler


class JobRunner(object):

    def __init__(self, scheduler):
        self.scheduler = scheduler
        self.add_ping('https://groceries-api.herokuapp.com/status')
        self.add_ping('https://challenge-backend.herokuapp.com/ping')
        self.scheduler.start()

    def add_ping(self, url):
        self.scheduler.add_job(
            self._ping(url),
            trigger='cron',
            minute='*/5',
            hour='7-22')

    def _ping(self, url):
        def handler():
            print('Pinging {}'.format(url))
        return handler


if __name__ == '__main__':
    JobRunner(BlockingScheduler())
