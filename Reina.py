# -*- coding: utf-8 -*-
"""ReinaStreamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FmvCZN14BGmqe8B99a5qHEvY0n4NR3lD
"""
import webbrowser
import streamlit as st
st.set_page_config(layout="wide")  # Set the layout to wide mode


# Sidebar
with st.sidebar:
    st.header('Hello! This is Reina')
    st.image('https://raw.githubusercontent.com/ReinaChenGY/Streamlit/main/photo/Reina.jpg', width=200)  # Adjust the path to your image
    st.write('Wish to connect?')
    if st.button('Connect via email'):
        webbrowser.open_new_tab('mailto:reinachen.gy@outlook.com')
    if st.button('Visit LinkedIn!'):
        webbrowser.open_new_tab('https://www.linkedin.com/in/reina-gy-chen/')

# Main content area
with st.container():
    st.title("Reina's Portfolio")
    st.write("Enjoy exploring user needs and data insights to develop solutions that enhance user experience and business performance")

    # Summary section
    st.subheader('Summary')
    st.write('''4+ years of professional experience at PwC and Blackmores, specializing in tech product solutions for e-commerce, retail, healthcare, and manufacturing industries. Adept in transforming complex business requirements and large datasets into actionable insights, product roadmaps, user-centric features, and interactive dashboards''')

# Work Project
with st.container():
    st.subheader('Work Project')
    clients = [
        "Amazon Electronics Recycler",
        "Top 3 Automobile, Globally",
        "Top 3 Search Engine, Globally",
        "Top 3 Engine Provider, Globally",
        "Top 4 Container Shipping, Globally",
        "Top 8 Dairy Retail, Globally"
    ]
    deliveries = [
        "A Quality Grading AI Software, including Database, ML model, and Dashboards",
        "Risk Assessment and Distribution Scorecard",
        "Data Warehouse and ETL Deployment",
        "Digital Transformation, including API, Demand Forecast Model, and Dashboard",
        "5-Year Strategy Plan, including Market Analysis and Re-organization",
        "Online-Merge-Offline Strategy and Power BI Implementation"
    ]
    images = ['Amazon.jpg', 'Audi.png', 'Baidu.png', 'Cummins.png', 'Cosco.png', 'MengNiu.jpg']
    cols = st.columns(3)
    for col, client, delivery, image in zip(cols, clients[:3], deliveries[:3], images[:3]):
        with col:
            st.image(f'https://raw.githubusercontent.com/ReinaChenGY/Streamlit/main/photo/{image}', use_column_width=True)
            st.markdown(f"<p style='margin-top: 0;'><b>Client:</b> {client}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin-top: 0;'><b>Delivery:</b> {delivery}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # Adding a space
    cols = st.columns(3)  # Maintain uniform column width by creating three columns again
    items = zip(clients[3:], deliveries[3:], images[3:])
    for col, (client, delivery, image) in zip(cols, items):
        with col:
            st.image(f'https://raw.githubusercontent.com/ReinaChenGY/Streamlit/main/photo/{image}', use_column_width=True)
            st.markdown(f"<p style='margin-top: 0;'><b>Client:</b> {client}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin-top: 0;'><b>Delivery:</b> {delivery}</p>", unsafe_allow_html=True)

# Academic Projects
with st.container():
    st.subheader('Academic Project')
    projects = [
        ("Capstone: FED FOMC Confidence Forecast", "Fed.png", "https://github.com/ReinaChenGY/Capstone_FedFomc.git"),
        ("Machine Learning: Credit Score Prediction", "ML.jpg", "https://github.com/ReinaChenGY/ML_CreditScore.git"),
        ("Time Series: Gold Forecasting", "TS.jpg", "https://github.com/ReinaChenGY/TS_GoldForecasting.git"),
        ("Real Time Intelligence: Stock Trading Strategy", "RT.png", "https://github.com/ReinaChenGY/RT_PennyStockForecast.git"),
        ("Data Engineering: Hotel Cancellation Analysis", "DE.png", "https://github.com/ReinaChenGY/DE_HotelCancellation.git")
    ]
    for idx in range(0, len(projects), 3):
        cols = st.columns(3)
        for col, (project_name, project_img, project_url) in zip(cols, projects[idx:idx+3]):
            with col:
                st.image(f'https://raw.githubusercontent.com/ReinaChenGY/Streamlit/main/photo/{project_img}', use_column_width=True, output_format='JPEG')
                st.write(project_name)
                link_html = f'<a href="{project_url}" target="_blank">Check it out!</a>'
                st.markdown(link_html, unsafe_allow_html=True)
                
# Skills section
with st.container():
    st.subheader('Skills')
    skills = [
        ("SQL", "green"), ("Python", "darkblue"), ("Power BI", "orange"),
        ("Tableau", "darkred"), ("Modeling", "green"), ("Database", "darkblue"),
        ("Data Analysis", "orange"), ("SAP", "darkred"), ("Oracle", "green"),
        ("SaaS", "darkblue"), ("UI/UX", "orange"), ("A/B Testing", "darkred"),
        ("Agile", "green"), ("Product", "darkblue"),("Consumer Insight", "orange"),
        ("KPI Metrics", "darkred"), ("E-Commerce", "green"), ("Communication", "darkblue")
    ]
    cols_per_row = 6
    rows = [skills[i:i + cols_per_row] for i in range(0, len(skills), cols_per_row)]
    for row in rows:
        cols = st.columns(cols_per_row)
        for col, (skill, color) in zip(cols, row):
            col.markdown(f"<span style='color:{color};'>{skill}</span>", unsafe_allow_html=True)

# Footer
st.markdown("<br>", unsafe_allow_html=True)  # Adding a space
st.markdown("<br>", unsafe_allow_html=True)  # Adding a space
st.markdown("<br>", unsafe_allow_html=True)  # Adding a space

st.write('© 2024 Reina. All Rights Reserved.')

