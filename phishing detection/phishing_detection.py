import re


SUSPICIOUS_KEYWORDS = [

    "update", "bank", "secure", "account", "verify", "login", "confirm",

    "urgent", "password", "webscr", "ebayisapi", "signin", "click"

]


def is_suspicious_url(url):

    url = url.lower()

    # Basic heuristics: suspicious keywords, IP address instead of domain, multiple dots

    if any(keyword in url for keyword in SUSPICIOUS_KEYWORDS):

        return True

    if re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url):

        return True

    if url.count('.') > 3:

        return True

    return False



def detect_phishing(text):

    # Extract URLs

    urls = re.findall(r'(https?://[^\s]+)', text)

    flagged = []

    for url in urls:

        if is_suspicious_url(url):

            flagged.append(url)

    if flagged:

        return True, flagged

    return False, []



def main():

    print("Phishing Detection Tool")

    print("Paste email or text content below (end input with an empty line):")

    lines = []

    while True:

        line = input()

        if not line.strip():

            break

        lines.append(line)

    content = '\n'.join(lines)


    suspicious, flagged_urls = detect_phishing(content)

    if suspicious:

        print("Warning: Potential phishing URLs detected:")

        for url in flagged_urls:

            print(f" - {url}")

    else:

        print("No phishing URLs detected.")



if __name__ == "__main__":

    main()
