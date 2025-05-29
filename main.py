import requests, json

from responseClass import ResponseClass

def getApiKey():
    with open("openrouterapi.txt", "r") as file:
        for line in file:
            return line
        
def main():
    key = getApiKey()

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "model": "deepseek/deepseek-r1-0528:free",
        "messages": [
            {
                "role": "user",
                "content": "What is your name?"
            },
            {
                "role": "user",
                "content": "Do you know how I'm talking to you?"
            }
        ]
    })

    response = requests.post(
        url=url,
        headers=headers,
        data=data
    )

    respObj = ResponseClass.from_response(response)

    # accessing fields
    print(respObj.id)
    print(respObj.choices[0].message.content)

    # convert back to json to print
    print(respObj.to_json())



main()