# Todo API

Todo API and fully opertional CURD API developed in Django Rest Framework. you can use it in any frontend project you like to use it.


## Authors

- [@sohailraoufi](https://www.github.com/SohailRaoufi)


## API Reference

#### Get all items

```http
  GET /api/
```

| Parameter | Type    
| :-------- | :------- 
| `api_key` | `string` 

#### Get item

```http
  GET /api/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Update an item

```http
  PUT /api/update/${id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Update(Patch) a specific field of Todo

```http
  PATCH /api/update/${id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### Create(POST) a Todo

```http
  POST /api/create/
```

#### Delete a Todo

```http
  DELETE /api/Delete/${id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |
## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt
```
```bash
  pip manage.py migrate
```
```bash
  pip manage.py runserver
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`



