import streamlit as st


# def tab_layout():
#     TAB_LAYOUT = '''
#         <style>
#             .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
#             font-size:3rem;
#             font-weight: bold;
#             text-align: center;
#             line-height: 100px;
#             }
#         </style>
#         '''
#     st.markdown(TAB_LAYOUT, unsafe_allow_html=True)
#

def expander_layout():
    EXPANDER_LAYOUT = '''
        <style>
            div[data-testid="stExpander"] div[role="button"] p {
            font-size: 1rem;
            font-weight: bold;
            }
        </style>
        '''
    st.markdown(EXPANDER_LAYOUT, unsafe_allow_html=True)