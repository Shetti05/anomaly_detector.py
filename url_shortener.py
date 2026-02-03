import random
import string

url_db = {}

def shorten_url(long_url):
    short = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    url_db[short] = long_url
    return short

def expand_url(short):
    return url_db.get(short, "URL not found")

if __name__ == "__main__":
    short = shorten_url("https://www.google.com")
    print("Short URL:", short)
    print("Original URL:", expand_url(short))
