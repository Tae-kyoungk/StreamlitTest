import streamlit as st
from PIL import Image

st.title('C421001 강태경')
st.header('👩🏻‍💻 파이썬 프로그래밍 개인 프로젝트 👩🏻‍💻')
st.markdown('### streamlit을 이용하여 개인 홈페이지를 개설하였습니다.')
st.markdown("&nbsp;")

st.write('## 1. 관심분야 (OTT 산업, 기후 위기)')
st.markdown('## 1️⃣ **OTT 산업**')
img = Image.open('ott1.PNG')
st.image(img, width=600)
st.markdown("&nbsp;")
st.markdown(
    '''
    ### ✅OTT의 정의
    - #### **'Over-The-Top'의 줄임말로, 인터넷을 통해 제공되는 온라인 동영상 서비스를 의미한다.**

    ### ✅OTT의 특징
    - #### **사용자가 시•공간적 제약 없이 콘텐츠를 선택 후 시청이 가능하다. 즉, 편성표에 구애받지 않는다.**
    - #### **사용자의 시청 패턴과 선호도를 분석하여 콘텐츠 추천 시스템을 운영한다.**
    - #### **스마트폰, 테블릿, TV, 게임 콘솔 등 다양한 기기에서 시청이 가능하도록 지원한다.** 

    ### ✅OTT의 종류
    - #### **[넷플릭스(NETFLIX)](https://www.netflix.com/kr/)**
    - #### **[디즈니 플러스(Disney+)](https://www.disneyplus.com/ko-kr)**
    - #### **[티빙(TVING)](https://www.tving.com/onboarding)**
    - #### **[왓챠(WATCHA)](https://watcha.com/browse/theater)**
    - #### **[웨이브(Wavve)](https://www.wavve.com)**
    - #### **글자 클릭 시 각 OTT 플랫폼 홈페이지로 이동한다.**
    - #### **이 외에도 쿠팡 플레이, 애플 티비, 아마존 프라임 비디오, 유튜브 등이 운영되고 있다.**

    ### ✅OTT 산업 속 데이터 분석가의 역할
    - #### **<span style="color:#278f43">OTT 구독자 데이터 분석</span>: 구독자의 시청 이력, 인구통계학적 데이터, 선호 장르와 배우 등의 방대한 데이터를 수집한다.**
    - #### **<span style="color:#278f43">개인 맞춤 콘텐츠 추천</span>: 수집한 데이터를 활용해 구독자의 시청 패턴, 선호도, 이탈 위험 등을 분석한다. 이를 기반으로 정밀한 추천 시스템 개선을 통해 구독자 만족도를 높인다.**
    - #### **<span style="color:#278f43">마케팅 전략 수립</span>: 분석한 내용으로 구독자들의 니즈를 파악하여, 기존 구독자 유지 및 신규 가입자 유치 전략에 도움을 준다.**
    - #### **<span style="color:#278f43">운영 효율성 및 최적화</span>: OTT 플랫폼의 서버 사용량, 트래픽 패턴, 인기 콘텐츠 등을 분석해 운영 비용 절감 및 최적화에 기여한다.**
    - #### **<span style="color:#278f43">전망</span>: OTT 시장의 지속적인 성장은 데이터 분석가에 대한 수요가 지속될 것으로 예상되어 전망 또한 긍정적으로 볼 수 있다.**
    
    ### ✅🎬희망 진로: <span style="color:#f00f07">OTT 산업 데이터 분석가</span>
    - #### **영화 산업에 대한 깊은 관심을 바탕으로 다양한 기준을 통해 영화를 분류하고 평가하는 작업을 즐겨해왔다.**
    - #### **모바일 기기를 이용한 시청 보편화 등의 장점으로 최근 급성장 중인 OTT 플랫폼 분야에도 자연스레 관심을 가지게 되었다.**
    - #### **이를 바탕으로 <span style="color:#f00f07">OTT 산업의 데이터 분석가</span>로 활동하며 <span style="color:#f00f07">구독자 데이터 분석과 추천 시스템 개선 등을 통해 OTT 서비스의 비즈니스 인사이트 도출에 기여</span>하고 싶다.**
    '''
    , unsafe_allow_html=True)

st.markdown('##  2️⃣**기후 위기**')
img = Image.open('CC1.PNG')
st.image(img, width=600)
st.markdown("&nbsp;")
st.markdown(
    '''
    ### ✅기후위기의 정의
    - #### **지구온난화, 이상기후 등으로 인해 생태계와 인류사회에 심각한 영향을 미치는 현상을 말한다.**

    ### ✅기후위기의 심각성
    - #### **폭염, 가뭄, 홍수, 태풍, 엘리뇨 등 이상기후가 자주 발생하고, 강도도 높아지고 있다.**
    - #### **해수면 상승, 산림 파괴 등으로 동식물 서식지가 파괴뿐만 아니라 인간의 생활도 위협하고 있다.**

    ### ✅기후위기 속 데이터 분석가의 역할
    - #### **<span style="color:#278f43">데이터 분석</span>: 방대한 기후 데이터, 환경 데이터, 사회경제 데이터 등을 체계적으로 수집하고 정제하여 분석한다.**
    - #### **<span style="color:#278f43">예측 모델 개발</span>: 기후 변화, 이상기후, 탄소중립 등에 대한 예측 모델을 개발한다. 이를 통해 미래 기후 시나리오를 만들어 기후변화 모니터링과 대응 정책 수립을 지원한다.**
    - #### **<span style="color:#278f43">사회•경제적 영향</span>: 기후위기로 인한 취약계층의 피해 예측, 공공 인프라 등 전반적인 사회•경제적 영향을 분석한다.**
    - #### **<span style="color:#278f43">전망</span>: 기후위기에 대한 관심과 우려가 높아짐에 따라서 기후 전문 데이터 분석가에 대한 수요가 지속적으로 증가할 것으로 예상된다.**

    ### ✅🌍희망 진로: <span style="color:#f00f07">기후 분야 데이터 분석가</span>
    - #### **기후위기의 심각성을 인지했기에 개인으로서 할 수 있는 행동이 무엇이 있는지 고민해왔다. 그래서 기후 전문 데이터 분석가로 활동하고 싶은 소망이 있다.**
    - #### **위성 데이터, 지질 데이터, 해양 데이터 등 <span style="color:#f00f07">다양한 기후 관련 데이터를 분석하여 기후변화 예측 시나리오를 개발하여 정부 및 전세계의 기후위기 대응 정책 수립에 기여</span>하고 싶다.**
    - #### **'기후위기'라는 도메인에서 활동하는 데이터 분석가로서 전세계적 난제인 <span style="color:#f00f07">기후위기 대응에 실질적인 도움을 주는 것</span>이 목표이다.**
''' , unsafe_allow_html=True)
