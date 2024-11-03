import asyncio 
import websockets
import module1



async def handle_connection(websocket,path):
    while True:
        try:
            message = await websocket.recv()
            print(f"received message : {message}")
            mood , song = module1.getSongsuggest(message)
            result = f"you are in {mood} mood , we prefer {song['title']}"
            print("result:",result)
            await websocket.send(result)
        except websockets.ConnectionClosed:
            print("Connection closed")
            break
async def main():
    async with websockets.serve(handle_connection, "localhost",5000):
        print("server started on port 5000")
        await asyncio.Future()


asyncio.run(main())