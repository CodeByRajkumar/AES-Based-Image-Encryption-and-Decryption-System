
# Import necessary libraries
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import numpy as np
import time
import os

# AES Encryption function
def encrypt_image(image_path, key):
    img = Image.open(image_path).convert('RGB')
    img_bytes = np.array(img).tobytes()
    
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(img_bytes, AES.block_size))
    
    return ciphertext, iv, img.size

# AES Decryption function
def decrypt_image(ciphertext, iv, key, img_size):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    img_array = np.frombuffer(decrypted_bytes, dtype=np.uint8).reshape((img_size[1], img_size[0], 3))
    return Image.fromarray(img_array)

# Save encrypted image as scrambled visual (for demo)
def save_encrypted_visual(ciphertext, image_size, output_path="encrypted_visual.png"):
    encrypted_array = np.frombuffer(ciphertext, dtype=np.uint8)
    
    total_pixels = image_size[0] * image_size[1] * 3
    padded_array = np.zeros(total_pixels, dtype=np.uint8)
    padded_array[:len(encrypted_array)] = encrypted_array[:total_pixels]
    
    encrypted_img = padded_array.reshape((image_size[1], image_size[0], 3))
    Image.fromarray(encrypted_img).save(output_path)
    print(f"Encrypted visual saved as {output_path}")

# Define your AES key (must be 16, 24, or 32 bytes)
key = b'Sixteen byte key'

# Set your image file name (make sure it's uploaded to the notebook environment)
image_path = "your_image.jpg"  # Change this to your uploaded image

# Check if the image file exists
if not os.path.exists(image_path):
    print(f"Image file '{image_path}' not found. Please upload it to the notebook environment.")
else:
    # Encrypt the image
    start = time.time()
    ciphertext, iv, size = encrypt_image(image_path, key)
    print("Image encrypted in", round(time.time() - start, 4), "seconds")

    # Save a visual version of the encrypted data
    save_encrypted_visual(ciphertext, size)

    # Decrypt the image
    start = time.time()
    decrypted_img = decrypt_image(ciphertext, iv, key, size)
    print("Image decrypted in", round(time.time() - start, 4), "seconds")

    # Save and show the decrypted image
    decrypted_img.save("decrypted_image.jpg")
    decrypted_img.show()
