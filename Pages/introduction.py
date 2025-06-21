import streamlit as st
import pickle
from PIL import Image
from streamlit_lottie import st_lottie
import  json
import streamlit.components.v1 as components

# method for calling an animation
def load_lottie_animation(filepath:str):
    with open(filepath,'r') as f:
        return json.load(f)

# loading the animation to a variable
animation=load_lottie_animation('Fetus_json_animation.json')


# navigation layout
st.set_page_config(
    page_title="Fetal Health Prediction",
    layout="wide",
    initial_sidebar_state="auto"
)

# streamlit code
st.markdown(
    """
    <p style="color:#f9c9c0; font-size: 50px; text-align: center; font-family: Playfair Display">
    Fetal Health Prediction
    </p>""",
    unsafe_allow_html=True)

st_lottie(animation, key=None, height=250)
# Typewriter effect
components.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond&display=swap');

h2, .box p, .box h4 {
    font-family: 'Cormorant Garamond', serif !important;
}

h2 {
    font-size: 16px;
    line-height: 1.4;
}

#fade-boxes {
    opacity: 0;
    transition: opacity 1s ease-in;
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
    flex-wrap: wrap;
}

.fade-in {
    opacity: 1 !important;
}

.box {
    background-color: #EEEEEE;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    width: 250px;
    color: #111;
}
.box h4 {
    color: #92140c;
    margin-top: 0;
}
</style>

<!-- Typewriter Box 1 -->
<div id="box1" style="
    background-color: #92140c;
    padding: 15px;
    border-radius: 5px;
    display: inline-block;
    margin: 5px auto;
    text-align: center;
">
    <h2 id="typing-text1" style="
        color: #EEEEEE;
        margin: 0;
        display: inline-block;
        white-space: pre-wrap;
    "></h2>
</div>

<!-- Typewriter Box 2 -->
<div id="box2" style="
    background-color: #92140c;
    padding: 10px;
    border-radius: 5px;
    display: none;
    text-align: center;
    margin: 5px auto;
">
    <h2 id="typing-text2" style="
        color: white;
        margin: 0;
        display: inline-block;
        white-space: pre-wrap;
    "></h2>
</div>

<!-- Fade-in Info Boxes -->
<div id="fade-boxes">
    <div class="box">
        <h4>Objective</h4>
        <p><ul>
            <li>Load and preprocess CTG data using pandas.<br><br></li>

            <li>Train a robust Random Forest model to classify fetal health as:<br><br></li>
                <ul style="list-style-type:square;">
                <li>Normal</li>
                This indicates that the fetus is in a healthy state<br>
                <li>Suspect</li>
                This is an intermediate category, meaning the fetus may be developing stress but not yet in a critical state<br>
                <li>Pathological</li>
                This category indicates serious fetal distress and potential danger to fetal health<br><br>
                </ul>
            <li>Evaluate model performance using metrics like accuracy, confusion matrix, and classification report.<br><br></li>
            
            <li>Deploy a user-friendly web app using Streamlit, where users can input values and get instant predictions.</li>
        </ul></p>
    </div>
    <div class="box">
        <h4>Workflow</h4>
        <p><ol>
            <li>Data Collection:</li>
                    <ul>
                    <li>Dataset: Fetal Health Classification Dataset (CTG-based features)</li>
                    <li>Format: CSV file with numerical inputs and unlabeled target classes</li>
                    </ul>
                    
            <li>Data Preprocessing (Pandas):</li>
                    <ul>    
                    <li>Feature scaling or normalization (if required)</li> 
                    <li>Splitting into training and testing sets</li>
                    </ul>
            <li>Model Training (Scikit-learn):</li>
                    <ul>
                    <li>Use RandomForestClassifier</li>
                    <li>Perform hyperparameter tuning</li>
                    <li>Evaluate using train/test split and cross-validation</li>
                    </ul>
            <li>Model Deployment (Streamlit):</li>
                    <ul>
                    <li>Create a web interface for user input</li>
                    <li>Display prediction results with classification labels</li>
                    <li>Include model confidence score or prediction probability</li>
                    </ul>
        </ol></p>
    </div>
    <div class="box">
        <h4>Resources Used</h4>
        <p><ul>
            <li>Python</li><br>
            <li>Pandas</li><br>
            <li>Sklearn</li><br>
            <li>CTG</li><br>
            <li>RandomForestClassifier</li><br>
            <li>Streamlit</li><br>
            <li>HTML and CSS</li><br>
        </p>
    </div>
</div>

<script>
let text1 = "An essential component of prenatal care that aids in identifying possible risks to the unborn child is fetal health assessment. Clinicians typically use cardiotocography (CTG) data to assess the health of the fetus. Manually interpreting these data, however, can be laborious and prone to errors.";
let text2 = "The goal of this project is to create a machine learning-based system that can automatically predict the health status of a fetus using Python and the Random Forest Classifier. The system uses pandas to preprocess data, trains a RandomForestClassifier on CTG data, and provides predictions via an API interface based on Streamlit for user or healthcare provider convenience.";

let i = 0;
let j = 0;

function typeWriter1() {
    if (i < text1.length) {
        document.getElementById("typing-text1").innerHTML += text1.charAt(i);
        i++;
        setTimeout(typeWriter1, 50);
    } else {
        document.getElementById("box2").style.display = "inline-block";
        setTimeout(typeWriter2, 100);
    }
}

function typeWriter2() {
    if (j < text2.length) {
        document.getElementById("typing-text2").innerHTML += text2.charAt(j);
        j++;
        setTimeout(typeWriter2, 50);
    } else {
        // Fade in the info boxes
        document.getElementById("fade-boxes").classList.add("fade-in");
    }
}

typeWriter1();
</script>
""", height=1500)
