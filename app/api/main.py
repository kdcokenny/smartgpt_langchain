from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # your code for handling the websocket connection goes here