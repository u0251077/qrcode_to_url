import streamlit as st
from PIL import Image
import io
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def read_qr_code(image):
    # 将PIL Image转换为OpenCV格式
    img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # 使用pyzbar解码QR码
    decoded_objects = decode(img_cv)
    
    # 如果检测到QR码
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None

st.title('QR码解析器')

uploaded_file = st.file_uploader("上传包含QR码的图片", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='上传的图片', use_column_width=True)
    
    if st.button('解析QR码'):
        url = read_qr_code(image)
        if url:
            st.success(f'解析到的URL: {url}')
            st.markdown(f'[点击这里访问链接]({url})')
        else:
            st.error('未能检测到QR码,请确保图片中包含有效的QR码。')
