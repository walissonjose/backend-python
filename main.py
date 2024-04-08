from fastapi import FastAPI
import uvicorn

from controllers import routes
from config.server import port

app = FastAPI(
    title="API for Calendar Application",
    version='0.0.1'
)

for router in routes:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app='main:app', host='localhost', port=port, reload=True)