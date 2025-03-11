import asyncio
import websockets
import json
import csv
import time

SOCKET_URL = "wss://ws.coincap.io/prices?assets=bitcoin,ethereum,tether,binance-coin,solana,usd-coin"
CSV_FILE = 'stock_data.csv'
data_batch = []

def write_to_csv(data_batch):
    if not data_batch:
        return
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["symbol", "price", "volume"])
        writer.writerows(data_batch)
    data_batch.clear()

async def connect():
    global data_batch
    while True:
        try:
            async with websockets.connect(SOCKET_URL) as websocket:
                print("Connected to WebSocket.")
                while True:
                    message = await websocket.recv()
                    data = json.loads(message)
                    symbol = data.get('symbol')
                    price = data.get('price')
                    volume = data.get('volume')
                    data_batch.append([symbol, price, volume])
                    if len(data_batch) >= 100:
                        write_to_csv(data_batch)

        except (websockets.exceptions.ConnectionClosed, ConnectionError) as e:
            print(f"Connection error: {e}. Reconnecting...")
            time.sleep(5)

async def main():
    await connect()

if __name__ == '__main__':
    asyncio.run(main())  