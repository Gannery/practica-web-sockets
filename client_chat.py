import asyncio
import websockets

async def chat_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        
        # Tarea para recibir mensajes del servidor.
        async def receive_messages():
            try:
                async for message in websocket:
                    # Imprime el mensaje recibido para que el usuario lo vea.
                    print(f"\n< Mensaje de otro usuario: {message}")
            except websockets.exceptions.ConnectionClosed:
                print("Conexión cerrada por el servidor.")

        # Tarea para enviar mensajes escritos por el usuario.
        async def send_messages():
            while True:
                message = await asyncio.to_thread(input, "Escribe tu mensaje y presiona Enter: ")
                if message.lower() == 'exit':
                    break
                await websocket.send(message)

        # Ejecuta ambas tareas concurrentemente.
        receive_task = asyncio.create_task(receive_messages())
        send_task = asyncio.create_task(send_messages())

        # Espera a que ambas tareas terminen (en este caso, nunca, hasta que se cancele).
        await asyncio.gather(receive_task, send_task)

if __name__ == "__main__":
    try:
        asyncio.run(chat_client())
    except KeyboardInterrupt:
        print("\nCerrando cliente.")
