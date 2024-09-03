
import streamlit as st
import numpy as np
from PIL import Image
import qrcode
from io import BytesIO

def generate_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

st.title('QR码生成器')

url = st.text_input('请输入要生成QR码的URL:')

if url:
    # 生成QR码
    qr_image = generate_qr_code(url)
    
    # 将PIL图像转换为字节流
    img_byte_arr = BytesIO()
    qr_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # 显示生成的QR码
    st.image(img_byte_arr, caption='生成的QR码', use_column_width=True)
    
    # 添加下载按钮
    st.download_button(
        label="下载QR码",
        data=img_byte_arr,
        file_name="qrcode.png",
        mime="image/png"
    )
    
    # 显示URL供复制
    st.text_input('复制URL:', value=url)
else:
    st.warning('请输入URL以生成QR码')


