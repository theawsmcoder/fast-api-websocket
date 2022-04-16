import os
import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config

from sample_code import app

ON_HEROKU = os.environ.get("ON_HEROKU")

PORT = os.environ.get("PORT", 17995)


config = Config()
config.bind = [f"0.0.0.0:{PORT}"]

asyncio.run(serve(app, config))

