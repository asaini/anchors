import streamlit as st
import numpy as np
import plotly.figure_factory as ff


st.sidebar.title('Sidebar Title')

st.sidebar.subheader('Sidebar subheader')

st.title('Introducing Anchor Tags with Headings')

st.write('This is a demo app to showcase the functionality of Anchor Tags')

st.markdown('''
---
With Anchor Tags, we can now create a Table of contents which links to other sections of the app.

**Table of Contents**

 - [Demo](#demo-for-anchor-tags)
    - [Section 1](#section-1)
        - [Section 1a](#section-1a)
        - [Section 1b](#section-1b)
    - [Section 2](#section-2-multiple-columns)
        - [Section 2b](#section-2b)
''')

st.title('Demo for Anchor Tags')


st.markdown('---')

st.header('Section 1')
st.markdown('''
        This is a single column section. To get the link to this, click the anchor icon to the left of the "Section 1" heading above. 
''')

st.subheader('Section 1a')
st.markdown('''
        This is a sub heading. To get the link to this, click the anchor icon to the left of the 'Section 1a' subheading above. 
        Clicking on the anchor icon will refocus the page to this subheading. 
''')

st.subheader('Section 1b')
st.markdown('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel dolor convallis, rhoncus elit a, tempus nulla. Aliquam erat volutpat. In turpis erat, fermentum nec ullamcorper nec, egestas a nibh. Nam pharetra nunc vitae sem pellentesque, vel convallis nibh convallis. Duis mattis egestas suscipit. Donec ligula mauris, lacinia ut mattis eget, blandit non ipsum. Sed lobortis semper blandit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam orci orci, porttitor vitae malesuada sit amet, pretium vel ex. Praesent quis purus ut libero dapibus dignissim. Sed tempor volutpat risus id sollicitudin. Nunc tincidunt velit elit, non ultrices tortor consectetur non. Mauris vitae molestie magna. Donec vitae hendrerit tortor, vel ultrices diam.
Maecenas blandit sapien odio, id bibendum leo consectetur vitae. Donec tempus venenatis lorem, in porta felis malesuada eget. Aenean suscipit commodo ligula. Nunc consequat volutpat mauris, ut luctus orci viverra in. Morbi sed blandit tortor. Donec at lacinia nisl, at eleifend urna. Nullam nec ligula vulputate ligula blandit ornare non in lectus. Proin blandit suscipit nisi, sed pellentesque libero suscipit in. Vivamus luctus augue augue. Vivamus consequat, nunc vitae finibus ultricies, nunc dui auctor justo, ut tincidunt ipsum enim a nibh. Donec convallis interdum diam, rhoncus porta ante bibendum a. Duis efficitur convallis condimentum.''')

st.markdown('---')

st.header('Section 2 Multiple Columns')
st.markdown('''
In this section of the app we focus on how anchors get rendered in multiple columns
''')

col1, col2 = st.beta_columns(2)

with col1:
    st.image('https://stmedia.stimg.co/ows_157235893649127.jpg?auto=compress&crop=faces&dpr=2&w=230')

with col2:
    st.subheader('On the left is a bird image')
    st.markdown('''There seems to be some overlap between the image and the anchor tag. 
* The tag is visible and discernable in Light mode. 
* Not so much in Dark Mode. This behavior can be seen in other tags down below as well.

    ''')


col1, col2 = st.beta_columns(2)

with col2:
    st.subheader('Section 2b')
    st.markdown('''
    On the left column is a plotly chart. 

We can see that there is no overlap between the chart supporting 
icons and the anchor tags icon. Moreover, both appear to only appear on hover so there is no confusion in 
distinguishing between them.
    ''')
with col1:
    # st.subheader('Section 2b')
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']

    fig = ff.create_distplot(hist_data, group_labels,
                             bin_size=[.1, .25, .5])

    st.plotly_chart(fig, use_container_width=True)
