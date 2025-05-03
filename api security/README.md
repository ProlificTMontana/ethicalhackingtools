How it works:

Sends various HTTP requests to a RESTful API endpoint to test its security aspects, including HTTP status codes, presence of authentication, data leakage via URL parameters, allowed methods via OPTIONS, and a naive rate limiting test by sending repeated requests.

How to use:

Run with API URL argument:
python api_security_tester.py https://example.com/api/resource
It prints the results of each test to help identify security issues.
