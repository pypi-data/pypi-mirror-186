import uuid
import tldextract


"""Given a record, finds the id given rules
"""


def normalize_id(record):
    """
    """

    record_type = record.get('@type', None)
    record_id = record.get('@id', None)
    
    # ContactPoint:
    if record_type in ['schema:Person', 'schema:ContactPoint']:
        record_id = find_id_by_email(record)
        if record_id:
            return record_id

    # if webpage
    elif record_type in ['schema:Organization', 'schema:WebPage', 'schema:SearchAction', 'schema:WebAPI']:
        record_id = find_id_by_url(record)
        if record_id:
            return record_id

    # if website
    elif record_type in ['schema:WebSite']:
        record_id = find_id_by_domain(record)
        if record_id:
            return record_id

    # if image
    elif record_type in ['schema:ImageObject', 'schema:VideoObject']:

        record_id = find_id_by_hash(record)
        if record_id:
            return record_id
            
        record_id = find_id_by_contenturl(record)
        if record_id:
            return record_id

        record_id = find_id_by_url(record)
        if record_id:
            return record_id


    elif record_type in ['schema:Brand', 'schema:Organization']:

        record_id = find_id_by_name(record)
        if record_id:
            return record_id

    
    else:
        record_id = find_id_by_url(record)
        if record_id:
            return record_id

    return None


def find_id_by_hash(record):

    record_type = record.get('@type', None)
    record_id = record.get('@id', None)
    sha256 = record.get('schema:sha256', None)

    sha256 = process_value_list(sha256)
    
    return sha256


def find_id_by_name(record):


    record_type = record.get('@type', None)
    record_id = record.get('@id', None)
    name = record.get('schema:name', None)
    name = process_value_list(name)
    
    
    return name
    
    
def find_id_by_url(record):

    record_type = record.get('@type', None)
    record_id = record.get('@id', None)
    url = record.get('schema:url', None)
    
    url = process_value_list(url)
    
    if not url:
        return None
    
    new_record_id = str(uuid.uuid3(uuid.NAMESPACE_URL, url))
    
    return new_record_id

    
def find_id_by_contenturl(record):

    record_type = record.get('@type', None)
    record_id = record.get('@id', None)
    contentUrl = record.get('schema:contentUrl', None)

    contentUrl = process_value_list(contentUrl)

    if not contentUrl:
        return None
    
    new_record_id = str(uuid.uuid3(uuid.NAMESPACE_URL, contentUrl))
    return new_record_id
    

def find_id_by_domain(record):

    record_type = record.get('@type', None)
    record_id = record.get('@id', None)
    url = record.get('schema:url', None)

    url = process_value_list(url)
    if not url:
        return None

    ext = tldextract.extract(url)
    domain = ext.registered_domain

    new_record_id = domain
    return new_record_id


def find_id_by_email(record):

    record_type = record.get('@type', None)
    record_id = record.get('@id', None)
    email = record.get('schema:email', None)

    email = process_value_list(email)
    
    return email


def process_value_list(value):
    """Verifies if value is list, if so dedupe, removes NUll and returns value if only one value left
    """

    if not isinstance(value, list):
        value = [value]

    # Dedupe
    value = list(set(value))

    # Remove blank
    new_value = []
    for i in value:
        if i:
            new_value.append(i)

    # Return element if unique
    if len(value) == 1:
        return value[0]
    else:
        return None
            