import pandas as pd
import numpy as np
import streamlit as st
from math import exp
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from streamlit_extras.stylable_container import stylable_container

class ShowHR:
    def __init__(self, hr1: float, hr2: float) -> None:
        self.hr1 = round(hr1, 2)
        self.hr2 = round(hr2, 2)

    def show(self):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('##### ' + 'Hazard ratio' + ' #####')
            with stylable_container(
                key="container_with_border",
                css_styles="""
            {
                border: 1px solid rgba(49, 0, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px);
                background-color: blue;
                color: white;
            }
            """,):
                text1 = '<p style="font-size:40px">' + str(self.hr1) + '</p>'
                st.markdown(text1, unsafe_allow_html=True)

        with col2:
            st.markdown('##### ' + 'Hazard ratio' + ' #####')
            with stylable_container(
                    key="container_with_border2",
                    css_styles="""
                   {
                       border: 1px solid rgba(49, 0, 63, 0.2);
                       border-radius: 0.5rem;
                       padding: calc(1em - 1px);
                       background-color: red;
                       color: white
                   }
                   """, ):
                text2 = '<p style="font-size:40px">' + str(self.hr2) + '</p>'
                st.markdown(text2, unsafe_allow_html=True)

class HrControl:
    session_name = 'init'

    @staticmethod
    def risk_calculation(dialysis=0, bun=30, age=65, lvef_2d_none=False, lvef_2d=30, esd_none=False, esd=5.5, rdw_cv_none=False, rdw_cv=14.5, ivsd_none=False, ivsd=1.2, bmi=28, lvmi_none=False, lvmi=125, nt_proBNP_none=False, nt_proBNP=1500, paod=0, total_acei=80, p2y12=0, ar_none=False, ar_value=1.5, en_h_display='Outpatient Department (OPD)', nyha=2, rvdd_none=False, rvdd=3.2, ua_u_0=0, alt_none=False, alt=30, lad_none=False, lad=4.5):
        # Exponential 部分數值
        # Dialysis & BUN 相關計算
        if dialysis == 0:
            sub1 = 0.026028463109 * bun
        else:
            sub1 = 0
        print('sub1: ', sub1)

        # Dialysis 相關計算
        if dialysis:
            sub2 = 0.950797843888
        else:
            sub2 = 0
        print('sub2: ', sub2)

        # Age & LVEF 相關計算
        if 30.855 < age <= 53.454 and lvef_2d_none is False and lvef_2d > 29.865:
            sub3 = -0.991824550572
        else:
            sub3 = 0
        print('sub3: ', sub3)

        # ESD 相關計算
        if esd_none is False and esd:
            sub4 = 0.268831763467 * esd
        else:
            sub4 = 0
        print('sub4: ', sub4)

        # RDW_CV.yes.x.RDW_CV.b14.283_GAM.M 相關計算
        if rdw_cv_none is False and rdw_cv > 14.283:
            sub5 = 0.515158554286
        else:
            sub5 = 0
        print('sub5: ', sub5)

        # IVSd.yes.x.IVSd 相關計算
        if ivsd_none is False and ivsd:
            sub6 = -1.19014798842 * ivsd
        else:
            sub6 = 0
        print('sub6: ', sub6)

        # BMI 相關計算
        if bmi < 25.999:
            sub7 = 0.471678762296
        else:
            sub7 = 0
        print('sub7: ', sub7)

        # LVMI.yes.x.LVMI.se134.942.b199.801_PSpline.M 相關計算
        if lvmi_none is False and (lvmi < 134.942 or lvmi > 199.801):
            sub8 = 0.490229719050
        else:
            sub8 = 0
        print('sub8: ', sub8)

        # NT_proBNP.yes 相關計算
        if nt_proBNP_none is False and nt_proBNP > 2481.283:
            sub9 = 1.094821587918 - 1.173401884380
        elif nt_proBNP_none is False and 2481.283 >= nt_proBNP > 0:
            sub9 = -1.173401884380
        else:
            sub9 = 0
        print('sub9: ', sub9)

        # PAOD 相關計算
        if paod:
            sub10 = 0.941410521315
        else:
            sub10 = 0
        print('sub10: ', sub10)

        # BaselineDrug_Yes.x.GDMT_RAASB_equi_0.se140.135_PSpline.S 相關計算
        if total_acei <= 140.135:
            sub11 = 0.750297099372
        else:
            sub11 = 0
        print('sub11: ', sub11)

        # BaselineDrug_Yes.x.P2Y12_U_0 相關計算
        if p2y12:
            sub12 = -0.633193186654
        else:
            sub12 = 0
        print('sub12: ', sub12)

        # AR.b0 相關計算
        if ar_none is False and ar_value > 0:
            sub13 = -0.454457104335
        else:
            sub13 = 0
        print('sub13: ', sub13)

        # En_H 相關計算
        if en_h_display == 'Inpatient Department (IPD)':
            sub14 = -0.589972039375
        else:
            sub14 = 0
        print('sub14: ', sub14)

        # NYHA.12 相關計算
        if nyha == 1 or nyha == 2:
            sub15 = -0.478237238417
        else:
            sub15 = 0
        print('sub15: ', sub15)

        # RVDd.yes.x.RVDd.b2.469_PSpline.S 相關計算
        if rvdd_none is False and rvdd > 2.469:
            sub16 = 0.455496776315
        else:
            sub16 = 0
        print('sub16: ', sub16)

        # BaselineDrug_Yes.ua_u_0 相關計算
        if ua_u_0 == 1:
            sub17 = -0.629241379606
        else:
            sub17 = 0
        print('sub17: ', sub17)

        # ALT.yes.x.ALT.se15.614.b84.255_PSpline.S 相關計算
        if alt_none is False and (alt < 15.614 or alt >= 84.255):
            sub18 = 0.401945974915
        else:
            sub18 = 0
        print('sub18: ', sub18)

        # LAD.yes.x.LAD.b4.348_PSpline.M 相關計算
        if lad_none is False and lad > 4.348:
            sub19 = 0.505894183559
        else:
            sub19 = 0
        print('sub19: ', sub19)

        # 列印個數值
        print('-' * 100)
        value_list = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11, sub12, sub13, sub14, sub15, sub16, sub17, sub18, sub19]

        text = ''
        for value in value_list:
            text += (str(value) + ' + ')
        print(text)
        print('-' * 100)
        print('Total exponential: ', sum(value_list))

        # 回傳 Cox 模型的風險值（不依賴 baseline_survival）
        return np.exp(sum(value_list))


