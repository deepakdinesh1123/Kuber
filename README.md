# steps

- poetry - https://python-poetry.org/

- ```bash
  docker run -d \
      --name kuber-postgres \
      -e POSTGRES_DB=kuber \
      -e POSTGRES_USER=root\
      -e POSTGRES_PASSWORD=root \
      -p 5432:5432 \
      postgres:latest
  ```
- ```shell
    cd rest
    poetry shell
    >>> python manage.py makemigrations
    >>> python manage.py migrate
    python manage.py runserver
  ```

- ```shell
    cd executor
    go run main.go
  ```

````

- ```shell
    cd ui
    npm run dev
````
