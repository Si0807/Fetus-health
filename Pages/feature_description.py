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
            <h4 style="color: #FF6500;">Percentage Of  Time With Abnormal Long Term Variability</h4>
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
            height:150px
        ">
            <h4 style="color: #FF6500;">Histogram Max</h4>
            <p>The maximum FHR value recorded.</p>
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
                <h4 style="color: #FF6500;">Light Decelerations</h4>
                <p>Small, temporary drops in FHR — may be benign or due to fetal head compression during contractions.</p>
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
                height:150px
            ">
                <h4 style="color: #FF6500;">Histogram Number Of Peaks</h4>
                <p>Number of peaks in the histogram — related to FHR mode changes or fluctuations.</p>
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
                <h4 style="color: #FF6500;">Histogram Tendency</h4>
                <p>A measure indicating whether FHR tends to increase or decrease over time (directional bias).</p>
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
        height:150px;
    ">
        <h4 style="color: #FF6500;">Fetal Movement</h4>
        <p>The number or magnitude of detected fetal movements — higher movement typically indicates a healthy and active fetus.</p>
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
                <h4 style="color: #FF6500;">Severe Decelerations</h4>
                <p>Deep and prolonged drops in FHR, possibly indicating fetal hypoxia or distress — a warning sign.</p>
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
                height:150px
            ">
                <h4 style="color: #FF6500;">Mean Value of Short Term Variability</h4>
                <p>Average beat-to-beat changes in FHR, reflecting instantaneous changes in autonomic nervous activity.</p>
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
                <h4 style="color: #FF6500;">Histogram Width</h4>
                <p>The range of the FHR values (max - min).</p>
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
                <h4 style="color: #FF6500;">Histogram Min</h4>
                <p>The minimum FHR value recorded.</p>
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
                height:150px
            ">
                <h4 style="color: #FF6500;">Histogram Number Of Zeroes</h4>
                <p>Number of bins with zero values in the histogram — might indicate uniformity or gaps in heart rate patterns.</p>
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
                height:150px
            ">
                <h4 style="color: #FF6500;">Histogram Median</h4>
                <p>	The middle value of the FHR distribution.</p>
            </div>
            """, height=200)