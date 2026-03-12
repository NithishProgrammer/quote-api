# Quact API

**Quact API** is a simple and lightweight REST API that provides **random Quotes and Facts**.  
It is built using **FastAPI** and served with **Uvicorn**.

This API is designed for developers who want to easily integrate **motivational quotes** or **interesting facts** into their applications.

---

## Base URL
https://quote-api-qjk6.onrender.com
 (NO API KEY NEEDED)


---

## API Endpoints

### 1. Random Quote

Endpoint
https://quote-api-qjk6.onrender.com/quote


Example Response:

json
{
  "Quote": "Your habits shape your future"
}

### 2. Random Fact

Endpoint

GET /fact

Full URL

https://quote-api-qjk6.onrender.com/fact

Example Response

{
  "Fact": "Octopuses have three hearts"
}


### Usage Example (JS) :
fetch("https://quote-api-qjk6.onrender.com/quote")
  .then(res => res.json())
  .then(data => console.log(data.Quote));
  
### Tech Stack

Python

FastAPI

Uvicorn

Notes

This is a free API, so usage may have limits depending on server resources.

### Developer

Created by NITHISH

Portfolio
https://nithishprogrammer.github.io/Nithish/
