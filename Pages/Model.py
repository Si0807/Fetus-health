import json
import streamlit as st
import pickle
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

# scaler loading
scaler=pickle.load(open('scaler_MinMax.sav','rb'))

# Model loading
model=pickle.load(open('model_RandomForest.sav','rb'))
# method to load animation
def load_lottie(filepath:str):
    with open(filepath,'r') as f:
        return json.load(f)
# loading an animation
load_animation=load_lottie('ECG.json')

# heading
st.markdown("""
            <p style="font-family:Times New Roman; font-size:30px;text-align: right;">
            Fill the required parameters
            </p>
            """,unsafe_allow_html=True)
space=st.empty()
col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    st_lottie(load_animation, key=None, height=300,width=300)
# forms
with col3:
    st.markdown('<br><br>',unsafe_allow_html=True)
    st.markdown("""
                <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                Base line value
                </p>
                """, unsafe_allow_html=True)
    baseline = st.text_input("", key="baseline_input")

    st.markdown("""
                    <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                    Accelerations
                    </p>
                    """, unsafe_allow_html=True)
    accelerations = st.text_input("", key="accelerations")


    st.markdown("""
                        <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                        Uterine contractions
                        </p>
                        """, unsafe_allow_html=True)
    uterine_contractions = st.text_input("", key="uterine_contractions")


    st.markdown("""
                        <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                        Prolonged decelerations
                        </p>
                        """, unsafe_allow_html=True)
    prolonged_decelerations = st.text_input("", key="prolonged_decelerations")

    st.markdown("""
                        <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                        Abnormal short term variability
                        </p>
                        """, unsafe_allow_html=True)
    abnormal_short_term_variability = st.text_input("", key="abnormal_short_term_variability")

    st.markdown("""
                           <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                           Percentage of time with abnormal long term variability
                           </p>
                           """, unsafe_allow_html=True)
    percentage_of_time_with_abnormal_long_term_variability = st.text_input("", key="percentage_of_time_with_abnormal_long_term_variability")

    st.markdown("""
                                   <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                                   Mean Value Of Long Term Variability
                                   </p>
                                   """, unsafe_allow_html=True)
    mean_value_of_long_term_variability = st.text_input("", key="mean_value_of_long_term_variability")

    st.markdown("""
                           <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                           Histogram mode
                           </p>
                           """, unsafe_allow_html=True)
    histogram_mode = st.text_input("", key="histogram_mode")

    st.markdown("""
                           <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                           Histogram mean
                           </p>
                           """, unsafe_allow_html=True)
    histogram_mean = st.text_input("", key="histogram_mean")

    st.markdown("""
                               <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                               Histogram median
                               </p>
                               """, unsafe_allow_html=True)
    histogram_median = st.text_input("", key="histogram_median")

    st.markdown("""
                               <p style="font-family:Times New Roman; font-size:20px;text-align:left;margin-bottom:5px;">
                               Histogram variance
                               </p>
                               """, unsafe_allow_html=True)
    histogram_variance = st.text_input("", key="histogram_variance")

    values = [baseline,
              accelerations,
              uterine_contractions,
              prolonged_decelerations,
              abnormal_short_term_variability,
              percentage_of_time_with_abnormal_long_term_variability,
              mean_value_of_long_term_variability,
              histogram_mode,
              histogram_mean,
              histogram_median,
              histogram_variance
              ]

    button=st.button(label="Check Fetus Health")
    if button:
        result=model.predict(scaler.transform([values]))
        if result==0:
            components.html("""        
                            <h2 id="typing-text" style="
                                color: white;
                                font-family:Julius Sans One;
                                margin: 0;
                            "></h2>
                        </div>

                        <script>
                        let text = "Normal";
                        let i = 0;

                        function typeWriter() {
                            if (i < text.length) {
                                document.getElementById("typing-text").innerHTML += text.charAt(i);
                                i++;
                                setTimeout(typeWriter,60);
                            }
                        }

                        typeWriter();
                        </script>
                        """, height=150)
        elif result==1:
            components.html(""" 
                                   
                            <h2 id="typing-text" style="
                                color: white;
                                font-family:Julius Sans One;
                                margin: 0;
                            "></h2>
                        </div>

                        <script>
                        let text = "Suspect";
                        let i = 0;

                        function typeWriter() {
                            if (i < text.length) {
                                document.getElementById("typing-text").innerHTML += text.charAt(i);
                                i++;
                                setTimeout(typeWriter,60);
                            }
                        }

                        typeWriter();
                        </script>
                        """, height=150)
        else:
            components.html("""  
            <!DOCTYPE html>
            <html>
            <head>
              <style>
                @keyframes pulse {
                  0% { transform: scale(1); }
                  50% { transform: scale(1.05); }
                  100% { transform: scale(1); }
                }
                .animated-text {
                  animation: pulse 1.5s infinite;
                  color: white;
                  font-family: 'Julius Sans One', sans-serif;
                  margin: 0;
                  font-size: 32px;
                }
                body {
                  background-color: transparent;
                  margin: 0;
                }
              </style>
            </head>
            <body>
              <h2 id="typing-text" class="animated-text"></h2>

              <script>
                let text = "Pathological";
                let i = 0;

                function typeWriter() {
                  if (i < text.length) {
                    document.getElementById("typing-text").innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 60);
                  }
                }

                typeWriter();
              </script>
            </body>
            </html>
            """, height=150)

