import requests

def fetch_top_downloaded_models():
    url = "https://huggingface.co/api/models?sort=downloads&size=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        top_downloaded_models = [model['modelId'] for model in data['models']]
        print("Top 10 Downloaded Models:")
        for idx, model in enumerate(top_downloaded_models, start=1):
            print(f"{idx}. {model}")
    else:
        print("Failed to fetch data from Hugging Face model hub.")

if __name__ == "__main__":
    fetch_top_downloaded_models()

