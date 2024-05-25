#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:54:00 2024

@author: irajkoohi
"""

# https://discuss.streamlit.io/t/can-i-add-to-a-selectbox-an-other-option-where-the-user-can-add-his-own-answer/28525
# https://discuss.streamlit.io/t/new-library-streamlit-jupyter-a-new-way-to-develop-streamlit-apps-in-jupyter-notebooks/35679
# https://www.google.com/search?q=how+to+deploy+streamlit+app+to+github&sca_esv=4b73ca8f0ec787dd&sca_upv=1&rlz=1CDGOYI_enUS1103US1103&hl=en-US&biw=390&bih=669&tbm=vid&sxsrf=ADLYWIKqs27KbY7ke8u2fICf8o5vJEfnOA%3A1716598267248&ei=-zVRZt_cDoyv5NoPx8Gz2AQ#fpstate=ive&vld=cid:5a4d68cb,vid:B0MUXtmSpiA,st:0



import pandas as pd
import streamlit as st
import os, pickle, datetime
from pprint import pprint
from IPython.display import display, HTML


pd.options.display.max_columns = None
pd.options.display.max_rows = None

#%%
def display(data):
    for key, value in data.items():
        st.write(f"{key}: {value}\n")   
        #print(f"{key}: {value}\n") 
    return None   

# def proc():
#     text = st.session_state.text_key
#     return text
# text = st.text_area('enter text', on_change=proc, key='text_key')
# st.write(text)

def data_dict():
    data = {
            'Personal_info':
                {
                    'FullName': '',
                    'Email':    '',
                    },
            'Demographics':
                {
                    'Area':             '',
                    'Sub_sector':       '',
                    'Institution_type': '',
                    'Job_title':        '',
                    },
            'Current_State':
                {
                    'CS_A_1': '',
                    'CS_A_2': '',
                    'CS_A_3': '',
                    },
            'Previous_Efforts':
                {
                    'PE_A_1': '',
                    'PE_A_2': '',
                    },
            'Previous_Strategy':
                {
                    'PS_A_1': '',
                    'PS_A_2': '',
                    },
            'Idea':
                {
                'Name':           '',
                'Desc':           '',
                'Key_objectives': '',
                'Requirements':   '',
                'Owner':          '',   
                },
            'Date': {
                'Date' : '',
                },
        }
    return data
data   = data_dict()  
record = pd.json_normalize(data) 

#%%     
Introduction = """
Thank you for agreeing to take our survey. This survey should take approximately 10-20 minutes to complete.

The goal of this survey is to gather your perspective on opportunities for economic development in Puerto Rico. For the industry you are specialized in, the survey will ask you about the current state landscape, prior initiatives and their effects, Puerto Rico’s positioning and potential go-forward strategy.

