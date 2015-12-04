#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import requests
import sys

from apscheduler.schedulers.blocking import BlockingScheduler


LOG = logging.getLogger(sys.argv[0])


class Runner(object):

    scheduler_class = BlockingScheduler

    def __init__(self, urls, scheduler_class=None):
        if scheduler_class is not None:
            self.scheduler_class = scheduler_class
        logging.basicConfig(level=logging.INFO)
        scheduler = self.scheduler_class()
        for url in urls:
            scheduler.add_job(
                self.ping(url),
                trigger='cron',
                minute='*/20',
                hour='6-21')
        scheduler.start()

    def ping(self, url):
        def fn():
            LOG.info('Pinging {}'.format(url))
            return requests.get(url)
        return fn


if __name__ == '__main__':
    Runner([
        'https://challenge-backend.herokuapp.com/ping',
        'https://groceries-api.herokuapp.com/status',
    ])
