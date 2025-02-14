import os
import time
import random
from instagrapi import Client


USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"


IMAGE_FOLDER = r"C:\Users\admin\OneDrive\Pictures\InstagramBotTest"


cl = Client()
cl.login(USERNAME, PASSWORD)

def get_random_image(folder):

    images = [f for f in os.listdir(folder) if f.lower().endswith(('jpg', 'jpeg', 'png'))]
    if not images:
        print("No images found in folder!")
        return None
    return os.path.join(folder, random.choice(images))

def upload_image():

    image_path = get_random_image(IMAGE_FOLDER)
    if image_path:
        caption = "Automated Post #️⃣ #instabot #python"
        try:
            cl.photo_upload(image_path, caption)
            print(f"✅ Uploaded: {image_path}")
            os.remove(image_path)
        except Exception as e:
            print(f"❌ Error uploading {image_path}: {e}")

if __name__ == "__main__":
    while True:
        upload_image()
        print("⏳ Waiting 24 hours for next upload...")
        time.sleep(86400)
