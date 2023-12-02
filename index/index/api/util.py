"""Utility functions."""
import re
import index


def read_stopwords(index_dir):
    """Read stopwords."""
    file_name = "/".join([str(index_dir), "stopwords.txt"])
    stopwords = 0
    with open(file_name, "r", encoding="utf-8") as text_file:
        stopwords = text_file.read()
    stopwords = re.sub(r'\n^$', '', stopwords, flags=re.MULTILINE)
    stopwords = re.split('\n', stopwords)
    return stopwords


def read_pagerank(index_dir):
    """Read pagerank."""
    file_name = "/".join([str(index_dir), "pagerank.out"])
    pagerank_data = {}
    with open(file_name, "r", encoding="utf-8") as file:
        for row in file.readlines():
            row = row.split(',')
            # Key = doc_id, Value = score
            row[1] = float(row[1])
            pagerank_data[int(row[0])] = row[1]
    return pagerank_data


def read_inverted_index(index_dir):
    """Read inverted index."""
    file_name = "/".join([str(index_dir), "inverted_index/",
                          index.app.config["INDEX_PATH"]])
    mydict, doc_norm = {}, {}
    with open(file_name, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split()
            # (f"{word}\t{idf} {doc_id} {tf} {norm_factor}")
            word, idf = line[0], float(line[1])
            num_list = (len(line)-2) // 3
            doc_list = {}
            for i in range(num_list):
                doc_id, term_freq, norm_factor = \
                                          int(line[3*i+2]), \
                                          int(line[3*i+3]), \
                                          float(line[3*i+4])
                doc_list[doc_id] = {"doc_id": doc_id,
                                    "tf": term_freq,
                                    "norm_factor": norm_factor}
                if doc_id not in doc_norm:
                    doc_norm[doc_id] = norm_factor
            mydict[word] = {"word": word,
                            "idf": idf,
                            "doc_list": doc_list}
    index.app.config["doc_norm"] = doc_norm
    return mydict
