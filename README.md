# Matchflix API
Webservice for Matchflix app

## Backend local development, additional details

### General workflow
By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.
From project root dir you can install all dependencies with:
```shell
$ poetry install
```
Then you can start a shell session with the new environment with:

```shell
$ poetry shell
```
Make sure your editor uses the environment you just created with Poetry. You can get the virtualenv path with:
```shell
$ poetry env info -p
```


### Migrations
Make sure you create a "revision" of your models and that you "upgrade" your database with that revision every time you change them. As this is what will update the tables in your database. Otherwise, your application will have errors.

- If you created a new model in ./matchflix/models/, make sure to import it in ./matchflix/db/base.py, that Python module (base.py) that imports all the models will be used by Alembic.

- After changing a model (for example, adding a column), inside the container, create a revision, e.g.:

```shell
$ alembic revision --autogenerate -m "Add column last_name to User model"
```
- Commit to the git repository the files generated in the alembic directory.

- After creating the revision, run the migration in the database (this is what will actually change the database):
```shell
$ alembic upgrade head
```