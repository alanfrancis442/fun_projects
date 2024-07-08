from PIL import Image
import os

def conver_to_webp(image_path,destination_path)->None:
    try:
        with Image.open(image_path) as im:
            im.save(destination_path, 'WEBP')
            print("success")
    except Exception as e:
        print(f"Error: {e}")

def dir_init():
    workign_dir = os.getcwd()
    image_dir = os.path.join(workign_dir,'webp_images')
    os.makedirs(image_dir, exist_ok=True)

    for file in os.listdir(workign_dir):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(workign_dir, file)
            destination_path = os.path.join(image_dir, os.path.splitext(file)[0]+'.webp')
            conver_to_webp(image_path, destination_path)

if __name__ == "__main__":
    dir_init()