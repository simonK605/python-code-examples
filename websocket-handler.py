import logging
import asyncio
from aiohttp import web, WSMsgType

# Configure logging
logging.basicConfig(filename='websocket_server.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


async def handle_message(ws, msg):
    """
    Handles incoming WebSocket messages.

    Parameters:
        ws (WebSocketResponse): WebSocket connection.
        msg (WSMessage): Received WebSocket message.

    Returns:
        None
    """
    try:
        if msg.type == WSMsgType.TEXT:
            await ws.send_str(f"Received: {msg.data}")
    except Exception as e:
        logging.error(f"Error handling message: {e}")
        await ws.close()


async def websocket_handler(request):
    """
    WebSocket handler function.

    Parameters:
        request (Request): WebSocket request.

    Returns:
        None
    """
    try:
        # Prepare WebSocket connection
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        # Process incoming WebSocket messages
        async for msg in ws:
            await handle_message(ws, msg)

    except asyncio.CancelledError:
        logging.info("WebSocket connection closed by client")
    except Exception as e:
        logging.exception("WebSocket handler error")
    finally:
        await ws.close()


async def start_websocket_server():
    """
    Starts the WebSocket server.

    Returns:
        None
    """
    app = web.Application()
    app.router.add_get('/ws', websocket_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()


if __name__ == '__main__':
    # Get the event loop
    loop = asyncio.get_event_loop()
    try:
        # Start the WebSocket server
        loop.run_until_complete(start_websocket_server())
        loop.run_forever()
    except KeyboardInterrupt:
        logging.info("WebSocket server stopped by user")
    finally:
        loop.close()
