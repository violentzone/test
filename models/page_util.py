from typing import Literal
import numpy as np
import streamlit as st


def get_max_difference(input_list: list, difference_type: Literal['increase', 'decrease']) -> float:
    input_list_ = input_list.copy()
    difference_list = []
    if difference_type == 'increase':
        for i in range(len(input_list_) - 1):
            first_num = input_list_.pop(0)
            difference_list += [first_num - min(input_list_)]

    elif difference_type == 'decrease':
        for i in range(len(input_list_) - 1):
            last_num = input_list_.pop()
            difference_list += [last_num - min(input_list_)]
    else:
        raise Exception('Unknown difference type, aware only use "increase" and "decrease"')

    calculated_result = max(difference_list)
    if calculated_result >= 0:
        return calculated_result
    else:
        return 0


def hr_cal(dialysis: bool, cad: bool, hb_level: float, nsaid: bool, antiplatelet_drug: bool, loop_diuretics: str, loop_diuretics_: str, daily_dose: float,
           hb_level_c: float, m_p_d_egfr_list: list, m_i_bun1_list: list, m_i_bun9_list: list, average_lvef_list: list, average_lvmi_list: list, lvedd: float,
           sv_daily_dose: float, nc_sum_dose_list: list, target_blank: Literal['risk_value2_col1', 'risk_value2_col2']) -> None:
    """
    Input each value in frontend then calculate hazard ratio
    :param dialysis: Selection of dialysis or not
    :param cad: Co-operate with antiplatelet_drug
    :param hb_level: Baseline Hb level
    :param nsaid: Baseline drug use NSAID
    :param antiplatelet_drug: Co-operate with cad
    :param loop_diuretics: Co-operate with loop_diuretics_ and daily_dose
    :param loop_diuretics_: Co-operate with loop_diuretics_ and daily_dose
    :param daily_dose: Co-operate with loop_diuretics_ and daily_dose
    :param hb_level_c: Hb level in current status
    :param m_p_d_egfr_list: Maximum percentage decrease of EGFR
    :param m_i_bun1_list: Maximum increase of BUN level 1 month
    :param m_i_bun9_list: Maximum increase of BUBN level 9 months
    :param average_lvef_list: Average LVEF (%)
    :param average_lvmi_list: Average LVMI (g/m2)
    :param lvedd: The LVEDD
    :param sv_daily_dose: Sacubitril/valsartan daily dose
    :param nc_sum_dose_list: Nicorandil cumulative
    :param target_blank: Tell session_state to change in red or blue card value
    """
    # Check for None in parameters
    check_tuple = (dialysis, cad, hb_level, nsaid, antiplatelet_drug, loop_diuretics,
                   hb_level_c, m_p_d_egfr_list, m_i_bun1_list, m_i_bun9_list, average_lvef_list, average_lvmi_list, lvedd,
                   sv_daily_dose, nc_sum_dose_list)

    # Param1
    if dialysis:
        param1 = 3.2082
    else:
        param1 = 0

    # Param2
    if cad is True and antiplatelet_drug is False:
        param2 = -2.4382
    else:
        param2 = 0

    # Param3
    if hb_level is not None:
        if 11.75 < hb_level <= 14.87:
            param3 = 1.6766
        else:
            param3 = 0
    else:
        param3 = 0

    # Param4
    if nsaid:
        param4 = 5.5419
    else:
        param4 = 0

    # Param5
    if loop_diuretics == 'bumetanide':
        if loop_diuretics_ == 'PO':
            pof = daily_dose * 40
        else:
            pof = daily_dose * 20
    elif loop_diuretics == 'furosemide':
        if loop_diuretics_ == 'PO':
            pof = daily_dose * 1
        else:
            pof = daily_dose * 2
    else:
        pof = 0

    if pof > 28.56:
        param5 = 1.9724
    else:
        param5 = 0

    # Param6
    if hb_level_c:
        param6 = hb_level_c * -0.4645
    else:
        param6 = 0

    # Param7
    if m_p_d_egfr_list:
        value = get_max_difference(m_p_d_egfr_list, difference_type='decrease')/max(m_p_d_egfr_list)
        print('value: ', value)
        print('m_p_d_egfr_list: ', m_p_d_egfr_list)
        param7 = value * 0.0408 * 100
    else:
        param7 = 0

    # Param8
    if m_i_bun1_list:
        value = get_max_difference(m_i_bun1_list, difference_type='increase')
        param8 = value * 0.0559
    else:
        param8 = 0

    # Param9
    if m_i_bun9_list:
        value = get_max_difference(m_i_bun9_list, difference_type='increase')
        param9 = value * 0.0269
    else:
        param9 = 0

    # Param10
    if average_lvef_list:
        value = sum(average_lvef_list) / len(average_lvef_list)
        if value <= 29.95:
            param10 = 1.3926
        else:
            param10 = 0
    else:
        param10 = 0

    # Param11
    if average_lvmi_list:
        value = sum(average_lvmi_list) / len(average_lvmi_list)
        if 167.09 < value <= 297.41:
            param11 = 1.8312
        else:
            param11 = 0
    else:
        param11 = 0

    # Param12
    if lvedd:
        if 45.03 < lvedd <= 66.22:
            param12 = 2.1068
        else:
            param12 = 0
    else:
        param12 = 0

    # Param13
    if sv_daily_dose:
        param13 = sv_daily_dose * -0.0085
    else:
        param13 = 0

    # Param14
    if nc_sum_dose_list:
        if sum(nc_sum_dose_list) > 387.78:
            param14 = 4.0097
        else:
            param14 = 0
    else:
        param14 = 0
    print('exponential: ', param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12,
          param13, param14, '\n sum: ', sum([param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12,
                                                 param13, param14]))
    st.session_state[target_blank] = np.exp(sum([param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12,
                                                 param13, param14]))
