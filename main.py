from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import random
from fastapi.responses import HTMLResponse

thirukkural = []
english = []
kannada = []


def load_data():
    global thirukkural, english, kannada
    try:
        with open("Tamil_Thirukkural.txt", "r", encoding="utf8") as file:
            thirukkural = [line.strip() for line in file if line.strip()]

        with open("English_Thirukkural.txt", "r", encoding="utf8") as file:
            english = [line.strip() for line in file if line.strip()]

        with open("Kannada_Thirukkural.txt", "r", encoding="utf8") as file:
            kannada = [line.strip() for line in file if line.strip()]
            
    except FileNotFoundError as e:
        raise RuntimeError(f"Missing file: {e.filename}")


def safe_get(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return "No translation available"


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_data()
    yield


app = FastAPI(
    title="Thirukkural API",
    description="""
    A multilingual API that provides Tamil Thirukkural verses 
    along with English and Kannada translations.
    """,
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)


@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Thirukkural API Home</title>
            <style>
                body { font-family: sans-serif; margin: 40px; line-height: 1.6; }
                pre { background: #f4f4f4; padding: 10px; border-radius: 5px; width: fit-content; }
                a { color: #0066cc; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Thirukkural API</h1>
            <p>Navigate to <a href="/docs">/docs</a> to view the API documentation.</p>

            <div>
                <h2>Available Endpoints</h2>
                <ul>
                    <li><a href="/thirukkural/random">/thirukkural/random</a> - Random Thirukkural Verse</li>
                    <li><a href="/thirukkural/1">/thirukkural/1</a> - Thirukkural Verse by ID (Example: 1)</li>
                </ul>
            </div>

            <div>
                <h2>Endpoint Formats</h2>
                <p>Random Thirukkural Verse:</p>
                <pre>/thirukkural/random</pre>
                <p>Thirukkural Verse by ID:</p>
                <pre>/thirukkural/{kural_id}</pre>
            </div>
        </body>
    </html>
    """



@app.get("/health")
def health():
    return {"status": "API is running"}



@app.get("/thirukkural/random")
def get_random_kural():
    if not thirukkural:
        raise HTTPException(status_code=500, detail="Data not loaded")

    random_index = random.randint(0, len(thirukkural) - 1)

    return {
        "Kural Number": random_index + 1,
        "Tamil Thirukkural": safe_get(thirukkural, random_index),
        "Kannada Translation": safe_get(kannada, random_index),
        "English Translation": safe_get(english, random_index),
    }



@app.get("/thirukkural/{kural_id}")
def get_kural_by_id(kural_id: int):

    if kural_id < 1 or kural_id > len(thirukkural):
        raise HTTPException(status_code=404, detail="Kural not found")

    index = kural_id - 1

    return {
        "Kural Number": kural_id,
        "Tamil Thirukkural": safe_get(thirukkural, index),
        "Kannada Translation": safe_get(kannada, index),
        "English Translation": safe_get(english, index),
    }