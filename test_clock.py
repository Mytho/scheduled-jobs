# -*- coding: utf-8 -*-
import clock
import mock


class TestRunner(object):

    @mock.patch('apscheduler.schedulers.blocking.BlockingScheduler.start')
    def test_init(self, patched):
        clock.Runner(['http://domain.tld/file.ext'])

        assert patched.call_count == 1

    @mock.patch('requests.get')
    def test_ping(self, patched):
        url = 'http://domain.tld/file.ext'
        runner = clock.Runner([url], scheduler_class=mock.Mock)
        runner.ping(url)()

        args, kwargs = patched.call_args
        assert args[0] == url
