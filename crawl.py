import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
import pandas as pd

def crawl(time_limit=30, source='github', return_format='csv'):
    PROJECT_NAME = source  # You can change the project name based on the source
    HOMEPAGE = 'http://' + source + '.com/'
    DOMAIN_NAME = get_domain_name(HOMEPAGE)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NUMBER_OF_THREADS = 8
    queue = Queue()
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

    # Create worker threads (will die when main exits)
    def create_workers():
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=work)
            t.daemon = True
            t.start()

    # Do the next job in the queue
    def work():
        while True:
            url = queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            queue.task_done()

    # Each queued link is a new job
    def create_jobs():
        for link in file_to_set(QUEUE_FILE):
            queue.put(link)
        queue.join()
        if return_format == 'csv':
            generate_csv_data()
        elif return_format == 'dict':
            generate_dict_data()

    # Check if there are items in the queue, if so crawl them
    def crawl():
        queued_links = file_to_set(QUEUE_FILE)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the queue')
            create_jobs()

    create_workers()
    crawl()

# Implement functions to generate CSV and dictionary data
def generate_csv_data():
    # For this example, let's assume that you have a list of dictionaries
    # representing crawled data, where each dictionary corresponds to a record.
    crawled_data = [
        {"title": "", "url": "", "content": "This is page 1 content"},
        {"title": "", "url": "", "content": "This is page 2 content"},
        # Add more crawled data as needed
    ]

    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(crawled_data)

    # Save the DataFrame to a CSV file
    df.to_csv('crawled_data.csv', index=False)

def generate_dict_data():
    # For this example, let's assume that you have a list of dictionaries
    # representing crawled data, where each dictionary corresponds to a record.
    crawled_data = [
        {"title": "", "url": "", "content": "This is page 1 content"},
        {"title": "", "url": "", "content": "This is page 2 content"},
        # Add more crawled data as needed
    ]

    # You can return the list of dictionaries directly as the crawled data
    return crawled_data

if __name__ == "__main__":
    crawl(time_limit=30, source='github', return_format='csv')


    # Implement functions to generate CSV and dictionary data

