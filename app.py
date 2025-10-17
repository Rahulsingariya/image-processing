import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Image Size Reducer", layout="centered")
st.title("🖼 Image Size Reducer")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_container_width=True)

    width = st.number_input("New width (px)", min_value=10, max_value=image.width, value=image.width//2)
    height = st.number_input("New height (px)", min_value=10, max_value=image.height, value=image.height//2)

    if st.button("Resize Image"):
        resized_image = image.resize((width, height))
        st.image(resized_image, caption="Resized Image", use_container_width=True)

        buf = BytesIO()
        resized_image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Resized Image",
            data=byte_im,
            file_name="resized_image.png",
            mime="image/png"
        )
else:
    st.info("Upload an image to start resizing!")