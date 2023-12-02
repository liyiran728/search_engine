"""Main.py."""
import pathlib
import re
from math import sqrt
from flask import jsonify, request
import index
from index.api.util import read_stopwords, read_pagerank, read_inverted_index
# Import g from flask in line 1 allows global variables in startup


@index.app.before_first_request
def startup():
    """Load inverted index, pagerank, and stopwords into memory."""
    # p5-search-engine/index/index
    index_dir = pathlib.Path(__file__).parent.parent
    # Store list of stopwords
    index.app.config["stopwords"] = read_stopwords(index_dir)
    # Store dictionary with key = doc_id, value = pagerank score
    index.app.config["pagerank"] = read_pagerank(index_dir)
    index.app.config["inverted_index"] = read_inverted_index(index_dir)


@index.app.route('/api/v1/', methods=['GET'])
def get_api_v1():
    """Show /api/v1/."""
    task = {
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    }
    return jsonify(task)


@index.app.route('/api/v1/hits/', methods=['GET'])
def get_api_v1_hits():
    """Show /api/v1/hits/."""
    # The weight of PageRank in the score is specified
    # by the optional parameter w=<weight>.
    # If w=<weight> is not specified, use the default value of 0.5.
    weight = request.args.get("w", type=float, default=0.5)
    # query is specified by the parameter q=<query>
    query = request.args.get("q", type=str)
    # Clean the query input
    # Remove non alphanumeric characters
    query = re.sub(r"[^a-zA-Z0-9 ]+", "", query)
    # Make all text lowercase
    query = query.casefold()
    # Split text into whitespace-delimited terms
    query = query.split()
    # Remove stopwords
    newquery = []
    for word in query:
        if word not in index.app.config["stopwords"]:
            newquery.append(word)
    # Count query frequency
    query, newquery = newquery, {}
    for word in query:
        if word not in newquery:
            newquery[word] = query.count(word)
    query = newquery
    context = calculate_score(query, weight)
    return jsonify({"hits": context})


def calculate_score(query, weight):
    """Calculate score for hits."""
    retlist = []
    # Count query normalization factor
    qnorm_factor = 0
    for word, term_freq in query.items():
        if word not in index.app.config["inverted_index"]:
            # not found in index, return empty list
            return []
        idf = index.app.config["inverted_index"][word]["idf"]
        qnorm_factor += (term_freq*idf)**2
    qnorm_factor = sqrt(float(qnorm_factor))
    # Get Score for document
    for docid, doc_norm in index.app.config["doc_norm"].items():
        has_word = True
        tfidf = 0
        pagerank = index.app.config["pagerank"][docid]
        for word in query:
            word_with_doc = \
                            index.app.config[
                                "inverted_index"][word]["doc_list"]
            if docid not in word_with_doc:
                has_word = False
                break
            term_freq = word_with_doc[docid]["tf"]
            idf = index.app.config["inverted_index"][word]["idf"]
            tfidf += term_freq*idf*query[word]*idf
        if not has_word:
            continue
        tfidf = float(tfidf) / qnorm_factor / sqrt(doc_norm)
        score = weight*pagerank + float(1-weight)*tfidf
        retlist.append({
            "docid": docid,
            "score": score
        })
    retlist.sort(reverse=True, key=compare_score)
    return retlist


def compare_score(item):
    """Compare score."""
    return item["score"]
