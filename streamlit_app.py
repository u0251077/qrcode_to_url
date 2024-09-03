import streamlit as st
from PIL import Image
import zbar
import io

def scan_qrcode(image):
    # 將 PIL 圖片轉換為灰度圖像
    image = image.convert('L')
    
    # 創建 ZBar 讀取器
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')
    
    # 將 PIL 圖片轉換為 ZBar 圖像
    width, height = image.size
    raw_image = image.tobytes()
    zbar_image = zbar.Image(width, height, 'Y800', raw_image)
    
    # 扫描二维码
    scanner.scan(zbar_image)
    
    # 解析结果
    result = []
    for symbol in zbar_image:
        result.append(symbol.data.decode('utf-8'))
    
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
