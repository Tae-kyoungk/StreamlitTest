import streamlit as st
from PIL import Image

st.write('# 2. 취업하고 싶은 기업소개')
st.markdown('## 1️⃣ **티빙 (TVING)**')
img = Image.open('tving.png')
st.image(img, width=600)
st.markdown("&nbsp;")
st.markdown('''
    - ##### <span style="color:#f00f07">티빙</span>은 CJ ENM이 운영하는 국내 대표 OTT 플랫폼이다. 
    - ##### CJ ENM 계열의 드라마와 예능 등의 방송 콘텐츠를 제공하고, 실시간 시청이 가능한 채널 또한 이용할 수 있다. 이외에도 국내외 영화, 독점 콘텐츠 또한 제공한다.
    - ##### 모바일, PC와 스마트TV 등 다양한 환경에서 OTT 서비스를 자유롭게 이용할 수 있다.
''', unsafe_allow_html=True)
st.markdown(
'''
    ### ✅'데이터 분석' 직무
    - ##### 티빙에서는 클라우드 엔지니어, 정보보안, 백엔드 개발, 앱개발, 데이터 분석, 미디어 엔지니어 등 다양한 직무를 채용하고 있다.
    - ##### 그 중 가장 관심있고, 취업하고 싶은 직무는 <span style="color:#f00f07">'데이터 분석'</span>이다.

    ### ✅담당 업무
    - ##### <span style="color:#278f43">데이터 지표 관리와 통계 분석 및 비즈니스 인사이트 도출</span>을 담당한다.
    - ##### <span style="color:#278f43">로그 수준의 데이터 가공을 바탕으로 기획, 설계 및 데이터 분석 툴(tool)</span>을 운영한다.
'''
, unsafe_allow_html=True)

st.markdown('## 2️⃣ **국립기상과학원**')
img = Image.open('ki.PNG')
st.image(img, width=600)
st.markdown("&nbsp;")
st.markdown('''
    - ##### 기상청 소속기관이다. 
    - ##### 기획운영과, 예보연구부, 관측연구부, 기후연구부, 기상응용연구부, 지구대기감시연구과, 인공지능기상연구과, 기후변화예측연구팀으로 구성되어 있다.
    - ##### 기후·기후변화 예측모델의 개발에 관한 연구와 기후 및 기후변화에 관한 연구를 추진한다.''')
st.markdown('''
    ### ✅국립기상과학원 '기후연구부' 
    - ##### 기후변화감시, 환경기상 연구, 지구대기 등의 관측 분석 및 연구를 수행한다. <span style="color:#f00f07">'기후모델개발'과 '현업 기후예측시스템의 운영·관리', '기후예측자료의 생산·지원·관리'</span>를 진행한다. 
    - ##### APEC 기후센터 기관 운영 감독과 세계기상기구 육불화황 세계표준센터를 운영한다.
            
    ### ✅'기후연구부 현업시스템 운영 모니터링' 업무
    - ##### <span style="color:#278f43">기후예측시스템/전지구 자료동화시스템 현업 운영 및 모니터링, 자료전송, 장애대응</span>을 진행한다.
    - ##### <span style="color:#278f43">기후예측시스템의 민감도를 실험하고, 대용량/기상기후 수치모델 자료 제공 업무</span>를 지원한다.

''', unsafe_allow_html=True)
