from cupcake import get_topic_page, get_top_repositories, write_csv
import sys

def scrape_topic_repositories(topic, path=None):
    """Get the top repositories for a topic and write them to a CSV file"""
    if path is None:
        path = topic + '.csv'
    topic_page_doc = get_topic_page(topic)
    topic_repositories = get_top_repositories(topic_page_doc)
    write_csv(topic_repositories, path)
    print('Top repositories for topic "{}" written to file "{}"'.format(topic, path))
    return path

if __name__ == "__main__":
    topic = sys.argv[1]
    scrape_topic_repositories(topic)