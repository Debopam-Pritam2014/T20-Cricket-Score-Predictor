import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

pipe = pickle.load(open('model.pkl', 'rb'))
teams = ['Sri Lanka', 'Australia', 'Bangladesh', 'Pakistan', 'India',
         'England', 'New Zealand', 'Afghanistan', 'South Africa',
         'West Indies']
venues = ['Shere Bangla National Stadium',
          'R Premadasa Stadium',
          'Dubai International Cricket Stadium',
          'New Wanderers Stadium',
          'Eden Park',
          'Newlands',
          'Pallekele International Cricket Stadium',
          'Kensington Oval, Bridgetown',
          'Melbourne Cricket Ground',
          'Beausejour Stadium, Gros Islet',
          'Kennington Oval',
          'Kingsmead',
          'Westpac Stadium',
          'Central Broward Regional Park Stadium Turf Ground',
          'Seddon Park',
          'SuperSport Park',
          'Old Trafford',
          'Zahur Ahmed Chowdhury Stadium',
          'R.Premadasa Stadium, Khettarama',
          'Sheikh Zayed Stadium',
          'Sydney Cricket Ground',
          'Trent Bridge',
          'The Rose Bowl',
          'Bay Oval',
          'Wankhede Stadium',
          'Eden Gardens',
          'Gaddafi Stadium',
          'Vidarbha Cricket Association Stadium, Jamtha',
          "Lord's",
          'Adelaide Oval',
          'M Chinnaswamy Stadium',
          'Warner Park, Basseterre',
          'Sophia Gardens',
          "Queen's Park Oval, Port of Spain"]

st.title('Male T20 Internationals Cricket Score Predictor')
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling Team', sorted(teams))

venue = st.selectbox('Venue', sorted(venues))

col3, col4, col5 = st.columns(3)

with col3:
    curr_score = st.number_input('Current Score:', min_value=0, max_value=300, value=0)

with col4:
    overs = st.number_input('Overs done(must be >5)', min_value=5, max_value=19, value=5)

with col5:
    wickets = st.number_input('Wickets Out', min_value=0, max_value=9, value=0)

last_five = st.number_input('Runs Scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - overs * 6
    wickets_left = 10 - wickets
    crr = curr_score / overs
    if batting_team == bowling_team:
        st.header(f"😃😃 {batting_team} playing against {bowling_team}".format(batting_team, bowling_team))
    else:
        inp_data = pd.DataFrame(
            {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'curr_score': [curr_score],
             'balls_left': [balls_left], 'wicket_left': [wickets_left], 'crr': [crr], 'last_five_over_runs': [last_five],
             'venue': [venue]
             })
        prediction = pipe.predict(inp_data)
        st.header('Predicted Score: ' + str(int(prediction[0])))
