"""Index/index/__init.py."""
import os
import flask

app = flask.Flask(__name__)  # pylint: disable=invalid-name
app.config["INDEX_PATH"] = os.getenv("INDEX_PATH", "inverted_index_1.txt")
import index.api  # noqa: E402  pylint: disable=wrong-import-position
