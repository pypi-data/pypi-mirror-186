from typing import List
from datetime import datetime, timezone, timedelta
from tickerdax.client import TickerDax
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='TickerDax Cache API')

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
def root():
    return 'running'


@app.get('/{group}/{item}')
def get_route(
        group: str,
        item: str,
        symbols: List = ['BTC'],
        start: datetime = datetime.now(tz=timezone.utc) - timedelta(hours=1),
        end: datetime = datetime.now(tz=timezone.utc),
        timeframe: str = '1h'
):
    return TickerDax().get_route(
        route=f'{group}/{item}',
        symbols=symbols,
        start=start,
        end=end,
        timeframe=timeframe
    )
