import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Enter image URLs separated by commas: ").split(",")
    urls = [url.strip() for url in urls]  # clean spaces

    os.makedirs("Fetched_Images", exist_ok=True)
    downloaded_files = set()  # track duplicates

    MAX_SIZE = 5 * 1024 * 1024  # 5 MB max

    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Check if content is an image
            if "image" not in response.headers.get("Content-Type", ""):
                print(f"✗ Skipping non-image URL: {url}")
                continue

            # Extract filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"

            # Check for duplicates
            if filename in downloaded_files or os.path.exists(os.path.join("Fetched_Images", filename)):
                print(f"✗ Skipping duplicate: {filename}")
                continue
            downloaded_files.add(filename)

            # Check file size
            if len(response.content) > MAX_SIZE:
                print(f"✗ Skipping {filename}: file too large")
                continue

            # Save image
            filepath = os.path.join("Fetched_Images", filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}\n")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
