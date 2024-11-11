import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the model using custom objects
model = tf.keras.models.load_model('final_model.keras')

# Function to preprocess the image and predict using the model
def predict_image(image):
    # Resize the image to the input size expected by the model (299x299)
    image = image.resize((299, 299))  # Resize to 299x299
    image_array = np.array(image) / 255.0  # Normalize pixel values
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    
    # Make a prediction
    prediction = model.predict(image_array)
    
    # Get the predicted class (assuming it's a classification model)
    predicted_class = np.argmax(prediction, axis=1)
    
    # Map predicted class to label (you need to define these labels)
    labels = ['Type 1', 'Type 2', 'Type 3']  # Update this with actual cervix types
    return labels[predicted_class[0]]

# Set up the Streamlit page
st.set_page_config(page_title="CerviCare Vision", page_icon=":guardsman:", layout="wide")

# Apply custom CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Sidebar navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Home"):
    st.session_state.page = "Home"
if st.sidebar.button("About Us"):
    st.session_state.page = "About Us"
if st.sidebar.button("Blog"):
    st.session_state.page = "Blog"
if st.sidebar.button("Security and Privacy"):
    st.session_state.page = "Security and Privacy"
if st.sidebar.button("Contact Us"):
    st.session_state.page = "Contact Us"

# Display the selected page
page = st.session_state.page

# Home page content
if page == "Home":
    st.markdown("""
        <h1 style='text-align: center;'>CerviCare Vision</h1>
    """, unsafe_allow_html=True)
    st.markdown("""
      <div class="banner">
                <div class="intro">
            <h2>Welcome to CerviCare Vision!</h2>
        </div>
    <h2>Your Health, Our Priority</h2>
    <p>Early detection saves lives. Use our tool to stay informed and take control of your health.</p>
     </div>
     """, unsafe_allow_html=True)
    st.markdown("""
      <div class="intro">
    <h3>Why Cervical Cancer Screening Matters</h3>
    <p>Cervical cancer is one of the most preventable forms of cancer. Regular screening and early detection can significantly reduce the risk of developing this disease. Our screening tool is designed to help you understand your health status and take proactive steps toward prevention.</p>
     </div>
     """, unsafe_allow_html=True)
    st.markdown("""
     <div class="features">
       <h3>Key Features of Our Tool</h3>
      <div class="feature-grid">
        <div class="feature">
            <h4>Fast & Accurate Screening</h4>
            <p>Our AI-driven model provides quick and accurate results to help you understand your risk level.</p>
        </div>
        <div class="feature">
            <h4>User-Friendly Interface</h4>
            <p>Easy-to-use interface designed for everyone, regardless of technical expertise.</p>
        </div>
        <div class="feature">
            <h4>Educational Resources</h4>
            <p>Access a wealth of information on cervical cancer prevention, treatment, and support.</p>
        </div>
    </div>
   </div>
   """, unsafe_allow_html=True)
    st.markdown("""
   <div class="cta">
    <h3>Get Started Today</h3>
    <p>Take the first step towards ensuring your health. Use our screening tool to assess your risk and learn more about cervical cancer prevention.</p>
   </div>
   """, unsafe_allow_html=True)

    # File uploader for image upload
    uploaded_file = None
    uploaded_file = st.file_uploader("Upload an image for screening", type=["jpg", "jpeg", "png"])

    # Only make a prediction if a file is uploaded
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Make prediction
        with st.spinner('Analyzing the image...'):
            prediction = predict_image(image)
        
        # Display the prediction result
        st.success(f"Prediction: {prediction}")

# About Us section
elif page == "About Us":
    st.title('About Us')

    st.markdown("""
    <div class="section">
    <h2>About Cervical Cancer Detection</h2>
    <p>Cervical cancer is a significant health concern for women worldwide, with early detection playing a critical role in successful treatment and prevention. One of the key factors in cervical cancer detection is determining the type of cervix. The cervix, the lower part of the uterus, varies in shape and structure among women, and these variations can influence the risk of developing cervical cancer.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="section">
    <h2>Why Determining the Cervix Type Matters</h2>
    <p><b>Tailored Screening Methods:</b> Different cervix types may require specific screening methods to ensure accurate detection. For instance, women with a cervix that is more difficult to visualize may need alternative examination techniques to ensure that any abnormalities are not missed.</p>
    <p><b>Risk Assessment:</b> Certain types of cervix may be more prone to developing pre-cancerous changes or cervical cancer. By identifying the cervix type, healthcare providers can better assess an individual's risk level and recommend appropriate follow-up care or preventive measures.</p>
    <p><b>Personalized Treatment Plans:</b> If cervical abnormalities or cancer are detected, understanding the cervix type helps in planning personalized treatment. For example, surgical approaches may differ depending on the cervix’s anatomy, ensuring that the treatment is both effective and minimally invasive.</p>
    <p><b>Improving Patient Outcomes:</b> Early and accurate detection of cervical abnormalities is key to preventing the progression of the disease. By identifying the type of cervix, healthcare providers can enhance the precision of screening and diagnostic procedures, leading to better patient outcomes.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h2>Our Mission</h2>
    <p>Our mission is to empower women with the knowledge and tools they need to take control of their cervical health. By offering a tool that not only screens for cervical cancer but also identifies the type of cervix, we aim to provide a comprehensive approach to cervical cancer prevention and early detection. We believe that every woman deserves access to personalized care that addresses her unique health needs.</p>
     </div>
    """, unsafe_allow_html=True)

    st.markdown("""
     <div class="section">
    <h2>Join Us in the Fight Against Cervical Cancer</h2>
    <p>Cervical cancer is one of the most preventable forms of cancer, yet it remains a leading cause of cancer-related deaths among women worldwide. Together, we can change this. By raising awareness and providing advanced tools for early detection, we are committed to reducing the incidence and impact of cervical cancer. Join us in our mission to save lives through education, early detection, and personalized care.</p>
    </div>
     """, unsafe_allow_html=True)
    
