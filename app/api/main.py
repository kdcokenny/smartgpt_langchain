from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.scripts import handle_smartgpt_chain

app = FastAPI()


app.mount("/static", StaticFiles(directory="app/frontend"), name="static")


@app.get("/")
def serve_html():
    return FileResponse("app/frontend/index.html")


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_json()

        query = message["query"]
        model = message["model"]
        print(f"Model: {model}")
        response = handle_smartgpt_chain(query, model)
        answer = response["final_answer"]

        await websocket.send_json({"answer": answer})
