# Polython Backend

### Backend system for Polython App

To get the project just type

```bash
git clone https://github.com/aaroncadillac/polython-backend
```

To setup the python local environment we'll use Docker and docker-compose so, you must have them already installed.

Ensure .env file with environmental variables exists and is placed in the root folder.

#### Example

```
DB_USER=<db_user>
DB_PASSWORD=<db_password>
DB_HOST=<db_host>
DB_NAME=<db_name>
DB_PORT=<db_port>
EMAIL_USER=<email_user>
EMAIL_PASSWORD=<email_password>
```


Now let's create the environment

```bash
docker-compose build
docker-compose up
```

And open your browser in http://localhost:8000/


## Endpoints

### Users

#### Create

```bash
POST /users/create/
```

Params:

```json
{
	"username": "pepito"
	"password": "purocarteldesantaalvcompa",
	"email": "pepito@polython.com"
}
```

Returns new user ID.

#### Login

```bash
POST /users/login/
```

Params:

```json
{
	"username": "pepito",
	"password": "purocarteldesantaalvcompa"
}
```

Returns a ok message if all goes well.

#### Detail

```json
GET /users/<user_id>/
```

Returns a the user information.

#### Logout

```json
GET /users/logout/
```

Returns a bye message if all goes well.

### Stores

#### Create

```bash
POST /stores/create/
```

Params:

```json
{
	"name": "La Conchita"
}
```

Returns new store ID.

#### Detail

```json
GET /stores/<store_id>/
```

Returns store information.

#### Add Products

```json
POST /stores/product/add/
```

```json
{
	"store_id": "4bd56f7c-532d-45e0-b593-652db9b4ab96",
	"products": [{
		"name": "chanclas2",
		"price": 80.5
	}]
}
```

Returns store information.

### Sales

#### Create

```bash
POST /sales/create/
```

Params:

```json
{
	"store_id": "4bd56f7c-532d-45e0-b593-652db9b4ab96",
	"total_amount": 50,
	"products": [
		{"id": "b0f95026-44e2-4b21-af36-96ab6a79f751",
		"quantity": 3
		}]
}
```

Returns new store ID.


#### Update

```bash
POST /sales/update/<sale_id>/
```

Params:

```json
{
	"status": "ACCEPTED"
}
```

or could be:

```json
{
	"status": "REFUSED"
}
```

Returns ok if sale instance update is correct.

