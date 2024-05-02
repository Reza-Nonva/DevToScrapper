import json
import re


def clean_text(text):
    """Remove HTML tags and extra whitespace from a string."""
    # Remove HTML tags
    clean_text = re.sub(r'<[^>]*>', '', text)
    # Remove extra whitespace and empty lines
    clean_text = re.sub(r'\n\s*\n', '\n', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    return clean_text.strip()


def is_exist(doc_id):
    """Check if a document ID exists in the 'doc_id.txt' file."""
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
    """save document ID in doc_id.txt file to prevent fetching the same page again"""
    try:
        with open('doc_id.txt', 'a+') as file:
            file.write(doc_id + '\n')
    except IOError as e:
        print("Error: Could not write to file:", e)


def save_doc_body(response, css_tag, **kwargs):
    body = clean_text(response.css(css_tag).getall()[0])
    data = {key: value for key, value in kwargs.items()}
    data['body'] = body

    with open(f'documents/{kwargs.get("doc_id")}.json', 'w') as file:
        json.dump(data, file, indent=4)

    # Save crawled pages paragraphs to file
    with open('crawled_posts.txt', 'a+') as file:
        paragraphs = response.css(css_tag + '>p::text').getall()
        for paragraph in paragraphs:
            file.write(paragraph + '\n')
