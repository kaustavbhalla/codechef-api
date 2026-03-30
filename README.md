# codechef-api

An unofficial REST API for CodeChef. Since CodeChef doesn't offer a public API, this project scrapes their website and exposes the data as clean, typed JSON endpoints — built for developers who want to integrate CodeChef data into their apps, portfolios, or tools.

Inspired by [alfa-leetcode-api](https://github.com/alfaarghya/alfa-leetcode-api).

---

## Base URL

```
https://codechef-api-oaus.onrender.com
```

## API Reference

Interactive docs available at `/docs` (Swagger UI).

---

### Get User Profile

```
GET /api/v1/users/{username}
```

Returns public profile data for a CodeChef user.

**Example**

```bash
curl https://your-service.onrender.com/api/v1/users/kaustavbhalla
```

**Response**

```json
{
  "name": "Kaustav Bhalla",
  "userName": "kaustavbhalla",
  "country": "India",
  "typeOf": "Student",
  "institution": "USICT",
  "rating": 1823,
  "division": "Division 2",
  "stars": 4,
  "globalRank": 1420,
  "countryRank": 312,
  "contestsParticipated": 18
}
```

**Error Responses**

| Status | Meaning                               |
| ------ | ------------------------------------- |
| `404`  | User not found on CodeChef            |
| `502`  | CodeChef HTML changed, parsing failed |
| `500`  | Internal server error                 |

---

## Self-hosting

**With Docker**

```bash
git clone https://github.com/yourusername/codechef-api
cd codechef-api
docker compose up -d
```

API will be available at `http://localhost:8000`.

**Without Docker**

```bash
git clone https://github.com/yourusername/codechef-api
cd codechef-api
pip install uv
uv sync
uv run uvicorn app.main:app --reload
```

---

## Stack

- [FastAPI](https://fastapi.tiangolo.com/) — API framework
- [httpx](https://www.python-httpx.org/) — Async HTTP client
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing
- [Pydantic](https://docs.pydantic.dev/) — Data validation
- [Docker](https://www.docker.com/) — Containerization

---

## Roadmap

- [x] User profile
- [ ] Contest list (upcoming, ongoing, past)
- [ ] Contest standings
- [ ] User submission history
- [ ] Problem details
- [ ] User rating history

---

## Contributing

Contributions are welcome. If an endpoint breaks because CodeChef changed their HTML, please open an issue with the endpoint name and the error you're seeing.

1. Fork the repo
2. Create a branch: `git checkout -b feature/endpoint-name`
3. Commit your changes
4. Open a pull request

---

## Disclaimer

This project is not affiliated with or endorsed by CodeChef. It scrapes publicly available data for developer use. Use responsibly and avoid sending excessive requests.

---

## License

MIT