Lastly, we want to assure you that all information you provide will be kept strictly confidential. You will not be required to provide any personally identifiable information and your responses will not be used for any kind of solicitation. If you choose to provide your name (albeit optional), please rest assured that none of your responses will be published in a way that is tied to your name/contact information. All responses will only be used in aggregate and only for research purposes.
"""
      
if True:
    Personal_questions = [
        "Please provide your full name (first and last name).",
        "Please provide your work/company email.",
    ] 
    Demographic_questions = [
        "Which of the following best describes the industry in which you work? Please select only one – that which describes the majority of the activities executed by your organization.", 
        "Which of the following best defines the type of institution you work for?",
        "Which best reflects your current job title?",
        ]
    CS_questions = [
        "What are priority enablers for growth in your industry? (e.g., government incentives, quality of infrastructure, workforce talent, cost of energy or logistics)",
        "What challenges is your industry facing in Puerto Rico? (e.g., market dynamics, policies)",
        "What are the assets that Puerto Rico offers to your industry? (e.g., market dynamics, policies)"
        ]
    PE_questions = [
        "What strategies/projects/policies have been beneficial for your industry in Puerto Rico? (e.g., tax credits, public-private partnerships, private sector efforts) And why?",
        "What strategies/projects/policies have not been successful in your industry in Puerto Rico? (e.g., tax credits, public-private partnerships, private sector efforts) And why?"   
        ]
    Strategy_questions = [
        " Over the next 10 years, what are the most significant outcomes you want to see in your industry in Puerto Rico? Please comment on job creation, investment, GDP growth, among others.",
        "Are there any other countries or states that are powerhouses in your industry? What can Puerto Rico learn from their strategies and models?"   
        ]
    Ideas = [
        "Provide 3-5 big ideas that your company or the sector should focus on in the future. Please provide as many details as possible."
        ]    
else:
    Personal_questions = [
        """
        Please provide your full name (first and last name).
        """,
        """
        Please provide your work/company email.
        """
        ]     
    Demographic_questions = [
        """
        Which of the following best describes the industry in which you work?
        Please select only one – that which describes the majority of the activities executed by your organization.
        """, 
        """
        Which of the following best defines the type of institution you work for?
        """,
        """
        Which best reflects your current job title?
        """
        ]
    CS_questions = [
        """
        What are priority enablers for growth in your industry?
        (e.g., government incentives, quality of infrastructure,
        workforce talent, cost of energy or logistics)
        """,
        """
        What challenges is your industry facing in Puerto Rico?
        e.g., market dynamics, policies)
        """,
        """
        What are the assets that Puerto Rico offers to your industry?
        (e.g., market dynamics, policies)
        """
        ]
    PE_questions = [
        """
        What strategies/projects/policies have been beneficial for your industry in PR
        (e.g., tax credits, public-private partnerships, private sector efforts)\n
        And why?
        """,
        """
        What strategies/projects/policies have not been successful in your industry in PR?
        (e.g., tax credits, public-private partnerships, private sector efforts)\n
        And why?
        """
        ]
    Strategy_questions = [
        """
        Over the next 10 years,\n
        what are the most significant outcomes you want to see in your industry in PR?
        Please comment on job creation, investment, GDP growth, among others.
        """,
        """
        Are there any other countries or states that are powerhouses in your industry?
        What can Puerto Rico learn from their strategies and models?
        """   
        ]
    Ideas = [
        """
        Provide 3-5 big ideas that your company or the sector should focus on in the future.
        Please provide as many details as possible.
        """
        ]    

st.write(f'Introduction\n {Introduction}')
#st.markdown("Enter the details of the new company below.")
#form = st.form(key="Demographic_questions")   
FullName = st.text_input(label='Full Name')
Email    = st.text_input(label='Email')

with st.form(key="form_1"):    
    st.write(Demographic_questions[0]) 
    Area = st.selectbox(label="Area", options=["Agriculture", "Commerce", "Family affairs", "Hospitality & tourism" , "Infrastructure", "Manufacturing", "Professional consulting", "Technology", "Back-office support", "Digital media and video production", "Education and workforce", "Financial services", "Healthcare insurance", "Healthcare services", "Insurance", "Public safety", "Telecommunications", "Transportation & logisticsculture", "Other"])
    Area_selected = st.form_submit_button(label="Select Area", disabled=False) 
    if Area == "Other": 
        Area = st.text_input("Enter your Area")
        if Area and not Area.isspace():
            Sub_sector = st.selectbox(label="Sub_sector", options=[Area, "Other"]) 
            if Sub_sector == "Other": 
                Sub_sector = st.text_input("Enter your Sub-sector")
                if Sub_sector and not Sub_sector.isspace():
                    st.info(f":white_check_mark: Sub_sector: {Sub_sector}")
    if Area == "Agriculture":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Forestry", "Fisheries"])     
    elif Area == "Commerce":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Exports", "Branding", "Promotions"])
    elif Area == "Family affairs":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Income", "Nutrition", "Social Services"])
    elif Area == "Hospitality & tourism":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Sports", "Recreation", "Culture"])
    elif Area == "Infrastructure":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Broadband", "Energy", "Housing", "Transportation", "Water"])
    elif Area == "Manufacturing":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Aerospace & defense", "Biopharma", "Disaster recovery", "Medical devices", "Apparel", "Food and Beverage"])
    elif Area == "Professional consulting":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Legal", "Business", "IT"])
    elif Area == "Technology":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Artificial intelligence", "Cybersecurity", "Data & analytics", "Enabling digital infrastructure"])
    elif Area == "Back-office support":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Back-office support"])
    elif Area == "Digital media and video production":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Digital media and video production"])
    elif Area == "Education and workforce":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Education and workforce"])
    elif Area == "Financial services":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Financial services"])
    elif Area == "Healthcare insurance":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Healthcare insurance"])
    elif Area == "Healthcare services":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Healthcare services"])
    elif Area == "Insurance":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Insurance"])
    elif Area == "Public safety":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Public safety"])
    elif Area == "Telecommunications":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Telecommunications"])
    elif Area == "Transportation & logistics":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Transportation & logistics"])
    elif Area == "Other":
        Sub_sector = st.selectbox(label="Sub_sector", options=["Other"])   
    if Area and not Area.isspace():
        SS_selected = st.form_submit_button(label="Select Sub-sector", disabled=False)  
    else:
        SS_selected = st.form_submit_button(label="Select Sub-sector", disabled=True) 
                 
with st.form(key="form_2"):   
    if SS_selected:
        st.write(Demographic_questions[1])   
        st.write("""
                  a.	Large Employer (e.g., one of the biggest employers and/or most influential companies in my industry in Puerto Rico)\n
                  b.	Small / Incoming Business (e.g., small employer in your industry that has been in Puerto Rico for many years, new company in your industry to Puerto Rico)\n
                  c.	Start-Up Business (e.g., high-growth/innovative company in your industry in Puerto Rico)\n
                  d.	Industry Association (e.g., coalition of company representatives and industry experts, special interest group)\n
                  e.	Community Development Organization (e.g., non-profits, community groups, think-tanks, academics)\n
                  f.	Other
                  """)
    Institution_type = st.selectbox(label="Institution_type", options=["Large Employer", "Small/Incoming Business", "Start-Up Business", "Industry Association" , "Community Development Organization", "Other"])    
    IT_selected = st.form_submit_button(label="Select Institution", disabled=False) 
    if Institution_type == "Other": 
        Institution_type = st.text_input("Enter your Institution_type")
        if Institution_type and not Institution_type.isspace():
            st.info(f":white_check_mark: Institution_type: {Institution_type}")

with st.form(key="form_3"):   
    if IT_selected:
        st.write(Demographic_questions[2]) 
        st.write("""
                  a.	C-Suite (e.g., CEO, Founder, Owner)\n
                  b.	Senior Leadership (VP and higher)\n
                  c.	Management (e.g., Manager, Director)\n
                  d.	Other
                  """)        
    Job_title  = st.selectbox(label="Job_title", options=["C-Suite", "Senior Leadership", "Management", "Other"])
    JT_selected = st.form_submit_button(label="Select Job Title", disabled=False)
    if Job_title == "Other": 
        Job_title = st.text_input("Enter your Job_title")
        if Job_title and not Job_title.isspace():
            st.info(f":white_check_mark: Institution_type: {Job_title}")

CS_A_1 = st.text_area(label=CS_questions[0])
CS_A_2 = st.text_area(label=CS_questions[1])
CS_A_3 = st.text_area(label=CS_questions[2])    
PE_A_1 = st.text_area(label=PE_questions[0])
PE_A_2 = st.text_area(label=PE_questions[1])
PS_A_1 = st.text_area(label=Strategy_questions[0])
PS_A_2 = st.text_area(label=Strategy_questions[1])

st.write(Ideas[0]) 
Idea_Name           = st.text_area(label='Name')
Idea_Desc           = st.text_area(label='Desc')
Idea_Key_objectives = st.text_area(label='Key_objectives')
Idea_Requirements   = st.text_area(label='Requirements')
Idea_Owner          = st.text_area(label='Owner')
with st.form(key="form_4"):   
    Submit_Questionary = st.form_submit_button(label="Submit Questionary", disabled=False)           
    if Submit_Questionary:    
        record['Personal_info.FullName']        = FullName   
        record['Personal_info.Email']           = Email
        record['Demographics.Area']             = Area
        record['Demographics.Sub_sector']       = Sub_sector
        record['Demographics.Institution_type'] = Institution_type
        record['Demographics.Job_title']        = Job_title
        record['Current_State.CS_A_1']          = CS_A_1   #  en(df['Current_State.CS_A_1'].iloc[10]): 163765         
        record['Current_State.CS_A_2']          = CS_A_2             
        record['Current_State.CS_A_3']          = CS_A_3            
        record['Previous_Efforts.PE_A_1']       = PE_A_1
        record['Previous_Efforts.PE_A_2']       = PE_A_2
        record['Previous_Strategy.PS_A_1']      = PS_A_1
        record['Previous_Strategy.PS_A_2']      = PS_A_2    
        record['Idea.Name']                     = Idea_Name
        record['Idea.Desc']                     = Idea_Desc
        record['Idea.Key_objectives']           = Idea_Key_objectives
        record['Idea.Requirements']             = Idea_Requirements
        record['Idea.Owner']                    = Idea_Owner
        record['Date.Date']                     = datetime.datetime.now()
 
        st.write(record)    
        if not os.path.exists(('df.csv')): 
            #df = pd.json_normalize(data) 
            df = record.copy()
            df.dropna(subset=['Demographics.Area'], inplace=True)
        else:
            df = pd.read_csv("df.csv")  
        df = df._append(record, ignore_index=True)
        df = df.drop_duplicates(subset=['Personal_info.FullName', 'Personal_info.Email',
                                        'Demographics.Area', 'Demographics.Sub_sector', 'Demographics.Institution_type', 'Demographics.Job_title',
                                        'Current_State.CS_A_1', 'Current_State.CS_A_2', 'Current_State.CS_A_3', 
                                        'Previous_Efforts.PE_A_1','Previous_Efforts.PE_A_2', 
                                        'Previous_Strategy.PS_A_1', 'Previous_Strategy.PS_A_2',
                                        'Idea.Name', 'Idea.Desc', 'Idea.Key_objectives', 'Idea.Requirements', 'Idea.Owner'], keep='first', ignore_index=True)
        df.to_csv('df.csv', index=False)  
        print("Questionary Submitted!")  
           
#%%

