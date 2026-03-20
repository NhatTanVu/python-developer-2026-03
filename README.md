# silverorange Python Developer Assessment

This exercise is designed to assess how you approach tasks required in your
position as Python developer at silverorange. We are interested to see how you
work as well, as what your final results are; include useful Git commit
messages and comments where you think your code may be unclear.

Please do not include your name or any other self-identifying information in
code or commit messages as silverorange will anonymize your work before
reviewing.

## Tasks

Using the provided Django framework, and data fixtures for authors and
posts that are provided:

1.  Create models for posts and authors in the blog app based on the data in
    JSON files.
1.  Write an importer in Python that imports post and author files
    (examples are provided in the `data` folder) into the SQLite database
    configured in the project.
1.  Update the post detail view to load a published post from the
    database with the specified id. Update the post detail template to render
    the post content (title, body, author) as HTML. _The post body is
    formatted as Markdown and the HTML should include the formatted Markdown_.
1.  Update the post index view to load all published posts from the
    database in reverse chronological order. Update the post index template to
    render ths list as HTML. Include the post titles and authors in the output.
    Make clicking a post go to the post details.

## Environment

The application uses Django 6.x and Python 3.12. The Python version is managed
using uv.

## Coding Standard

Please use Python type hints for your code. [Ruff](https://docs.astral.sh/ruff/)
is configured in the project and may be used to format and lint your code:

```sh
uv run ruff check --fix .
uv run ruff format .
```

Django templates can be checked and formatted using djLint:

```sh
uv run djlint . --lint
uv run djlint . --reformat
```

All linting can be checked with:

```sh
make lint-check
make lint-fix
```

## Dependencies

Please use the [uv](https://docs.astral.sh/uv/) tool for dependency
management. You can use any 3rd-party libraries as necessary or as desired in
order to achieve the tasks. Uv can be installed in a variety of ways including
using Brew on macOS.

## Commits

Your commit history is important to us! Try to make meaningful commit messages
that show your progress. **Remember to not include your name or any other
self-identifying information in your commit messages.**

## Getting Started with the Django Application

Provided is a basic Django application with [esbuild](https://esbuild.github.io/)
for compiling CSS assets. To install the required dependencies:

```sh
# Django toolchain
uv sync
# esbuild toolchain
npm install
```

You can then start a development server for Django and esbuild by running the
command:

```sh
make dev
```

You can then access the application on port 8000. The following links can be
used to test:

- http://localhost:8000 - this will verify the application is running.
- http://localhost:8000/posts - the posts index page.
- http://localhost:8000/posts/6ec246b1-ad09-4e03-8573-21e2e779856c - this
  should load a post once the posts are imported and the application is updated.
- http://localhost:8000/asdfghjk - this should show a not-found page.
