import streamlit as st

st.write("""Hello my name is yashwanth""")
number = st.slider("Pick a number", 0, 100)
# s.write("")
st.write(number)
date = st.date_input("Pick a date")
# Just add it after st.sidebar:
a = st.sidebar.radio('Welcome to Streamlit',["Male","female"])
'_This_ is some __Markdown__'
a=3
# 'dataframe:', 0
# st.markdown('_Markdown_')
# st.caption('Balloons. Hundreds of them...')
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

# Show different content based on the user's email address.
# if st.user.email == 'jane@email.com':
#     display_jane_content()
# elif st.user.email == 'adam@foocorp.io':
#     display_adam_content()
# else:
#     st.write("Please contact us to get access!")

# Insert a chat message container.
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
st.chat_input("Say something")