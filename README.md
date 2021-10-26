# Flask Mongo

A flask + mongodb api.

## How to run
- The project suppose to use a local version of mongodb


1. Create a virtual env
```bash
# Windows
python -m venv venv
```

2. Activate the virtual env
```
# Windows
venv\Scripts\activate
```

3. Install flask
```
pip install Flask
```

4. Run mongodb in another terminal
```
mongod
```

5. Execute flask
```
flask run
```

## Endpoints

GET `/games`

Show the list of all the games

POST `/games`

Create a new game like the example below

```json
{
	"name": "game name"
}
```

DELETE `/games/id`

Delete the given element