def calculate_and_set(dialysis, bun, age, lvef_2d_none, lvef_2d, esd_none, esd, rdw_cv_none, rdw_cv, ivsd_none, ivsd, bmi, lvmi_none, lvmi, nt_proBNP_none, nt_proBNP, paod, total_acei, p2y12, ar_none, ar_value, en_h_display, nyha, rvdd_none, rvdd, ua_u_0, alt_none, alt, lad_none, lad, session_name):
    value = HrControl.risk_calculation(dialysis, bun, age, lvef_2d_none, lvef_2d, esd_none, esd, rdw_cv_none, rdw_cv, ivsd_none, ivsd, bmi, lvmi_none, lvmi, nt_proBNP_none, nt_proBNP, paod, total_acei, p2y12, ar_none, ar_value, en_h_display, nyha, rvdd_none, rvdd, ua_u_0, alt_none, alt, lad_none,
                                       lad)
    st.session_state[session_name] = value
    st.session_state['pred_copy'] = False
    
@st.cache_data
def load_csv(data_path):
    data = pd.read_csv(data_path)
    return data


def predict_plot(hr1: float, hr2: float, show_blue: bool, show_red: bool):
    baseline_hazard = load_csv("./models/baseline_hazard(1).csv")
    baseline_survival = np.exp(-baseline_hazard['hazard'])
    f = plt.figure('v1', figsize=(10, 3), facecolor='#FAF3DD', edgecolor='#FAF3DD')
    plt.style.use('Solarize_Light2')
    predicted_survival1 = baseline_survival ** hr1
    predicted_survival2 = baseline_survival ** hr2

    # 使用基準風險中的時間列來繪製曲線
    if show_red:
        plt.plot(baseline_hazard['time'], predicted_survival2, color='red', label='Scenario 2')

    plt.plot(baseline_hazard['time'], predicted_survival1, color='blue', label='Scenario 1')

    plt.title('')
    plt.xlabel('Years after Sacubitril/Valsartan Initiation')
    plt.ylabel('Survival Probability')
    
    # 設定 X 軸的刻度為 1 年、2 年、3 年、4 年、5 年（以年份顯示）
    plt.xticks([12, 24, 36, 48, 60], ['1', '2', '3', '4', '5'])
    
    # 設定 X 軸的上限（最多 5 年）
    plt.xlim(0, 60)
    
    # 設定 Y 軸的刻度，從 0 到 1，每 0.1 一個刻度
    plt.yticks(np.arange(0, 1.1, 0.1), ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']) 
    plt.ylim(0, 1.02)
    
    # 顯示圖例
    plt.legend(loc='lower left')
    
    return f

