import requests

import sys


def test_api(url):

    print(f"Testing API endpoint: {url}")


    # 1. Check status code for GET

    try:

        r = requests.get(url, timeout=5)

        print(f"GET request status: {r.status_code}")

    except Exception as e:

        print("GET request failed:", e)

        return


    # 2. Check for presence of authentication header in response

    auth_headers = ['WWW-Authenticate', 'Authorization']

    has_auth = any(h in r.headers for h in auth_headers)

    print("Authentication required:" , has_auth)


    # 3. Check for data leakage by modifying URL parameters

    if '?' in url:

        test_url = url + '&testparam=123'

    else:

        test_url = url + '?testparam=123'

    try:

        r2 = requests.get(test_url, timeout=5)

        if 'testparam=123' in r2.text:

            print("Potential data leakage: parameters reflected in response")

    except Exception as e:

        print("Request with parameter failed:", e)


    # 4. Check allowed methods

    try:

        r_options = requests.options(url, timeout=5)

        allowed = r_options.headers.get('Allow', 'Unknown')

        print("Allowed methods:", allowed)

    except Exception as e:

        print("OPTIONS request failed:", e)


    # 5. Basic rate limiting check (send 10 quick requests)

    success_responses = 0

    for i in range(10):

        try:

            r_temp = requests.get(url, timeout=3)

            if r_temp.status_code == 200:

                success_responses += 1

        except:

            break

    if success_responses < 10:

        print("Potential rate limiting detected.")

    else:

        print("No rate limiting detected.")


def main():

    if len(sys.argv) < 2:

        print("Usage: python api_security_tester.py <API endpoint URL>")

        return


    test_api(sys.argv[1])



if __name__ == "__main__":

    main()
