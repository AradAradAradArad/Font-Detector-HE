import streamlit as st
from PIL import Image
import numpy as np
import re

def hex_to_rgb(hex_color):
    # Convert hex color to RGB
    hex_color = re.sub("#", "", hex_color)
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def process_image(image, target_color):
    # Convert image to NumPy array
    image_array = np.array(image)

    # Extract RGB channels
    red, green, blue = image_array[:, :, 0], image_array[:, :, 1], image_array[:, :, 2]

    # Create masks for matching and non-matching pixels
    match_mask = (
        (red >= target_color[0] - 45) & (red <= target_color[0] + 45) &
        (green >= target_color[1] - 45) & (green <= target_color[1] + 45) &
        (blue >= target_color[2] - 45) & (blue <= target_color[2] + 45)
    )

    # Update matching pixels to black and non-matching pixels to white
    image_array[:, :, :3][match_mask] = [0, 0, 0]
    image_array[:, :, :3][~match_mask] = [255, 255, 255]

    # Convert back to PIL Image
    processed_image = Image.fromarray(image_array)

    return processed_image

def main():
    st.title("Font Detection")
    if st.button("Click me for balloons"):
        st.balloons()
    # Upload image using Streamlit file uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Display color picker for target color
    target_color_hex = st.color_picker("Choose target color", "#cab264")
    target_color = hex_to_rgb(target_color_hex)

    if uploaded_file is not None:
        # Process the image
        original_image = Image.open(uploaded_file)
        processed_image = process_image(original_image, target_color)

        # Display the original and processed images
        st.image([original_image, processed_image], caption=["Original Image", "Processed Image"], use_column_width=True)

        # Save the processed image
        output_path = "output_image_processed.png"
        processed_image.save(output_path)
        st.success(f"Processed image saved as {output_path}")

if __name__ == "__main__":
    main()
