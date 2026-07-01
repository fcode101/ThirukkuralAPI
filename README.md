# Thirukkural API

A lightweight, high-performance multilingual REST API built with **FastAPI** that provides access to all **1,330 Thirukkural** verses. The API returns the original Tamil verse along with its English and Kannada translations.

---

## Features

- Multilingual support (Tamil, English, Kannada)
- FastAPI-powered REST API
- Loads datasets into memory during startup for faster responses
- Interactive API documentation with Swagger UI and ReDoc
- Input validation and error handling
- Random Thirukkural endpoint
- Retrieve any Kural by its number (1–1330)
- Health check endpoint

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ThirukkuralAPI.git
cd ThirukkuralAPI
```

### 2. Create a Virtual Environment (Optional)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install "fastapi[standard]"
```

or

```bash
pip install -r requirements.txt
```

### 4. Add Dataset Files

Place the following files in the project root:

```
Tamil_Thirukkural.txt
English_Thirukkural.txt
Kannada_Thirukkural.txt
```

### 5. Run the API

```bash
fastapi dev main.py
```

Server:

```
http://127.0.0.1:8000
```

## Project Structure

```text
ThirukkuralAPI/
├── main.py
├── Tamil_Thirukkural.txt
├── English_Thirukkural.txt
├── Kannada_Thirukkural.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Landing page |
| GET | `/health` | Health check |
| GET | `/thirukkural/random` | Get a random Thirukkural |
| GET | `/thirukkural/{kural_id}` | Get a Thirukkural by ID (1–1330) |

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

## Example Response

```json
{
  "Kural Number": 1,
  "Tamil Thirukkural": "அகர முதல எழுத்தெல்லாம் ஆதி\nபகவன் முதற்றே உலகு.",
  "Kannada Translation": "ಅಕ್ಷರಗಳು ಅಗರದಿಂದ ಆರಂಭವಾಗುತ್ತವೆ. ಹಾಗೆಯೇ ಜಗತ್ತು ಆದಿಭಗವಾನನಿಂದ ಆರಂಭವಾಗುತ್ತದೆ.",
  "English Translation": "As the letter A is the first of all letters, so the Eternal God is first in the world."
}
```

## License

This project is licensed under the MIT License.


---


Made with ❤️🫰
