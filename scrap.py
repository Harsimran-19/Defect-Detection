import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_image(url, folder):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # Extract the file name from the URL
        file_name = os.path.join(folder, url.split("/")[-1])
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download image from: {url}")

def scrape_rust_images(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                download_image(img_url, folder)

if __name__ == "__main__":
    # Replace 'https://example.com' with the actual URL you want to scrape
    base_url = 'https://example.com'
    
    # Replace 'path/to/save/images' with the desired folder to save the images
    save_folder = 'path/to/save/images'
    
    # Create the save folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)
    
    scrape_rust_images(base_url, save_folder)
