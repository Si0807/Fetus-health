import streamlit as st
# navigation part
page1=st.Page(
    page='Pages/introduction.py',
    title='Home Screen',
    icon=':material/home:',
    default=True
)
page2=st.Page(
    page='Pages/feature_description.py',
    title='Feature Description',
    icon=':material/manage_search:'
)
page3=st.Page(
    page='Pages/Model.py',
    title='Fetus Health Predictor',
    icon=':material/token:'
)

pg=st.navigation(
    {
        'Info':[page1],
        'Features':[page2],
        'Test':[page3]
    }
)
pg.run()