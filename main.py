import streamlit as st
import math 


st.title("RESCUE TEAM CALCULATOR")

scaled = [1, 2, 3, 4, 5]

#.........................List to display in a Selection box........................#
options_E = [
            "<51",
            "51-150",
            "151-500",
            "501-2000",
            ">2000"
            ]
options_S = ["Integrated",
            "Interdependent",
            "Independent",
            "Dependent",
            "Reactive"]

options_L = ["Full Automation",
            "Semi Automation",
            "Mechanised",
            "Semi-Mechanised",
            "Conventional"]

options_D = ["<200 m",
            "201 m - 300 m",
            "301 m - 400 m",
            "401 m - 500 m",
            ">500 m"]

options_T = ["<13 mins",
            "13-20 mins",
            "20-30 mins",
            "30-60 mins",
            ">60 mins"]

options_N = ["1",
            "2",
            "3",
            "4",
            "5 or more"]

options_R = ["Robots for Mine Rescue",
            "Rescue Capsules, Van, Mobile station",
            "Breathing Apparatus for all team members and fully stocked refuge chambers",
            "With breathing Apparatus for First Team",
            "Volunteers and Without breathing apparatus"]


#.............................getting selection from the user................................................#
option1=st.selectbox(
  "Number of Employees per shift?",
  options_E
)

option2=st.selectbox(
  "Safety Culture in the Mine?",
  options_S
)

option3=st.selectbox(
  "Level of Mechanisation?",
  options_L
)

option4=st.selectbox(
  "Mining Depth",
  options_D
)

option5=st.selectbox(
  "Nearness and Responsivenes of Sister Rescue Team?",
  options_T
)

option6=st.selectbox(
  "Number of active Mines within the Mine?",
  options_N
)

option7=st.selectbox(
  "Resourcefulness of the Rescue team?",
  options_R
)


#........................Scaling user selection and doing calculation................#
def solve():
    scaled = [1, 2, 3, 4, 5]
    for option in options_E:
        if option == option1:
            index = options_E.index(option)
    E = scaled[index]

    for option in options_S:
        if option == option2:
            index = options_S.index(option)
    S = scaled[index]

    for option in options_R:
        if option == option7:
            index = options_R.index(option)
    R = scaled[index]

    for option in options_N:
        if option == option6:
            index = options_N.index(option)
    N = scaled[index]

    for option in options_L:
        if option == option3:
            index = options_L.index(option)
    L = scaled[index]

    for option in options_D:
        if option == option4:
            index = options_D.index(option)
    D = scaled[index]

    for option in options_T:
        if option == option5:
            index = options_T.index(option)
    T = scaled[index]

    NRT_constants = {"E":0.194, "S":0.225, "R":0.177, "N":0.146, "L":0.097, "D":0.082, "T":0.079}
    
    actual_NRT = E*NRT_constants["E"] + S*NRT_constants["S"] +  R*NRT_constants["R"] +  N*NRT_constants["N"] +  L*NRT_constants["L"] +  D*NRT_constants["D"]+ T*NRT_constants["T"]

    return actual_NRT


#...............calc function runs when calc is press....................................
def calc():
    
    actual_value = solve()
    
    st.write("Number of Rescue Team Required (NRT):  {}".format(actual_value))
    if (actual_value - int(actual_value))!=0:
      st.write("Approximated NRT:  {}".format(math.ceil(actual_value)))

#.................calculate button for getting output...............................
if st.button("calc"):
  calc()
