#imports
import streamlit as st 
import pandas as pd 

#any config variables 
#Wide layout
st.set_page_config(layout="wide")

#runtime variables 
questionbank = {
    1:{
        "q":"How to enhance the functionality of a function?",
        "a":['function overloading','operator overloading','decorators'],
        "k":"decorators"
    },
    2:{
        "q":"Select the correct library that helps in data analysis ? ",
        "a":['pandas','nltk','streamlit'],
        "k":"pandas"
    },
    3:{
        "q":"Select a library that you can use for creating charts ? ",
        "a":['streamlit','seaborn'],
        "k":"seaborn"
    },
    4:{
        "q":"Select a plot that helps you analyse more than 3 variables ? ",
        "a":['scatterplot','boxplot','historgram'],
        "k":"scatterplot"
    },
    5:{
        "q":"Select the method that doesnt depends on the instance  ? ",
        "a":['instance method','class method','static method'],
        "k":"static method"
    },
}


#functions 
if 'count' not in st.session_state:
	st.session_state.count = 0

def increment_counter():
	st.session_state.count += 1


def main ():
    st.title("Welcome to Streamlit")
    menu = ["Home","Quiz","NLTK Activity"] # defining the menu items as a list
    choice = st.sidebar.selectbox("Menu",menu,index=1) # show the index option to show how to pre-select menus
    
    if choice=='Home':
        st.write(f"Welcome to {choice} page") # do not hard code the values 
    elif choice=='Quiz':
        st.write(f"Welcome to {choice} page")
        # start a quiz here by showing questions         
        question_container = st.container() # declare a container and start the magic                 
        for k,v in questionbank.items(): # 
            with question_container: # scope statement
                st.write(f" Question {k} : {v.get('q')} ") # Question 
                answer = st.radio('Answers',v.get('a'),horizontal = True) # Answer
                submit = st.button("Submit",key=f"question{k}") # Submit button 
                if submit:
                    #show whether the option is correct or incorrect
                    if answer==v.get('k'):
                        st.success(f"You selected the option {answer} ! - Correct ")
                        increment_counter()
                    else:
                        st.error(f"You selected the option {answer} - Incorrect ",icon="⚠️")        
                        

        #outside the for container
        validate=st.button("Final Scores",key=f"scores")
        if validate:
            st.write (f"Thanks for taking the quiz . Your score is {st.session_state.count}" )
            # reset the counter 
            st.session_state.count = 0 

    elif choice=='NLTK Activity':
        st.write(f"Welcome to {choice} page ..  ")
    else:
        st.write(f"Welcome to {choice} page ..  ")





#starting point
if __name__ == "__main__":
    main()
