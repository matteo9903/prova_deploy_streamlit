import requests

# IP of LLAMA server
LLAMA_IP = 'http://10.30.83.223:8080'

#  Function to get the response from the LLAMA server
def answer_message(message: dict):
    
    url = f'{LLAMA_IP}/answerMessage'
    
    print("------------")
    print(f"Making request to the API {url}")
    print("------------")
    response = requests.post(url = url, json=message)
    answer = response.json()['response']
    
    return answer
    

