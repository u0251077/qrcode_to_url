
import streamlit as st
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decode_qr_code(image):
    # 将图像转换为灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 解码QR码
    decoded_objects = decode(gray)
    
    if decoded_objects:
        # 返回第一个解码对象的数据
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None

st.title('QR码解码器')

uploaded_file = st.file_uploader("上传包含QR码的图片", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # 读取上传的图片
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    # 显示上传的图片
    st.image(image, caption='上传的图片', use_column_width=True)
    
    # 解码QR码
    url = decode_qr_code(image)
    
    if url:
        st.success('成功解码QR码！')
        st.write('解码后的URL:')
        st.code(url)
        
        # 添加复制按钮
        st.text_input('复制URL:', value=url)
    else:
        st.error('无法解码QR码，请确保上传的图片包含有效的QR码。')
