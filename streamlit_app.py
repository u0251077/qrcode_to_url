import streamlit as st
from PIL import Image
import cv2
import numpy as np

def scan_qrcode(image):
    # 將 PIL 圖片轉換為 OpenCV 圖像格式
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # 使用 OpenCV 的 QRCodeDetector 來解碼 QR 碼
    detector = cv2.QRCodeDetector()
    decoded_text, points, qr_code = detector(gray)
    
    return decoded_text

def main():
    st.title('QR Code Scanner')

    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        with st.spinner('Scanning QR code...'):
            decoded_text = scan_qrcode(image)
            
        if decoded_text:
            st.subheader("QR Code Data:")
            st.write(decoded_text)
        else:
            st.write("No QR Code detected.")

if __name__ == "__main__":
    main()
