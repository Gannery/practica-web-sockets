import asyncio
import websockets

# Esta función se ejecuta cada vez que un cliente se conecta.
async def echo(websocket):
    print(f"Cliente conectado desde {websocket.remote_address}")

    try:
        # Itera sobre los mensajes recibidos del cliente.
        async for message in websocket:
            print(f"Recibido del cliente: {message}")
            
            # Envía el mismo mensaje de vuelta al cliente.
            await websocket.send(message)
            print(f"Enviado al cliente: {message}")

    except websockets.exceptions.ConnectionClosed:
        print(f"Cliente desconectado: {websocket.remote_address}")

    finally:
        # El bucle termina cuando el cliente se desconecta.
        print("Conexión cerrada.")

async def main():
    # Inicia el servidor de WebSockets en localhost, puerto 8765.
    # Llama a la función `echo` para cada nueva conexión.
    async with websockets.serve(echo, "localhost", 8765):
        print("Servidor de Eco iniciado en ws://localhost:8765")
        await asyncio.Future()  # Mantiene el servidor corriendo indefinidamente.

if __name__ == "__main__":
    asyncio.run(main())