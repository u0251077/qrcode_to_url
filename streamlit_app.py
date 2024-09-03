import streamlit as st
from PIL import Image
from pyzbar.pyzbar import decode

def scan_qrcode(image):
    # 將 PIL 圖片轉換為灰度圖像
    image = image.convert('RGB')
    
    # 解碼 QR 碼
    decoded_objects = decode(image)
    
    # 提取 QR 碼數據
    result = [obj.data.decode('utf-8') for obj in decoded_objects]
    
    return result

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
            for text in decoded_text:
                st.write(text)
        else:
            st.write("No QR Code detected.")

if __name__ == "__main__":
    main()
