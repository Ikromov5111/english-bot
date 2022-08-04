import requests

app_id = "2e4d67ee"
app_key = "a96431389d0cb4c49ac6ae22f3e1f346"
language = 'en-gb'

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key":app_key})
    response = r.json()

    if 'error' in response.keys():
        return False

    output = {}
    senses= response['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"--| {sense['definitions'][0]}")

    output['definitions'] = "\n".join(definitions)

    if response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output


if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinitions('Great Britain'))
    print(getDefinitions('america'))

