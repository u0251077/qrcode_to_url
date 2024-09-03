import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

def decode_qr_code(image):
    decoded_objects = decode(image)
    for obj in decoded_objects:
        # 將 QR 碼內容轉換成字串
        return obj.data.decode('utf-8')
    return None

def main():
    st.title("QR Code Image to URL")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # 使用 PIL 讀取上傳的影像
        image = Image.open(uploaded_file)

        # 顯示影像
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # 解碼 QR 碼
        qr_code_data = decode_qr_code(image)
        if qr_code_data:
            st.write("Decoded QR Code Data:")
            st.write(qr_code_data)
        else:
            st.write("No QR Code found in the image.")

if __name__ == "__main__":
    main()
