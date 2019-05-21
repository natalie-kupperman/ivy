# change column names to pythonic syntax
import pandas as pd
import glob, os

files = glob.glob('spreadsheets/ctr-report*.csv')

for file_ in files:
    df = pd.read_csv(file_).rename(columns = {
                                              'Period Name' : 'period_name',
                                              'Period Number' : 'period_number',
                                              'Low Load(avg)' : 'load_low_avg',
                                              'Profile Max Velocity' : 'velocity_profile_max',
                                              'TRIMP' : 'trimp',
                                              'TRIMP(avg) ' : 'trimp_avg',
                                              'TRIMP/MIN' : 'trimp_per_minute',
                                              'Volume Load' : 'load_volume',
                                              'Work/Rest Ratio': 'work_rest_ratio',
                                              'Player Load Band 8 Average Duration' : 'player_load_band_8_duration_avg',
                                              'Acceleration Density': 'accel_density',
                                              'Acceleration Density Index': 'accel_density_index',
                                              'Avg Acceleration Load (Session)': 'accel_load_session_avg',
                                              'Total Acceleration Load': 'accel_load_total',
                                              'Total Activities': 'activities_total',
                                              'Player Name': 'player_name',
                                              'Date': 'date',
                                              'Day Name': 'day_of_week',
                                              'Estimated Indoor Distance (Session)': 'distance_indoor_session_est',
                                              'Estimated Distance (Indoor)': 'distance_indoor_est',
                                              'Average Duration': 'duration_avg',
                                              'Duration (min)': 'duration_minute',
                                              'Average Duration (Session)': 'duration_session_avg',
                                              'Total Duration': 'duration_total',
                                              'Unix End Time': 'end_time_unix',
                                              'Field Time': 'field_time',
                                              'Avg Heart Rate': 'hr_average',
                                              'Avg HR (% Max)': 'hr_avg_perc_max',
                                              'Heart Rate Band 1 Average BPM': 'hr_band_1_bpm_avg',
                                              'Heart Rate Band 1 Average Duration': 'hr_band_1_duration_avg',
                                              'Heart Rate Band 1 Duration %': 'hr_band_1_duration_perc',
                                              'Heart Rate Band 1 Average Duration (Session)': 'hr_band_1_duration_session_avg',
                                              'Heart Rate Band 1 Total Duration': 'hr_band_1_total_duration',
                                              'Heart Rate Band 2 Average BPM': 'hr_band_2_bpm_avg',
                                              'Heart Rate Band 2 Average Duration': 'hr_band_2_duration_avg',
                                              'Heart Rate Band 2 Duration %': 'hr_band_2_duration_perc',
                                              'Heart Rate Band 2 Average Duration (Session)': 'hr_band_2_duration_session_avg',
                                              'Heart Rate Band 2 Average Effort Count': 'hr_band_2_effort_count_avg',
                                              'Heart Rate Band 2 Average Effort Count (Session)': 'hr_band_2_effort_count_session_avg',
                                              'Heart Rate Band 2 Total Effort Count': 'hr_band_2_effort_count_total',
                                              'Heart Rate Band 2 Total Duration': 'hr_band_2_total_duration',
                                              'Heart Rate Band 3 Average BPM': 'hr_band_3_bpm_avg',
                                              'Heart Rate Band 3 Average Duration': 'hr_band_3_duration_avg',
                                              'Heart Rate Band 3 Duration %': 'hr_band_3_duration_perc',
                                              'Heart Rate Band 3 Average Duration (Session)': 'hr_band_3_duration_session_avg',
                                              'Heart Rate Band 3 Average Effort Count': 'hr_band_3_effort_count_avg',
                                              'Heart Rate Band 3 Average Effort Count (Session)': 'hr_band_3_effort_count_session_avg',
                                              'Heart Rate Band 3 Total Effort Count': 'hr_band_3_effort_count_total',
                                              'Heart Rate Band 3 Total Duration': 'hr_band_3_total_duration',
                                              'Heart Rate Band 4 Average BPM': 'hr_band_4_bpm_avg',
                                              'Heart Rate Band 4 Average Duration': 'hr_band_4_duration_avg',
                                              'Heart Rate Band 4 Duration %': 'hr_band_4_duration_perc',
                                              'Heart Rate Band 4 Average Duration (Session)': 'hr_band_4_duration_session_avg',
                                              'Heart Rate Band 4 Average Effort Count': 'hr_band_4_effort_count_avg',
                                              'Heart Rate Band 4 Average Effort Count (Session)': 'hr_band_4_effort_count_session_avg',
                                              'Heart Rate Band 4 Total Effort Count': 'hr_band_4_effort_count_total',
                                              'Heart Rate Band 4 Total Duration': 'hr_band_4_total_duration',
                                              'Heart Rate Band 5 Average BPM': 'hr_band_5_bpm_avg',
                                              'Heart Rate Band 5 Average Duration': 'hr_band_5_duration_avg',
                                              'Heart Rate Band 5 Duration %': 'hr_band_5_duration_perc',
                                              'Heart Rate Band 5 Average Duration (Session)': 'hrband_5_duration_session_avg',
                                              'Heart Rate Band 5 Average Effort Count': 'hr_band_5_effort_count_avg',
                                              'Heart Rate Band 5 Average Effort Count (Session)': 'hr_band_5_effort_count_session_avg',
                                              'Heart Rate Band 5 Total Effort Count': 'hr_band_5_effort_count_total',
                                              'Heart Rate Band 5 Total Duration': 'hr_band_5_total_duration',
                                              'Heart Rate Band 6 Average BPM': 'hr_band_6_bpm_avg',
                                              'Heart Rate Band 6 Average Duration': 'hr_band_6_duration_avg',
                                              'Heart Rate Band 6 Duration %': 'hr_band_6_duration_perc',
                                              'Heart Rate Band 6 Average Duration (Session)': 'hr_band_6_duration_session_avg',
                                              'Heart Rate Band 6 Average Effort Count': 'hr_band_6_effort_count_avg',
                                              'Heart Rate Band 6 Average Effort Count (Session)': 'hr_band_6_effort_count_session_avg',
                                              'Heart Rate Band 6 Total Effort Count': 'hr_band_6_effort_count_total',
                                              'Heart Rate Band 6 Total Duration': 'hr_band_6_total_duration',
                                              'Heart Rate Band 7 Average BPM': 'hr_band_7_bpm_avg',
                                              'Heart Rate Band 7 Average Duration': 'hr_band_7_duration_avg',
                                              'Heart Rate Band 7 Duration %': 'hr_band_7_duration_perc',
                                              'Heart Rate Band 7 Average Duration (Session)': 'hr_band_7_duration_session_avg',
                                              'Heart Rate Band 7 Average Effort Count': 'hr_band_7_effort_count_avg',
                                              'Heart Rate Band 7 Average Effort Count (Session)': 'hr_band_7_effort_count_session_avg',
                                              'Heart Rate Band 7 Total Effort Count': 'hr_band_7_effort_count_total',
                                              'Heart Rate Band 7 Total Duration': 'hr_band_7_total_duration',
                                              'Heart Rate Band 8 Average BPM': 'hr_band_8_bpm_avg',
                                              'Heart Rate Band 8 Average Duration': 'hr_band_8_duration_avg',
                                              'Heart Rate Band 8 Duration %': 'hr_band_8_duration_perc',
                                              'Heart Rate Band 8 Average Duration (Session)': 'hr_band_8_duration_session_avg',
                                              'Heart Rate Band 8 Average Effort Count': 'hr_band_8_effort_count_avg',
                                              'Heart Rate Band 8 Average Effort Count (Session)': 'hr_band_8_effort_count_session_avg',
                                              'Heart Rate Band 8 Total Effort Count': 'hr_band_8_effort_count_total',
                                              'Heart Rate Band 8 Total Duration': 'hr_band_8_total_duration',
                                              'Heart Rate Exertion': 'hr_extertion',
                                              'Heart Rate Exertion Per Minute': 'hr_extertion_per_minute',
                                              'Maximum Heart Rate': 'hr_max',
                                              'Max HR (% Max)': 'hr_max_perc_max',
                                              'Minimum Heart Rate': 'hr_min',
                                              'Profile Max Heart Rate': 'hr_profile_max',
                                              "High IMA 12 O'Clock (Session)": 'ima_ 12_oclock_high_session',
                                              "IMA 1 O'Clock High": 'ima_1_oclock_high',
                                              'IMA 1 OClock High 1.0': 'ima_1_oclock_high_1',
                                              "High IMA 1 O'Clock (Session)": 'ima_1_oclock_high_session',
                                              "IMA 1 O'Clock Low": 'ima_1_oclock_low',
                                              "IMA 1 O'Clock Low 1.0": 'ima_1_oclock_low_1',
                                              "IMA 1 O'Clock Medium": 'ima_1_oclock_medium',
                                              "IMA 1 O'Clock Medium 1.0": 'ima_1_oclock_medium_1',
                                              "IMA 10 O'Clock High": 'ima_10_oclock_high',
                                              "IMA 10 O'Clock High 1.0": 'ima_10_oclock_high_1',
                                              "High IMA 10 O'Clock (Session)": 'ima_10_oclock_high_session',
                                              "IMA 10 O'Clock Low": 'ima_10_oclock_low',
                                              "IMA 10 O'Clock Low 1.0": 'ima_10_oclock_low_1',
                                              "IMA 10 O'Clock Medium": 'ima_10_oclock_medium',
                                              "IMA 10 O'Clock Medium 1.0": 'ima_10_oclock_medium_1',
                                              "IMA 11 O'Clock High": 'ima_11_oclock_high',
                                              "IMA 11 O'Clock High 1.0": 'ima_11_oclock_high_1',
                                              "High IMA 11 O'Clock (Session)": 'ima_11_oclock_high_session',
                                              "IMA 11 O'Clock Low": 'ima_11_oclock_low',
                                              "IMA 11 O'Clock Low 1.0": 'ima_11_oclock_low_1',
                                              "IMA 11 O'Clock Medium": 'ima_11_oclock_medium',
                                              "IMA 11 O'Clock Medium 1.0": 'ima_11_oclock_medium_1',
                                              "IMA 12 O'Clock High": 'ima_12_oclock_high',
                                              "IMA 12 O'Clock High 1.0": 'ima_12_oclock_high_1',
                                              "IMA 12 O'Clock Low": 'ima_12_oclock_low',
                                              "IMA 12 O'Clock Low 1.0": 'ima_12_oclock_low_1',
                                              "IMA 12 O'Clock Medium": 'ima_12_oclock_medium',
                                              "IMA 12 O'Clock Medium 1.0": 'ima_12_oclock_medium_1',
                                              "IMA 2 O'Clock High": 'ima_2_oclock_high',
                                              "IMA 2 O'Clock High 1.0": 'ima_2_oclock_high_1',
                                              "High IMA 2 O'Clock (Session)": 'ima_2_oclock_high_session',
                                              "IMA 2 O'Clock Low": 'ima_2_oclock_low',
                                              "IMA 2 O'Clock Low 1.0": 'ima_2_oclock_low_1',
                                              "IMA 2 O'Clock Medium": 'ima_2_oclock_medium',
                                              "IMA 2 O'Clock Medium 1.0": 'ima_2_oclock_medium_1',
                                              "IMA 3 O'Clock High": 'ima_3_oclock_high',
                                              "IMA 3 O'Clock High 1.0": 'ima_3_oclock_high_1',
                                              "High IMA 3 O'Clock (Session)": 'ima_3_oclock_high_session',
                                              "IMA 3 O'Clock Low": 'ima_3_oclock_low',
                                              "IMA 3 O'Clock Low 1.0": 'ima_3_oclock_low_1',
                                              "IMA 3 O'Clock Medium": 'ima_3_oclock_medium',
                                              "IMA 3 O'Clock Medium 1.0": 'ima_3_oclock_medium_1',
                                              "IMA 4 O'Clock High": 'ima_4_oclock_high',
                                              "IMA 4 O'Clock High 1.0": 'ima_4_oclock_high_1',
                                              "High IMA 4 O'Clock (Session)": 'ima_4_oclock_high_session',
                                              "IMA 4 O'Clock Low": 'ima_4_oclock_low',
                                              "IMA 4 O'Clock Low 1.0": 'ima_4_oclock_low_1',
                                              "IMA 4 O'Clock Medium": 'ima_4_oclock_medium',
                                              "IMA 4 O'Clock Medium 1.0": 'ima_4_oclock_medium_1',
                                              "IMA 5 O'Clock High": 'ima_5_oclock_high',
                                              "IMA 5 O'Clock High 1.0": 'ima_5_oclock_high_1',
                                              "High IMA 5 O'Clock (Session)": 'ima_5_oclock_high_session',
                                              "IMA 5 O'Clock Low": 'ima_5_oclock_low',
                                              "IMA 5 O'Clock Low 1.0": 'ima_5_oclock_low_1',
                                              "IMA 5 O'Clock Medium": 'ima_5_oclock_medium',
                                              "IMA 5 O'Clock Medium 1.0": 'ima_5_oclock_medium_1',
                                              "IMA 6 O'Clock High": 'ima_6_oclock_high',
                                              "IMA 6 O'Clock High 1.0": 'ima_6_oclock_high_1',
                                              "High IMA 6 O'Clock (Session)": 'ima_6_oclock_high_session',
                                              "IMA 6 O'Clock Low": 'ima_6_oclock_low',
                                              "IMA 6 O'Clock Low 1.0": 'ima_6_oclock_low_1',
                                              "IMA 6 O'Clock Medium": 'ima_6_oclock_medium',
                                              "IMA 6 O'Clock Medium 1.0": 'ima_6_oclock_medium_1',
                                              "IMA 7 O'Clock High": 'ima_7_oclock_high',
                                              "IMA 7 O'Clock High 1.0": 'ima_7_oclock_high_1',
                                              "High IMA 7 O'Clock (Session)": 'ima_7_oclock_high_session',
                                              "IMA 7 O'Clock Low": 'ima_7_oclock_low',
                                              "IMA 7 O'Clock Low 1.0": 'ima_7_oclock_low_1',
                                              "IMA 7 O'Clock Medium": 'ima_7_oclock_medium',
                                              "IMA 7 O'Clock Medium 1.0": 'ima_7_oclock_medium_1',
                                              "IMA 8 O'Clock High": 'ima_8_oclock_high',
                                              "IMA 8 O'Clock High 1.0": 'ima_8_oclock_high_1',
                                              "High IMA 8 O'Clock (Session)": 'ima_8_oclock_high_session',
                                              "IMA 8 O'Clock Low": 'ima_8_oclock_low',
                                              "IMA 8 O'Clock Low 1.0": 'ima_8_oclock_low_1',
                                              "IMA 8 O'Clock Medium": 'ima_8_oclock_medium',
                                              "IMA 8 O'Clock Medium 1.0": 'ima_8_oclock_medium_1',
                                              "IMA 9 O'Clock High": 'ima_9_oclock_high',
                                              "IMA 9 O'Clock High 1.0": 'ima_9_oclock_high_1',
                                              "High IMA 9 O'Clock (Session)": 'ima_9_oclock_high_session',
                                              "IMA 9 O'Clock Low": 'ima_9_oclock_low',
                                              "IMA 9 O'Clock Low 1.0": 'ima_9_oclock_low_1',
                                              "IMA 9 O'Clock Medium": 'ima_9_oclock_medium',
                                              "IMA 9 O'Clock Medium 1.0": 'ima_9_oclock_medium_1',
                                              'IMA Accel High': 'ima_accel_high',
                                              'IMA Accel High 1.0': 'ima_accel_high_1',
                                              'IMA Average ACCEL High (Session) 1.0': 'ima_accel_high_1_session_avg',
                                              'High IMA Accel (avg)': 'ima_accel_high_avg',
                                              'IMA Accel Low': 'ima_accel_low',
                                              'IMA Accel Low 1.0': 'ima_accel_low_1',
                                              'IMA Average ACCEL Low (Session) 1.0': 'ima_accel_low_1_session_avg',
                                              'Low IMA Accel (Session)': 'ima_accel_low_session',
                                              'IMA Accel Medium': 'ima_accel_medium',
                                              'IMA Accel Medium 1.0': 'ima_accel_medium_1',
                                              'IMA Average ACCEL Medium (Session) 1.0': 'ima_accel_medium_1_session_avg',
                                              'Medium IMA Accel (Session)': 'ima_accel_medium_session',
                                              'IMA CoD Left High': 'ima_cod_left_high',
                                              'IMA CoD Left High 1.0': 'ima_cod_left_high_1',
                                              'High IMA CoD Left (avg)': 'ima_cod_left_high_avg',
                                              'IMA CoD Left Low': 'ima_cod_left_low',
                                              'IMA CoD Left Low 1.0': 'ima_cod_left_low_1',
                                              'Low IMA CoD Left (Session)': 'ima_cod_left_low_session',
                                              'IMA CoD Left Medium': 'ima_cod_left_medium',
                                              'IMA CoD Left Medium 1.0': 'ima_cod_left_medium_1',
                                              'Medium IMA CoD Left (Session)': 'ima_cod_left_medium_session',
                                              'IMA CoD Right High': 'ima_cod_right_high',
                                              'IMA CoD Right High 1.0': 'ima_cod_right_high_1',
                                              'High IMA CoD Right (avg)': 'ima_cod_right_high_avg',
                                              'IMA CoD Right Low': 'ima_cod_right_low',
                                              'IMA CoD Right Low 1.0': 'ima_cod_right_low_1',
                                              'Low IMA CoD Right (Session)': 'ima_cod_right_low_session',
                                              'IMA CoD Right Medium': 'ima_cod_right_medium',
                                              'IMA CoD Right Medium 1.0': 'ima_cod_right_medium_1',
                                              'Medium IMA CoD Right (Session)': 'ima_cod_right_medium_session',
                                              'IMA Decel High': 'ima_decel_high',
                                              'IMA Decel High 1.0': 'ima_decel_high_1',
                                              'IMA Average DECEL High (Session) 1.0': 'ima_decel_high_1_session_avg',
                                              'High IMA Decel (avg)': 'ima_decel_high_avg',
                                              'IMA Decel Low 1.0': 'ima_decel_low_1',
                                              'IMA Average DECEL Low (Session) 1.0': 'ima_decel_low_1_session_avg',
                                              'Low IMA Decel (Session)': 'ima_decel_low_session',
                                              'IMA Decel Medium': 'ima_decel_medium',
                                              'IMA Decel Medium 1.0': 'ima_decel_medium_1',
                                              'IMA Average DECEL Medium (Session) 1.0' : 'ima_decel_medium_1_session_avg',
                                              'IMA Decel Low' : 'ima_decel_low',
                                              'Medium IMA Decel (Session)': 'ima_decel_medium_session',
                                              '% High IMA': 'ima_high_perc',
                                              'IMA Jump Count Band 4' : 'ima_jump_band_4_count',
                                              'IMA Jump Count Band 5' : 'ima_jump_band_5_count',
                                              'IMA Jump Count Band 6' : 'ima_jump_band_6_count',
                                              'IMA Jump Count Band 7' : 'ima_jump_band_7_count',
                                              'IMA Jump Count Band 8' : 'ima_jump_band_8_count',
                                              'IMA Jump Count High Band': 'ima_jump_high_band_count',
                                              'IMA Jump Count Low Band': 'ima_jump_low_band_count',
                                              'IMA Jump Count Med Band': 'ima_jump_medium_band_count',
                                              'IMA Average LEFT High (Session) 1.0': 'ima_left_high_session_1',
                                              'IMA Average LEFT Low (Session) 1.0': 'ima_left_low_1_session_avg ',
                                              'IMA Average LEFT Medium (Session) 1.0': 'ima_left_medium_session_1',
                                              'IMA/Min': 'ima_per_minute',
                                              'IMA Average RIGHT High (Session) 1.0': 'ima_right_high_1_session_avg',
                                              'IMA Average RIGHT Low (Session) 1.0': 'ima_right_low_1_session_avg ',
                                              'IMA Average RIGHT Medium (Session) 1.0': 'ima_right_medium_1_session_avg',
                                              'Total IMA': 'ima_total',
                                              'Total IMA (avg)': 'ima_total_avg',
                                              'Total IMA V1': 'ima_total_v1',
                                              'Total IMA (avg) V1': 'ima_total_v1_avg',
                                              'Jumps/Minute': 'jumps_per_minute',
                                              'Total Jumps': 'jumps_total',
                                              'High Load': 'load_high',
                                              'High Load (avg)': 'load_high_avg',
                                              'High Load / Minute': 'load_high_per_minute',
                                              'High Load % of Total': 'load_high_perc_total',
                                              'Low Load': 'load_low',
                                              ' Low Load (avg)': 'load_low_avg',
                                              'Low Load / Minute': 'load_low_per_minute',
                                              ' Medium Load': 'load_medium',
                                              'Medium Load (avg)': 'load_medium_avg',
                                              'Med Load / Minute': 'load_medium_per_minute',
                                              'Estimated Miles': 'miles_estimate',
                                              'Estimated Miles (session)': 'miles_session_estimate',
                                              'Month Name': 'month_name',
                                              'Average Player Load (1D Fwd)': 'player_load_1d_fwd_avg',
                                              'Player Load (1D Fwd %)': 'player_load_1d_fwd_perc',
                                              'Average Player Load (1D Fwd) (Session)': 'player_load_1d_fwd_session_avg',
                                              'Player Load (1D Fwd)': 'player_load_1d_fwd',
                                              'Average Player Load (1D Side)': 'player_load_1d_side_avg',
                                              'Player Load (1D Side %)': 'player_load_1d_side_perc',
                                              'Average Player Load (1D Side) (Session)': 'player_load_1d_side_session_avg',
                                              'Player Load (1D Side)': 'player_load_1d_side',
                                              'Average Player Load (1D Up)': 'player_load_1d_up_avg',
                                              'Player Load (1D Up %)': 'player_load_1d_up_perc',
                                              'Average Player Load (1D Up) (Session)': 'player_load_1d_up_session_avg',
                                              'Player Load (1D Up)': 'player_load_1d_up',
                                              'Average Player Load (2D)': 'player_load_2d_avg',
                                              'Average Player Load (2D) (Session)': 'player_load_2d_session_avg',
                                              'Player Load (avg)': 'player_load_avg',
                                              'Player Load Band 1 Average Duration': 'player_load_band_1_duration_avg',
                                              'Player Load Band 1 Duration %': 'player_load_band_1_duration_perc',
                                              'Player Load Band 1 Average Duration (Session)': 'player_load_band_1_duration_session_avg',
                                              'Player Load Band 1 Total Player Load': 'player_load_band_1_player_load_total',
                                              'Player Load Band 1 Total Duration': 'player_load_band_1_total_duration',
                                              'Player Load Band 2 Average Duration': 'player_load_band_2_duration_avg',
                                              'Player Load Band 2 Duration %': 'player_load_band_2_duration_perc',
                                              'Player Load Band 2 Average Duration (Session)': 'player_load_band_2_duration_session_avg',
                                              'Player Load Band 2 Total Duration': 'player_load_band_2_duration_total',
                                              'Player Load Band 2 Average Effort Count': 'player_load_band_2_effort_count_avg',
                                              'Player Load Band 2 Average Effort Count (Session)': 'player_load_band_2_effort_count_session_avg',
                                              'Player Load Band 2 Total Effort Count': 'player_load_band_2_effort_count_total',
                                              'Player Load Band 2 Total Player Load': 'player_load_band_2_player_load_total',
                                              'Player Load Band 3 Average Duration': 'player_load_band_3_duration_avg',
                                              'Player Load Band 3 Duration %': 'player_load_band_3_duration_perc',
                                              'Player Load Band 3 Average Duration (Session)': 'player_load_band_3_duration_session_avg',
                                              'Player Load Band 3 Total Duration': 'player_load_band_3_duration_total',
                                              'Player Load Band 3 Average Effort Count': 'player_load_band_3_effort_count_avg',
                                              'Player Load Band 3 Average Effort Count (Session)': 'player_load_band_3_effort_count_session_avg',
                                              'Player Load Band 3 Total Effort Count': 'player_load_band_3_effort_count_total',
                                              'Player Load Band 3 Total Player Load': 'player_load_band_3_player_load_total',
                                              'Player Load Band 4 Average Duration': 'player_load_band_4_duration_avg',
                                              'Player Load Band 4 Duration %': 'player_load_band_4_duration_perc',
                                              'Player Load Band 4 Average Duration (Session)': 'player_load_band_4_duration_session_avg',
                                              'Player Load Band 4 Average Effort Count': 'player_load_band_4_effort_count_avg',
                                              'Player Load Band 4 Average Effort Count (Session)': 'player_load_band_4_effort_count_session_avg',
                                              'Player Load Band 4 Total Effort Count': 'player_load_band_4_effort_count_total',
                                              'Player Load Band 4 Total Player Load': 'player_load_band_4_player_load_total',
                                              'Player Load Band 4 Total Duration': 'player_load_band_4_total_duration',
                                              'Player Load Band 5 Average Duration': 'player_load_band_5_duration_avg',
                                              'Player Load Band 5 Duration %': 'player_load_band_5_duration_perc',
                                              'Player Load Band 5 Average Duration (Session)': 'player_load_band_5_duration_session_avg',
                                              'Player Load Band 5 Total Duration': 'player_load_band_5_duration_total',
                                              'Player Load Band 5 Average Effort Count': 'player_load_band_5_effort_count_avg',
                                              'Player Load Band 5 Average Effort Count (Session)': 'player_load_band_5_effort_count_session_avg',
                                              'Player Load Band 5 Total Effort Count': 'player_load_band_5_effort_count_total',
                                              'Player Load Band 5 Total Player Load': 'player_load_band_5_player_load_total',
                                              'Player Load Band 6 Average Duration': 'player_load_band_6_duration_avg',
                                              'Player Load Band 6 Duration %': 'player_load_band_6_duration_perc',
                                              'Player Load Band 6 Average Duration (Session)': 'player_load_band_6_duration_session_avg',
                                              'Player Load Band 6 Average Effort Count': 'player_load_band_6_effort_count_avg',
                                              'Player Load Band 6 Average Effort Count (Session)': 'player_load_band_6_effort_count_session_avg',
                                              'Player Load Band 6 Total Effort Count': 'player_load_band_6_effort_count_total',
                                              'Player Load Band 6 Total Player Load': 'player_load_band_6_player_load_total',
                                              'Player Load Band 6 Total Duration': 'player_load_band_6_total_duration',
                                              'Player Load Band 7 Average Duration': 'player_load_band_7_duration_avg',
                                              'Player Load Band 7 Duration %': 'player_load_band_7_duration_perc',
                                              'Player Load Band 7 Average Duration (Session)': 'player_load_band_7_duration_session_avg',
                                              'Player Load Band 7 Total Duration': 'player_load_band_7_duration_total',
                                              'Player Load Band 7 Average Effort Count': 'player_load_band_7_effort_count_avg',
                                              'Player Load Band 7 Average Effort Count (Session)': 'player_load_band_7_effort_count_session_avg',
                                              'Player Load Band 7 Total Effort Count': 'player_load_band_7_effort_count_total',
                                              'Player Load Band 7 Total Player Load': 'player_load_band_7_player_load_total',
                                              'Player Load Band 8 Duration %': 'player_load_band_8_duration_perc',
                                              'Player Load Band 8 Average Duration (Session)': 'player_load_band_8_duration_session_avg',
                                              'Player Load Band 8 Average Effort Count': 'player_load_band_8_effort_count_avg',
                                              'Player Load Band 8 Average Effort Count (Session)': 'player_load_band_8_effort_count_session_avg',
                                              'Player Load Band 8 Total Effort Count': 'player_load_band_8_effort_count_total',
                                              'Player Load Band 8 Total Player Load': 'player_load_band_8_player_load_total',
                                              'Player Load Band 8 Total Duration': 'player_load_band_8_total_duration',
                                              'Peak Player Load': 'player_load_peak',
                                              'Player Load Per Minute': 'player_load_per_minute',
                                              'Average Player Load (period)': 'player_load_period_avg',
                                              'Average Player Load (Slow)': 'player_load_slow_avg',
                                              'Average Player Load (Slow) (Session)': 'player_load_slow_session_avg',
                                              'Player Load (Slow)': 'player_load_slow',
                                              'Total Player Load': 'player_load_total',
                                              'Total Player Load (2D)': 'player_load_total_2d',
                                              'Session Count': 'session_count',
                                              'Unix Start Time': 'start_time_unix',
                                              'Tendon Load': 'tendon_load',
                                              'Tendon Load (avg)': 'tendon_load_avg',
                                              'Duration (avg)' : 'duration_avg'
                                            })
    df.to_csv(file_, index = False)