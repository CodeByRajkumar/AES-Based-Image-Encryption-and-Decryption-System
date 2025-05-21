# AES-Based Image Encryption 🔐🖼️

This project demonstrates how to encrypt and decrypt image files using the AES (Advanced Encryption Standard) algorithm in CBC mode.

## Features
- AES encryption with a 16-byte key
- Converts image data into byte format and encrypts it
- Generates a scrambled image visual of encrypted data
- Fully restores the original image after decryption

## Files
- `image_aes_encryption.ipynb`: Jupyter notebook containing the full encryption & decryption workflow
- `code.py`: Python script version of the same logic
- `decrypted_image.jpg`: Output image after decryption
- `encrypted_visual.png`: Encrypted data visualized as an image

## Requirements
- Python 3.x
- Libraries:
  - `pycryptodome`
  - `pillow`
  - `numpy`

Install dependencies:
```bash
pip install pycryptodome pillow numpy
