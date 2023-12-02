"""Ask485 index (main) view."""
import heapq
import threading
import flask
import requests
import search


@search.app.route('/', methods=['GET'])
def show_search():
    """Display / route."""
    context = {
        "results": [],
        "weight": 0.5,
        "query": "",
        "query_none": True
    }
    results = context["results"]
    # Get argument from search form
    query = flask.request.args.get('q', default=None, type=str)
    weight_str = flask.request.args.get('w', default='0.5', type=str)
    weight = float(weight_str)
    if query == "":
        context["query_none"] = False
        context["weight"] = weight
    elif query is not None:
        # Query the three index servers
        index_url_list = get_index_url(weight, query)
        threads = []
        # Make 3 lists to take results from 3 servers
        lists = [[], [], []]
        for num in range(3):
            thread = threading.Thread(target=send_requests,
                                      args=(index_url_list[num], lists, num))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        # merge 3 sorted list with the score as key
        merged_list = heapq.merge(
                                  lists[0], lists[1], lists[2],
                                  key=lambda result: result["score"],
                                  reverse=True)
        final_list = list(merged_list)
        # Only take the top 10 results
        top_ten = final_list[:10]
        for doc in top_ten:
            docid = doc["docid"]
            # Get info from database
            results.append(get_docinfo(docid))
        # Render search template with context
        context["weight"] = weight_str
        context["query"] = query
        context["query_none"] = False
    return flask.render_template("search.html", **context)


def send_requests(url, lists, num):
    """Send request to specified url and append results to list."""
    data = requests.get(url)
    results = data.json()
    lists[num] = results["hits"]
    return lists[num]


def get_index_url(weight, query):
    """Return url with weight and query appended."""
    query_list = query.split()
    query_str = "+".join(query_list)
    arg_str = f"?w={weight}&q={query_str}"
    # arg_str = "?w={}&q={}".format(weight, query_str)
    index_url_list = []
    for url in search.app.config["SEARCH_INDEX_SEGMENT_API_URLS"]:
        index_url_list.append(str(url) + arg_str)
    return index_url_list


def get_docinfo(docid):
    """Return url, title, and summary for a docid."""
    # Connect to database
    connection = search.model.get_db()
    # Query database
    cur = connection.execute(
        "SELECT url, title, summary FROM Documents WHERE docid=?", (docid,)
    )
    doc = cur.fetchone()
    # Constuct result
    url = str(doc["url"]).strip()
    title = str(doc["title"]).strip()
    summary = str(doc["summary"]).strip()
    result = {
        "doc_url": url,
        "doc_title": title,
        "doc_summary": summary
    }
    return result
