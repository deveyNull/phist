#!/usr/bin/env python

import os
import re
import sys
import time
import Queue
import datetime
import json
import signal
import hashlib
from threading import Thread, activeCount
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.util import Finalize
from functools import partial
from urllib2 import URLError
from signal import SIGTERM

halt = False

try:
    import argparse
except ImportError as e:
    print
    'Missing needed module: easy_install argparse'
    halt = True

try:
    import requests
except ImportError as e:
    print
    'Missing needed module: easy_install requests'
    halt = True

try:
    from pyvirtualdisplay import Display
except ImportError as e:
    print
    'Missing needed module: easy_install pyvirtualdisplay'
    halt = True

try:
    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
except ImportError as e:
    print
    'Missing needed module: easy_install selenium'
    halt = True

try:
    import MySQLdb
except ImportError as e:
    print
    'Missing needed module: pip install MySQL-python'
    halt = True

try:
    import boto
    import boto.sqs
    from boto.s3.key import Key
    from boto.sqs.message import RawMessage
except ImportError as e:
    print
    'Missing needed module: pip install boto'
    halt = True

try:
    from PIL import Image
except ImportError as e:
    print
    'Missing needed module: easy_install pillow'
    halt = True

try:
    import psutil
except ImportError as e:
    print
    'Missing needed module: easy_install psutil'
    halt = True

if halt:
    sys.exit()

# from lib.core.constants import TOOL_ROOT
# from lib.core.config import Config
# from lib.core.database import db

sigint = False
_finalizers = []


def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', action='store', dest='threads', default=4, type=int,
                        help='Enable Threading. Specify No. of Threads')
    parser.add_argument('-w', '--wait', action='store', dest='wait', default=0, type=int,
                        help='Wait time between tasks')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='Enable debug messages')
    parser.add_argument('-f', '--file', action='store', dest='file', help='files of domains or ips')

    global args
    args = parser.parse_args()

    # global cfg
    # cfg = Config()


# noinspection PyStatementEffect
def signal_handler(signal, frame):
    print
    ' Ctrl+C detected... exiting...\n'
    sys.exit(1)


def process_handler(domain_data, regex):
    queue = Queue.Queue()

    if args.threads > 1:
        threads = []
        for domain in domain_data:
            queue.put(domain)

        while not queue.empty() and not sigint:
            if args.threads >= activeCount() and not sigint:
                q_itm = queue.get()
                try:
                    t = Thread(target=run_process, args=(q_itm, regex,))
                    t.daemon = True

                    threads.append(t)
                    t.start()
                finally:
                    queue.task_done()

        while activeCount() > 1:
            time.sleep(0.1)

        for thread in threads:
            thread.join(timeout=150)

            if thread.is_alive():
                thread.terminate()

            thread.kill_received = True

        queue.join()

    else:
        for domain in domain_data:
            run_process(domain, regex)
            if sigint:
                signal_handler('', '')

    return


def run_process_helper(args):
    return run_process(*args)


# noinspection PyStatementEffect
def run_process_helper_abortable(func, *args, **kwargs):
    out = ''
    timeout = kwargs.get('timeout', None)
    p = ThreadPool(1)
    res = p.apply_async(func, args=args)
    try:
        out = res.get(timeout)
    except multiprocessing.TimeoutError:
        print
        'Aborting due to timeout'
        p.terminate()
    return out


# noinspection PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect,PyStatementEffect
def run_process(domain):
    saved = False

    domain_name = domain[0].strip()
    # print(domain_name)
    if args.debug:
        print
        'Starting thread for %s' % domain_name

    display = Display(visible=0, size=(800, 800), backend='xvfb')
    display.start()

    if display.is_started:
        try:
            browser = webdriver.PhantomJS()
            browser.set_window_size(800, 800)
            browser.set_page_load_timeout(5)
        except Exception as e:
            if args.debug:
                print
                'Error creating browser %s' % e.message
            return

        if browser:
            try:
                browser.get('http://%s' % domain_name)
            except TimeoutException as e:
                pass
            except URLError as e:
                pass
            finally:
                try:
                    fileName = "Screenshots/" + domain_name.replace("/", "-")
                    saved = browser.save_screenshot('%s.png' % fileName)
                except Exception as e:
                    if args.debug:
                        print
                        'Some weird error %s %s' % (domain_name, e)
                try:
                    browser.close()
                except ValueError as e:
                    if args.debugdd:
                        print
                        'browser.close() ValueError %s' % e
                    pass

                browser.quit()

                if args.debug:
                    print
                    'Deleting SQS message for %s' % domain_name

        else:
            if args.debug:
                print
                'Skipping NO_BROWSER for %s.png' % domain_name

        d_pid = display.pid

        display.stop()

        try:
            os.kill(d_pid, SIGTERM)
            if args.debug:
                print
                'Forced killing the display [os.kill(d_pid)] for %s' % domain_name
        except OSError as e:
            pass

        display.popen.wait()

        try:
            display.popen.kill()
            if args.debug:
                print
                'Forced Killing the display [popen.kill()] for %s' % domain_name
        except Exception as e:
            pass

    else:
        if args.debug:
            print
            'Display was not started'

    if args.debug:
        print
        'Ending Thread for %s' % domain_name

    return


def run_process_callback(x):
    pass


# noinspection PyStatementEffect
def main():
    setup()
    # print 'Running....'
    no_items = False

    fp = open(args.file, 'rb')
    omarax_500 = fp.readlines()
    fp.close()
    # print(omarax_500)

    if omarax_500:

        try:
            p = multiprocessing.Pool(args.threads)
            # _finalizers.append(Finalize(p, p.terminate))
            for bl_itm in omarax_500:
                ja = [bl_itm.strip()]
                # abortable_func = partial(run_process_helper_abortable, run_process_helper, timeout=300)
                p.map_async(run_process, (ja,), callback=run_process_callback)
                # run_process_callback(run_process(ja))

            p.close()
            p.join()
        finally:
            pass

        # print 'tring to kill processes...'

        for proc in psutil.process_iter():
            if proc.name() == 'phantomjs':
                try:
                    proc.kill()
                except psutil.NoSuchProcess:
                    pass

        for proc in psutil.process_iter():
            if proc.name() == 'nodejs':
                try:
                    proc.kill()
                except psutil.NoSuchProcess:
                    pass

        for proc in psutil.process_iter():
            if proc.name() == 'Xvfb':
                try:
                    proc.kill()
                except psutil.NoSuchProcess:
                    pass

    else:
        print
        'There were no queue items to process'


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
