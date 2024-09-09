from fastapi import FastAPI

from app.internal.db import init_db

app = FastAPI()


@app.on_event("startup")
async def start_db() -> None:
    """To start the database on application startup.

    This function is called when the application starts up
    and initializes the database by calling the `init_db()` function.

    Parameters
    ----------
    None
    Returns:
    None

    """
    await init_db()