# Blog section
elif page == "Blog":
   st.title('Blog')
   st.markdown("""
   <div class="section">
    <h2>Welcome to Our Blog</h2>
    <p>Stay informed and engaged with the latest insights, updates, and stories related to cervical cancer prevention, early detection, and treatment. Our blog is a resource for women, healthcare providers, and anyone interested in learning more about cervical health.</p>
   </div>
   """, unsafe_allow_html=True)

   st.markdown("""
   <div class="section">
    <h2>Latest Posts</h2>
    <p>Explore our most recent articles:</p>
    <ul>
        <li><a href="#" target="_blank">Understanding the Importance of Regular Cervical Screening</a></li>
        <li><a href="#" target="_blank">HPV Vaccination: What You Need to Know</a></li>
        <li><a href="#" target="_blank">How Lifestyle Choices Affect Cervical Cancer Risk</a></li>
        <li><a href="#" target="_blank">Spotlight on Cervical Cancer Awareness Month</a></li>
    </ul>
   </div>
   """, unsafe_allow_html=True)

   st.markdown("""
   <div class="section">
    <h2>Categories</h2>
    <p>Browse our blog by categories:</p>
    <ul>
        <li><a href="#" target="_blank">Cervical Cancer Prevention</a></li>
        <li><a href="#" target="_blank">Screening and Diagnosis</a></li>
        <li><a href="#" target="_blank">Treatment and Care</a></li>
        <li><a href="#" target="_blank">Patient Stories</a></li>
    </ul>
   </div>
""", unsafe_allow_html=True)

   st.markdown("""
   <div class="section">
    <h2>Contribute to Our Blog</h2>
    <p>Do you have a story to share or insights to contribute? We welcome guest posts from healthcare professionals, survivors, and advocates. Get in touch with us to submit your article.</p>
    <p><b>Email:</b> blog@cervicalscreeningtool.com</p>
   </div>
   """, unsafe_allow_html=True)

# Security and Privacy section
elif page == "Security and Privacy":
    st.title('Security and Privacy')

    st.markdown("""
    <div class="section">
    <h2>Your Privacy is Our Priority</h2>
    <p>We understand that your privacy and security are of utmost importance, especially when it comes to sensitive health information. Our cervical cancer screening tool is designed with your security and privacy in mind, ensuring that your data is protected at all times.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
   <div class="section">
    <h2>Latest Posts</h2>
    <p>Explore our most recent articles:</p>
    <ul>
        <li><a href="#" target="_blank">Understanding the Importance of Regular Cervical Screening</a></li>
        <li><a href="#" target="_blank">HPV Vaccination: What You Need to Know</a></li>
        <li><a href="#" target="_blank">How Lifestyle Choices Affect Cervical Cancer Risk</a></li>
        <li><a href="#" target="_blank">Spotlight on Cervical Cancer Awareness Month</a></li>
    </ul>
   </div>
   """, unsafe_allow_html=True)

    st.markdown("""
   <div class="section">
    <h2>Categories</h2>
    <p>Browse our blog by categories:</p>
    <ul>
        <li><a href="#" target="_blank">Cervical Cancer Prevention</a></li>
        <li><a href="#" target="_blank">Screening and Diagnosis</a></li>
        <li><a href="#" target="_blank">Treatment and Care</a></li>
        <li><a href="#" target="_blank">Patient Stories</a></li>
    </ul>
   </div>
""", unsafe_allow_html=True)

    st.markdown("""
   <div class="section">
    <h2>Contribute to Our Blog</h2>
    <p>Do you have a story to share or insights to contribute? We welcome guest posts from healthcare professionals, survivors, and advocates. Get in touch with us to submit your article.</p>
    <p><b>Email:</b> blog@cervicalscreeningtool.com</p>
   </div>
   """, unsafe_allow_html=True)

# Contact Us section
elif page == "Contact Us":
    st.title('Contact Us')

    st.markdown("""
    <div class="section">
    <h2>We'd Love to Hear From You</h2>
    <p>If you have any questions, feedback, or need further information about our cervical cancer screening tool, please feel free to reach out to us. Your input is valuable, and we're here to assist you in any way we can.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h2>Contact Information</h2>
    <p><b>Email:</b> support@cervicalscreeningtool.com</p>
    <p><b>Phone:</b> +1 (800) 123-4567</p>
    <p><b>Address:</b> 123 Health St, Wellness City, Healthland, 98765</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
    <h2>Follow Us</h2>
    <p>Stay connected and follow us on our social media channels for the latest updates, tips, and resources on cervical cancer prevention and early detection.</p>
    <p>
        <b>Facebook:</b> <a href="https://www.facebook.com/cervicalscreeningtool" target="_blank">facebook.com/cervicalscreeningtool</a><br>
        <b>Twitter:</b> <a href="https://www.twitter.com/cervicaltool" target="_blank">twitter.com/cervicaltool</a><br>
        <b>LinkedIn:</b> <a href="https://www.linkedin.com/company/cervicalscreeningtool" target="_blank">linkedin.com/company/cervicalscreeningtool</a>
    </p>
    </div>
    """, unsafe_allow_html=True) 
