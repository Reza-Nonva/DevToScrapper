import json
import re
import csv


def remove_html_tags(text):
    html_pattern = re.compile('<.*?>')
    clean_text = re.sub(html_pattern, '', text)
    return clean_text


def is_exist(doc_id):
    """
    Check if a document ID exists in the 'doc_id.txt' file.
    """
    try:
        with open('doc_id.txt', 'r') as file:
            for line in file:
                if line.strip() == doc_id:
                    return True
        return False
    except Exception as e:
        print("Error:", e)
        return False


def save_doc_id(doc_id):
    """
    save document ID in doc_id.txt file to prevent fetching the same pagr again
    """
    try:
        with open('doc_id.txt', 'a+') as file:
            file.write(doc_id + '\n')
    except IOError as e:
        print("Error: Could not write to file:", e)


def save_doc_body(response, css_tag, **kwargs):
    body = remove_html_tags(response.css(css_tag).getall()[0])
    body = body.strip()
    data = {
        'doc_id': kwargs.get('doc_id'),
        'title': kwargs.get('title'),
        'author': kwargs.get('author'),
        'tags': kwargs.get('tags'),
        'publish_date': kwargs.get('publish_date'),
        'body': body,
    }

    with open(f'documents/{kwargs.get("doc_id")}.json', 'w') as file:
        json.dump(data, file, indent=4)
