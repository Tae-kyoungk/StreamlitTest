import streamlit as st
st.set_page_config(layout="centered")

st.title('C421001 강태경')
st.header('👩🏻‍💻 파이썬 프로그래밍 개인 프로젝트 👩🏻‍💻')
st.subheader('streamlit을 이용하여 개인 홈페이지를 개설하였습니다.')
st.markdown("&nbsp;")

st.write('# 1. 관심분야 (OTT 산업, 기후 분야)')
st.markdown('## 1️⃣ **OTT 산업**')
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2. *기울임* 표시
        - 마크다운
        - 마크다운

    ## 마크다운 헤더2
    - [네이버](https://youtube.com)
    - [구글](https://google.com)

    ### 마크다운 헤더3
    일반 텍스트
    '''
    )

st.write('# 이것은 제목입니다. : st.write()')
st.write('이것은 제목입니다. : st.write()')
st.write('## 이것은 제목입니다. : st.write()')
st.title('이것은 제목입니다. : st.title()')
st.header('이것은 헤더입니다. : st.header()')
st.subheader('이것은 서브헤더입니다. : st.subheader()')
st.text('## 이것은 텍스트입니다. : st.text()')
st.markdown('## 이것은 마크다운입니다. : st.markdown()')

