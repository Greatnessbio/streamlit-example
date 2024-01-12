import streamlit as st
from PIL import Image
import cairosvg
import io

def convert_to_svg(input_image):
    # Convert PIL Image to PNG bytes
    with io.BytesIO() as output_bytes:
        input_image.save(output_bytes, format='PNG')
        png_data = output_bytes.getvalue()

    # Convert PNG bytes to SVG
    svg_data = cairosvg.png2svg(png_data)
    return svg_data

def save_image(image, format):
    with io.BytesIO() as output_bytes:
        image.save(output_bytes, format=format)
        return output_bytes.getvalue()

def main():
    st.title("Image File Converter")

    # Upload file
    uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg', 'gif', 'bmp'])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Choose output format
        format_options = ['SVG', 'PNG', 'JPG', 'GIF', 'BMP']
        output_format = st.selectbox("Select Output Format", format_options)

        if st.button("Convert"):
            if output_format == 'SVG':
                converted_data = convert_to_svg(image)
                file_ext = 'svg'
            else:
                converted_data = save_image(image, output_format)
                file_ext = output_format.lower()

            # Create a download link
            download_filename = f"converted_image.{file_ext}"
            st.download_button(
                label="Download Image",
                data=converted_data,
                file_name=download_filename,
                mime=f"image/{file_ext}"
            )

if __name__ == "__main__":
    main()
