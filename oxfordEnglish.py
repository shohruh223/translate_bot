import requests
from pprint import pprint as print

from utils import APP_ID, APP_KEY
#
app_id = APP_ID
app_key = APP_KEY
language = "en-gb"

word_id = "orange"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()


r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# print(r.status_code)
# response = r.json()
# print(response)

# audio = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
# definition = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']


def get_definitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    response = r.json()
    if 'error' in response.keys():
        return False

    output = {}
    senses = response['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(sense['definitions'][0])
    output['definitions'] = '\n'.join(definitions)

    if response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output


if __name__ == '__main__':
    print(get_definitions('ism'))