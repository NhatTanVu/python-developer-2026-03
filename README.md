# silverorange Python Developer Assessment

## Introduction

This exercise is designed to assess how you approach tasks required in your
position as Python developer at silverorange. We are interested to see how you
work as well, as what your final results are; include useful Git commit
messages and comments where you think your code may be unclear.

If you have any questions about the exercise, please reach out to us!

Please do not include your name or any other self-identifying information in
code or commit messages as silverorange will anonymize your work before
reviewing.

## Project Setup

This project uses **uv** to manage Python dependencies and Python versions. You
will need [uv installed](https://docs.astral.sh/uv/getting-started/installation/)
to initialize and run the project. If you are using macOS you can install uv
using Homebrew:

```sh
brew install uv
```

Once uv is installed, you can sync and migrate the included Django project:

```sh
uv sync
uv run python manage.py migrate
```

Client-side assets are managed using [esbuild](https://esbuild.github.io/).
This toolchain is managed using NPM. NPM is bundled with Node.js, which can
also be installed using Homebrew:

```sh
brew install node
```

Once NPM is available, install dependencies using NPM:

```sh
npm install
```

With dependencies installed, you can run the project using the following
command. This will run the Django development server as well as an esbuild file
watcher:

```sh
make dev
```

With the development server running, you can access the application on port 8000. The following links can be used to test:

- http://localhost:8000 - this will verify the application is running.
- http://localhost:8000/posts - the posts index page.
- http://localhost:8000/posts/6ec246b1-ad09-4e03-8573-21e2e779856c - this
  should load a post once the posts are imported and the application is updated.
- http://localhost:8000/asdfghjk - this should show a not-found page.

## Tasks

Using the provided Django project, and provided data fixtures for authors and
posts:

1.  Create models for _posts_ and _authors_ in the blog app based on the data in
    JSON files.
1.  Write an importer in Python that imports post and author data files from the
    `data` into the SQLite database configured in the Django project.
1.  Update the post _index_ view to load all published posts from the
    database in reverse chronological order.
    - Update the template to render this list as HTML.
    - Include the post titles and authors in the output.
    - Make clicking a post go to the post details.
1.  Add a post _detail_ route to the blog app that will load a published post
    from the database from the id in the URL.
    - The URL path should be of the form `posts/[id]`.
    - The view and template should render the post content (title, body,
      author) as HTML.
    - If the requested post is unavailable, show a 404 page.
    - **The post body is formatted as Markdown and the HTML should include the
      formatted Markdown.**
1.  Add basic CSS to the _index_ and _detail_ views. The SCSS file
    `static/src/main.scss` is set up as the main entrypoint for the index view
    and can be used on the detail view as well.
    - Use modern CSS best practices.
    - If you know SCSS you may use SCSS features where appropriate, but they are
      not required.
    - No designs are provided. Do your best to make these basic pages visually
      appealing.

## Success Criteria

We will evaluate your anonymized implementation based on the following criteria:

- Modern Python best practices
- Code legibility
- Correctness of task implementation
- Use of provided tools
- Error handling and security
- CSS implementation
- Testability of implementation and/or testing

## Coding Standard

Please use Python type hints for your code. [Ruff](https://docs.astral.sh/ruff/)
is configured in the project and may be used to format and check your code.
Django templates can be checked and formatted using
[djLint](https://djlint.com/). Both tools can be called using Makefile targets:

```sh
make lint-check
make lint-fix
```

## Commits

Your commit history is important to us! Try to make meaningful commit messages
that show your progress. **Remember to not include your name or any other
self-identifying information in your commit messages.**
