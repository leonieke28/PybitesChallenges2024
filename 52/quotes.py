from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]


def _get_quote(qid):
    """Recommended helper"""
    for quote in quotes:
        if quote.get("id") == qid:
            return quote
    else:
        abort(404)


def _quote_exists(existing_quote):
    """Recommended helper"""
    return any(
        quote["quote"] == existing_quote["quote"]
        and quote["movie"] == existing_quote["movie"]
        for quote in quotes
    )


@app.route("/api/quotes", methods=["GET"])
def get_quotes():
    return jsonify({"quotes": quotes}), 200


@app.route("/api/quotes/<int:qid>", methods=["GET"])
def get_quote(qid):
    return jsonify({"quotes": [_get_quote(qid)]})


@app.route("/api/quotes", methods=["POST"])
def create_quote():
    if not request.json or not "quote" in request.json or not "movie" in request.json:
        abort(400)
    if _quote_exists(request.json):
        abort(400)
    quote = {
        "id": quotes[-1]["id"] + 1,
        "quote": request.json["quote"],
        "movie": request.json["movie"],
    }
    quotes.append(quote)
    return jsonify({"quote": quote}), 201


@app.route("/api/quotes/<int:qid>", methods=["PUT"])
def update_quote(qid):
    quote = _get_quote(qid)
    if quote is None:
        abort(404)
    if not request.json or not "quote" in request.json or not "movie" in request.json:
        abort(400)
    quote["quote"] = request.json.get("quote", quote["quote"])
    quote["movie"] = request.json.get("movie", quote["movie"])
    return jsonify({"quote": quote}), 200


@app.route("/api/quotes/<int:qid>", methods=["DELETE"])
def delete_quote(qid):
    quote = _get_quote(qid)
    if quote is None:
        abort(404)
    quotes.remove(quote)
    return jsonify({}), 204
