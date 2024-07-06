import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching : {res.status_code}")
    return res


def read_response(response):
    print(response.text)


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    query = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5, tail = query[:5], query[5:]
    res = request_api_data(first_5)
    # print(first_5, tail)
    leak_count = get_password_leaks_count(res, tail)
    # print(leak_count)
    return leak_count


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was leaked {count} times...")
        else:
            print(f"{password} is safe")

    return "done!"


main(sys.argv[1:])
