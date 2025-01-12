import streamlit as st
from models import baseline_model, prediction_model
from layout_css import expander_layout
from streamlit_extras.stylable_container import stylable_container


def run():
    st.set_page_config(layout="wide")
    expander_layout()
    # Set st.session_state which page to display
    if 'page' not in st.session_state:
        st.session_state['page'] = 'baseline_model'

    space, col1, space, col2, space = st.columns([2.2, 5, 2.5, 5, 0.5])
    with col1:
        with stylable_container(
                key="baseline_model",
                css_styles="""
                   button {
                    height:50px;
                    padding-right: 5rem;
                    padding-left: 5rem;
                    width:auto;
                    background-color: gray;
                    color: white;
                    border-radius: 20px;
                    font-size: 1.5rem;
                    margin: 4px 2px;
font-size: 16px;
                   }
                   """,
        ):
            baseline = st.button("Explanation", key='baseline')
            if baseline:
                st.session_state['page'] = 'baseline_model'
    with col2:
        with stylable_container(
                key="prediction_model",
                css_styles="""
                   button {
                    height:50px;
                    padding-right: 5rem;
                    padding-left: 5rem;
                    width:auto;
                    background-color: gray;
                    color: white;
                    border-radius: 20px;
                    font-size: 1.5rem;
                    margin: 4px 2px;
                   }
                   """,
        ):
            prediction = st.button("Prediction", key='predicton')
            if prediction:
                st.session_state['page'] = 'prediction_model'

    # Identify which to show
    if st.session_state['page'] == 'baseline_model':
        baseline_model.baseline_view()
    elif st.session_state['page'] == 'prediction_model':
        prediction_model.prediction_view()


if __name__ == '__main__':
    run()
