import easyocr
import cv2
import matplotlib.pyplot as plt
import os

# Image file name
image_path = "sample_img.png"

# Check if image exists
if not os.path.exists(image_path):
    print(f"Error: '{image_path}' not found.")
    print("Make sure the image is in the same folder as app.py")
    exit()

# Initialize OCR Reader
reader = easyocr.Reader(['en'])

# Read text from image
results = reader.readtext(image_path)

# Load image for display
img = cv2.imread(image_path)

if img is None:
    print("Error: Unable to open image.")
    exit()

# Convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(img)
plt.axis("off")
plt.title("Input Image")
plt.show()

# Print OCR results
print("\n===== DETECTED TEXT =====\n")

for result in results:
    bbox, text, confidence = result

    print(f"Text       : {text}")
    print(f"Confidence : {confidence:.2f}")
    print("-" * 40)