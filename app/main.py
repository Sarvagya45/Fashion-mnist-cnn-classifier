import streamlit as st
import torch
from PIL import Image
import numpy as np
import os

# import your model class
from model import MyNN   # make sure this file exists

# device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# path
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_model/checkpoint.pth"

# load model
model = MyNN(input_features=1)   # same as training
model.to(device)

checkpoint = torch.load(model_path, map_location=device)
model.load_state_dict(checkpoint['model_state_dict'])

model.eval()

# class labels
class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

# preprocess function
def preprocess_image(image):
    img = Image.open(image).convert('L')   # grayscale
    img = img.resize((28, 28))

    img_array = np.array(img)
    
    # Fashion MNIST images are trained with a black background and white clothing.
    # If the user uploads an image with a white background, we invert the colors.
    if img_array[0, 0] > 128:
        img_array = 255.0 - img_array
        
    img_array = img_array / 255.0
    img_tensor = torch.tensor(img_array, dtype=torch.float32)

    # Apply same normalization as training: mean=0.5, std=0.5
    img_tensor = (img_tensor - 0.5) / 0.5

    # shape → (1, 1, 28, 28)
    img_tensor = img_tensor.unsqueeze(0).unsqueeze(0)

    return img_tensor.to(device)

# Streamlit UI
st.title("Fashion Item Classifier (PyTorch)")

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)

    col1, col2 = st.columns(2)

    # LEFT SIDE → show image
    with col1:
        resized_img = image.resize((100, 100))
        st.image(resized_img, caption="Uploaded Image")

    # RIGHT SIDE → prediction
    with col2:
        if st.button("Classify"):

            # preprocess
            input_tensor = preprocess_image(uploaded_image)

            # prediction
            with torch.no_grad():
                output = model(input_tensor)
                _, predicted = torch.max(output, 1)

            predicted_class = class_names[predicted.item()]

            st.success(f"Prediction: {predicted_class}")