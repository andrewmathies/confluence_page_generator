post_kwargs = {
    'headers': {
        'Content-Type': 'application/json',
        'Authorization': ''
    },
    'json': {
        "type": "page",
        "title": "",
        "space": {
            "key": ""
        },
        "ancestors": [
            {
                "id": ""
            }
        ],
        "body": {
            "storage": {
                "value": "",
                "representation": "storage"
            }
        }
    }
}

get_kwargs = {
    'headers': {
        'Content-Type': 'application/json',
        'Authorization': ''
    },
    'params': {
        "spaceKey": "",
        "limit": "1000"
    }
}

descendant_kwargs = {
    'headers': {
        'Content-Type': 'application/json',
        'Authorization': ''
    },
    'params': {
        'limit': '1000'
    }
}

delete_kwargs = {
    'headers': {
        'Content-Type': 'application/json',
        'Authorization': ''
    }
}