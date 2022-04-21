import streamlit as st

def main():
    st.title("Simple streamlit blog")
    
    menu = ["Home", "Preferences", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Home")
        
    elif choice == "Preferences":
        st.subheader("Preferences")
        
    elif choice == "About":
        st.subheader("ifykyk")
        
if __name__ == '__main__':
    main()



