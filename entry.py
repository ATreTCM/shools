import argparse
import asyncio

import aiohttp
from schools import create_app
from schools.settings import config

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print("not working")

parser = argparse.ArgumentParser(description="Schools project")
parser.add_argument("--host",help="Host to listen", default="0.0.0.0")
parser.add_argument ("--port", help="Port to accept connections", default="5000")
parser.add_argument("--reload", action="store_true", help="autoreload code on change")

args = parser.parse_args()
 
    
app = create_app(config)


if args.reload:
    
    import aioreloader
    aioreloader.start()

if __name__ == "__main__":
    aiohttp.web.run_app(app, host=args.host, port=args.port)