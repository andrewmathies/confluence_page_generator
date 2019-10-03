import base64

def encodeKey(email, key):
    string = email + ':' + key
    encodedAuth = base64.b64encode(string.encode('utf-8'))
    return 'Basic ' + encodedAuth.decode('utf-8')