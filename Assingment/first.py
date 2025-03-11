import asyncio
import websockets
import json
import csv
import time

SOCKET_URL = "wss://ws.coincap.io/prices?assets=bitcoin,ethereum,tether,binance-coin,solana,usd-coin"

# Define the CSV file name
CSV_FILE = 'stock_data.csv'

# Initialize a list to batch data before writing to CSV
data_batch = []

# Function to write data to CSV
def write_to_csv(data_batch):
    # If no data in the batch, exit
    if not data_batch:
        return

    # Open CSV file in append mode
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write the headers if the file is empty
        if file.tell() == 0:
            writer.writerow(["symbol", "price", "volume"])
        # Write batched data
        writer.writerows(data_batch)
    # Clear the batch after writing
    data_batch.clear()

# WebSocket connection handler with reconnection logic
async def connect():
    global data_batch
    while True:
        try:
            async with websockets.connect(SOCKET_URL) as websocket:
                print("Connected to WebSocket.")
                while True:
                    message = await websocket.recv()
                    data = json.loads(message)
                    
                    # Extract data from the JSON
                    symbol = data.get('symbol')
                    price = data.get('price')
                    volume = data.get('volume')

                    # Prepare data to be written in CSV
                    data_batch.append([symbol, price, volume])

                    # If the batch size is 100, write to CSV and clear the batch
                    if len(data_batch) >= 100:
                        write_to_csv(data_batch)

        except (websockets.exceptions.ConnectionClosed, ConnectionError) as e:
            print(f"Connection error: {e}. Reconnecting...")
            time.sleep(5)  # Wait before attempting to reconnect

# Start the WebSocket connection and handle reconnection
async def main():
    await connect()

# Run the asyncio event loop
if __name__ == '__main__':
    asyncio.run(main())