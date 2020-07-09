import argparse
import asyncio
import logging
import sys

import pyppeteer

from pyShot import pyShot

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--proxy', '-p', type=str, help='Proxy to use for outbound connections e.g. http://127.0.0.1:8080')
PARSER.add_argument('--url', '-u', type=str, required=True, action='append', help='Remote URL to screenshot with optional port. This can be specified multiple times')

ARGS = PARSER.parse_args()

logging.basicConfig(format='%(message)s', level=logging.INFO, stream=sys.stderr)

# Suppress pyppeteer logs
pyppeteer_logger = logging.getLogger('pyppeteer')
pyppeteer_logger.setLevel(logging.WARNING)


async def capture(browser: pyppeteer.browser, urls: list):
    coros = [s.capture_screenshot(browser, url) for url in urls]
    await asyncio.gather(*coros)
    await browser.close()


if __name__ == '__main__':
    s = pyShot.pyShot(ARGS.proxy)
    loop = asyncio.get_event_loop()
    browser = loop.run_until_complete(s.get_browser())
    loop.run_until_complete(capture(browser, ARGS.urls))
