import streamlit.components.v1 as components
import streamlit as st

col1,col2,col3=st.columns([2,2,2])

with col1:
    components.html("""
    <div style="
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        margin: 5px;
        font-family: 'Cormorant Garamond', serif;
        color: white;
        backdrop-filter: blur(5px);
        width:300px;
        height:150px;
    ">
        <h4 style="color: #FF6500;">Base line</h4>
        <p>The average fetal heart rate (FHR) in beats per minute (bpm), measured over a 10-minute window. A healthy baseline is typically 110–160 bpm.</p>
    </div>
    """,height=200)

    components.html("""
        <div style="
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin: 5px;
            font-family: 'Cormorant Garamond', serif;
            color: white;
            backdrop-filter: blur(5px);
            width:300px;
            height:150px;
        ">
            <h4 style="color: #FF6500;">Uterine Contractions</h4>
            <p>Frequency or strength of uterine contractions — essential to monitor labor progression and how the fetus reacts to stress during contractions.</p>
        </div>
        """, height=200)

    components.html("""
        <div style="
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin: 5px;
            font-family: 'Cormorant Garamond', serif;
            color: white;
            backdrop-filter: blur(5px);
            width:300px;
            height:150px;
        ">
            <h4 style="color: #FF6500;">Prolonged Decelerations</h4>
            <p>FHR drops lasting longer than 2 minutes — usually a sign of significant fetal compromise and requires urgent attention.</p>
        </div>
        """, height=200)

    components.html("""
        <div style="
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin: 5px;
            font-family: 'Cormorant Garamond', serif;
            color: white;
            backdrop-filter: blur(5px);
            width:300px;
            height:150px;
        ">
            <h4 style="color: #FF6500;">Percentage Of Time With Abnormal Long Term Variability</h4>
            <p>Percentage of total CTG recording time where long-term variability is abnormal — high values indicate risk.</p>
        </div>
        """, height=200)

    components.html("""
        <div style="
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin: 5px;
            font-family: 'Cormorant Garamond', serif;
            color: white;
            backdrop-filter: blur(5px);
            width:300px;
            height:150px;
        ">
            <h4 style="color: #FF6500;">Histogram Mode</h4>
            <p>The most frequent FHR value.</p>
        </div>
        """, height=200)

    components.html("""
        <div style="
            background-color: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            margin: 5px;
            font-family: 'Cormorant Garamond', serif;
            color: white;
            backdrop-filter: blur(5px);
            width:300px;
            height:150px;
        ">
            <h4 style="color: #FF6500;">Histogram Variance</h4>
            <p>Statistical spread/variability in FHR data.</p>
        </div>
        """, height=200)



with col2:
    components.html("""
    <div style="
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        margin: 5px;
        font-family: 'Cormorant Garamond', serif;
        color: white;
        backdrop-filter: blur(5px);
        width:300px;
        height:150px;
    ">
        <h4 style="color: #FF6500;">Accelerations</h4>
        <p>Short-term increases in FHR above the baseline, usually in response to fetal movements or uterine contractions — a positive sign of fetal well-being.</p>
    </div>
    """,height=200)

    components.html("""
            <div style="
                background-color: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin: 5px;
                font-family: 'Cormorant Garamond', serif;
                color: white;
                backdrop-filter: blur(5px);
                width:300px;
                height:150px;
            ">
                <h4 style="color: #FF6500;">Abnormal Short Term Variability</h4>
                <p>Binary indicator (1 or 0): whether short-term variability is outside normal range — low variability can mean nervous system impairment or hypoxia.</p>
            </div>
            """, height=200)

    components.html("""
            <div style="
                background-color: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin: 5px;
                font-family: 'Cormorant Garamond', serif;
                color: white;
                backdrop-filter: blur(5px);
                width:300px;
                height:150px;
            ">
                <h4 style="color: #FF6500;">Mean Value Of Long Term Variability</h4>
                <p>Represents rhythmic fluctuations over longer periods (e.g., 1 minute) — low long-term variability may indicate fetal distress.</p>
            </div>
            """, height=200)


    components.html("""
            <div style="
                background-color: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin: 5px;
                font-family: 'Cormorant Garamond', serif;
                color: white;
                backdrop-filter: blur(5px);
                width:300px;
                height:150px;
            ">
                <h4 style="color: #FF6500;">Histogram Mean</h4>
                <p>The average FHR.</p>
            </div>
            """, height=200)


with col3:
    components.html("""
            <div style="
                background-color: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                margin: 5px;
                font-family: 'Cormorant Garamond', serif;
                color: white;
                backdrop-filter: blur(5px);
                width:300px;
                height:150px
            ">
                <h4 style="color: #FF6500;">Histogram Median</h4>
                <p>	The middle value of the FHR distribution.</p>
            </div>
            """, height=200)