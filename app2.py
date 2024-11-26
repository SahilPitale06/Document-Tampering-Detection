import streamlit as st
from skimage.metrics import structural_similarity
import cv2
from PIL import Image
import numpy as np
import requests
import os
from pdf2image import convert_from_bytes

# Create directories for saving processed images if they don't exist
os.makedirs("id_card_tampering/image", exist_ok=True)

# Document templates for comparison (Replace these URLs with actual templates for Aadhaar, Voter ID, etc.)
original_urls = {
    "Pan Card": 'https://www.thestatesman.com/wp-content/uploads/2019/07/pan-card.jpg',
    "Aadhaar Card": 'https://link_to_aadhaar_image.jpg',  # Example: Replace with actual URL for Aadhaar
    "Voter ID": 'https://link_to_voter_id_image.jpg',   # Example: Replace with actual URL for Voter ID
    "Driving License": 'https://link_to_driving_license_image.jpg'  # Example: Replace with actual URL for Driving License
}

# Streamlit UI
st.title("Document Tampering Detection")

# Select document type
doc_type = st.selectbox("Select Document Type", options=["Pan Card", "Aadhaar Card", "Voter ID", "Driving License"])

# Load the original image based on the selected document type
original_url = original_urls[doc_type]
original_image = Image.open(requests.get(original_url, stream=True).raw)
original_image = original_image.resize((250, 160))  # Resize for consistency

# Convert the original image to OpenCV format for processing
original_cv = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2BGR)
original_gray = cv2.cvtColor(original_cv, cv2.COLOR_BGR2GRAY)

# Upload an image or PDF file
uploaded_file = st.file_uploader("Upload an image or PDF file to check for tampering", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    # Determine if the uploaded file is an image or PDF
    if uploaded_file.type == "application/pdf":
        # Convert PDF to image
        pdf_pages = convert_from_bytes(uploaded_file.read(), dpi=200)
        user_image = pdf_pages[0]  # Take only the first page
    else:
        # Load image file directly
        user_image = Image.open(uploaded_file)
    
    # Resize user image to match original
    user_image = user_image.resize((250, 160))
    
    # Convert the user's image to OpenCV format
    user_cv = cv2.cvtColor(np.array(user_image), cv2.COLOR_RGB2BGR)
    user_gray = cv2.cvtColor(user_cv, cv2.COLOR_BGR2GRAY)
    
    # Display both images
    st.image(original_image, caption=f"Original {doc_type.replace('_', ' ').title()}", use_column_width=True)
    st.image(user_image, caption="Uploaded Image", use_column_width=True)

    # Compute the Structural Similarity Index (SSI) between the images
    (score, diff) = structural_similarity(original_gray, user_gray, full=True)
    st.write(f"Image similarity score: {score:.4f}")

    # Check similarity score and provide feedback
    if score >= 0.9:
        st.success("The images are very similar; tampering is unlikely.")
    else:
        st.warning("The images differ significantly; tampering may have occurred.")

    # Process the difference image
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image to find regions of change
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Find contours of the thresholded difference areas
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    # Draw bounding boxes around detected differences
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(original_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(user_cv, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Convert the images with differences to display in Streamlit
    original_diff_image = Image.fromarray(cv2.cvtColor(original_cv, cv2.COLOR_BGR2RGB))
    user_diff_image = Image.fromarray(cv2.cvtColor(user_cv, cv2.COLOR_BGR2RGB))

    # Display images with differences highlighted
    st.image(original_diff_image, caption="Original Image with Differences Highlighted", use_column_width=True)
    st.image(user_diff_image, caption="Uploaded Image with Differences Highlighted", use_column_width=True)
