import streamlit as st
from PIL import Image
import numpy as np

# 页面标题和描述
st.set_page_config(page_title="集装箱货场服务质量分析平台", layout="wide")
st.title("📦 集装箱货场服务质量分析与优化平台")
st.write("欢迎使用本系统，请上传您的货场平面设计图，我们将为您提供服务质量分析和改进建议。")

# 上传文件
uploaded_file = st.file_uploader("📤 上传货场平面设计图（JPG/PNG）", type=["jpg", "png"])

# 如果文件已上传
if uploaded_file is not None:
    # 显示上传图像
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 上传的货场平面图", use_column_width=True)

    # 模拟货场分析（这里只是展示思路，实际分析可基于你的模型和公式）
    st.subheader("📝 分析结果")
    analysis_result = {
        "场地利用率": f"{np.random.randint(70, 95)}%",
        "运输效率": f"{np.random.randint(60, 90)}%",
        "能耗表现": f"{np.random.randint(50, 80)}%",
        "排放控制": f"{np.random.randint(40, 75)}%"
    }

    for key, value in analysis_result.items():
        st.write(f"✅ **{key}**：{value}")

    # 改进建议（基于分析结果生成建议，这里用随机数模拟）
    st.subheader("💡 改进建议")
    suggestions = [
        "🔹 优化集装箱堆放布局，减少装卸时间。",
        "🔹 提高运输设备调度效率，避免设备闲置。",
        "🔹 引入新能源设备，降低能耗和碳排放。",
        "🔹 增加场地标识，提高货物分区管理效率。"
    ]
    for suggestion in suggestions:
        st.write(suggestion)
else:
    st.info("⏳ 请上传货场平面设计图以开始分析。")
