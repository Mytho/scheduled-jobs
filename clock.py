#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import requests
import sys

from apscheduler.schedulers.blocking import BlockingScheduler


LOG = logging.getLogger(sys.argv[0])


def ping(url):
    def fn():
        LOG.info('Pinging {}'.format(url))
        return requests.get(url)
    return fn


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    scheduler = BlockingScheduler()
    scheduler.add_job(
        ping('https://challenge-backend.herokuapp.com/ping'),
        trigger='cron',
        minute='*/20',
        hour='6-21')
    scheduler.add_job(
        ping('https://groceries-api.herokuapp.com/status'),
        trigger='cron',
        minute='*/20',
        hour='6-21')
    scheduler.start()
