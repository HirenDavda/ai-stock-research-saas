import requests

BASE_URL = "http://localhost:8000"


def test_health():

    response = requests.get(
        f"{BASE_URL}/api/health/health"
    )

    print("Health Status:",
          response.status_code)

    print(response.json())


def test_upload():

    files = {
        "file": open(
            "/Users/hiren/Desktop/sample.txt",
            "rb"
        )
    }

    response = requests.post(
        f"{BASE_URL}/api/upload/upload-document",
        files=files
    )

    print("Upload Status:",
          response.status_code)

    print(response.json())


def test_ask():

    payload = {
        "question": "What is revenue?"
    }

    response = requests.post(
        f"{BASE_URL}/api/chat/ask",
        json=payload
    )

    print("Ask Status:",
          response.status_code)

    print(response.json())


if __name__ == "__main__":

    print("Running Smoke Tests...\n")

    test_health()

    print()

    test_upload()

    print()

    test_ask()