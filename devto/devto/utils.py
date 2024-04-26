import re
import csv


def remove_html_tags(text):
    html_pattern = re.compile('<.*?>')
    clean_text = re.sub(html_pattern, '', text)
    return clean_text


def is_exist(doc_id):
    reader = csv.reader(open('data.csv', 'r'))
    for data in reader:
        if doc_id == data[0]:
            return True
    return False


fields = ['doc_id', 'title', 'author', 'publish_date']


def write_data(**kwargs):
    with open('data.csv', 'a+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        # writer.writeheader()
        writer.writerow(kwargs)


def write_document(response, doc_id, css_tag):
    body = remove_html_tags(response.css(css_tag).getall()[0])
    body.strip()
    with open(f'documents/{doc_id}.txt', 'w') as file:
        file.write(body)
        file.close()
