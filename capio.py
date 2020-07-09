import argparse
import asyncio
import logging
import sys

import pyppeteer

from pyShot import pyShot

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--proxy', '-p', type=str, help='Proxy to use for outbound connections e.g. http://127.0.0.1:8080')
PARSER.add_argument('--url', '-u', type=str, action='append', help='Remote URL to screenshot with optional port. This can be specified multiple times')
PARSER.add_argument('--inputfile', '-if', type=str, help='Path to input file, one line per URL in the format protocol://host[:port]')

ARGS = PARSER.parse_args()

if not (ARGS.url or ARGS.inputfile):
    PARSER.error('--url or --inputfile must be specified')

logging.basicConfig(format='%(message)s', level=logging.INFO, stream=sys.stderr)

# Suppress pyppeteer logs
pyppeteer_logger = logging.getLogger('pyppeteer')
pyppeteer_logger.setLevel(logging.WARNING)


async def capture(s: pyShot, browser: pyppeteer.browser, urls: list):
    coros = [s.capture_screenshot(browser, url) for url in urls]
    await asyncio.gather(*coros)
    await browser.close()


def main():
    s = pyShot.pyShot(ARGS.proxy)
    loop = asyncio.get_event_loop()
    browser = loop.run_until_complete(s.get_browser())

    if ARGS.inputfile:
        try:
            with open(ARGS.inputfile, 'r') as url_file:
                urls = url_file.read().splitlines()
                url_file.close()
                logging.info(f'[i] Found {len(urls)} url(s) in {ARGS.inputfile}')

        except (OSError, IOError) as err:
            logging.error(f'[!] Input file{ARGS.inputfile} not found')
            sys.exit(1)
    else:
        urls = ARGS.url

    loop.run_until_complete(capture(s, browser, urls))


if __name__ == '__main__':
    main()
