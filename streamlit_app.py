import streamlit as st

# [출력] 앱의 제목과 간단한 설명
st.title("🏆 3등을 찾아라! 프로그램")
st.write("학생들의 이름과 점수를 입력하면, 정확히 3등을 한 사람을 찾아주는 프로그램입니다.")

st.markdown("---")

# [입력] 텍스트 상자를 통해 사용자로부터 데이터를 입력받음 (기본값 설정)
st.subheader("1. 데이터 입력하기")
user_input = st.text_area(
    "이름과 점수를 한 줄에 하나씩 입력하세요. (형식: 이름 점수)",
    value="김철수 95\n이영희 88\n박민수 92\n최수연 79\n정태양 85\n강바다 71",
    height=180
)

# [출력/조건문] 버튼을 누르면 프로그램이 실행되도록 설정
if st.button("📊 3등 결과 분석하기"):
    
    # 데이터를 담을 빈 리스트 생성
    students_data = []
    
    # [반복문] 입력된 텍스트를 줄 바꿈(\n) 기준으로 잘라서 한 줄씩 처리
    lines = user_input.strip().split("\n")
    for line in lines:
        if line.strip():  # 빈 줄이 아닐 때만 실행
            try:
                # 공백을 기준으로 이름과 점수를 분리
                name, score_str = line.split()
                score = int(score_str)  # 점수를 숫자로 변환
                students_data.append((name, score))
            except ValueError:
                st.error(f"⚠️ 형식 오류: '{line}' 문장을 확인해 주세요. (예: 홍길동 90)")
                st.stop()

    st.subheader("2. 분석 결과")

    # [조건문] 입력된 데이터가 3개 미만일 때 예외 처리
    if len(students_data) < 3:
        st.warning("⚠️ 3등을 찾으려면 최소 3명 이상의 데이터를 입력해야 합니다.")
    
    else:
        # [데이터 처리] 점수를 기준으로 내림차순 정렬 (높은 점수가 앞으로)
        students_data.sort(key=lambda x: x[1], reverse=True)
        
        # 중복을 제거한 점수 목록을 만들어 정확한 순위 기준을 세움
        unique_scores = sorted(list(set([score for name, score in students_data])), reverse=True)
        
        # [조건문] 서로 다른 점수가 3개 이상 존재하지 않는 경우 처리
        if len(unique_scores) < 3:
            st.info("ℹ️ 점수의 종류가 부족하여 3등을 결정할 수 없습니다. (모두 동점이거나 1, 2등만 존재)")
        
        else:
            # 3번째로 높은 점수를 '3등 점수'로 지정
            third_score = unique_scores[2]
            
            # [반복문 & 조건문] 3등 점수를 가진 사람들을 찾아서 리스트에 저장
            third_place_winners = []
            for name, score in students_data:
                if score == third_score:  # 조건문: 점수가 3등 점수와 같다면
                    third_place_winners.append(f"{name}({score}점)")
            
            # [출력] 최종 결과 발표
            # 조인(join)을 사용해 공동 3등이 있을 경우도 깔끔하게 출력합니다.
            result_names = ", ".join(third_place_winners)
            st.success(f"🎉 축하합니다! 이번 명단에서 3등은 **{result_names}** 입니다!")
            
            # [출력 & 반복문] 전체 순위를 한눈에 보기 좋게 표 형태로 정렬하여 보여줌
            st.write("---")
            st.markdown("### 📋 전체 순위 리스트")
            
            for idx, (name, score) in enumerate(students_data, start=1):
                # 가독성을 위해 3등은 강조 표시
                if score == third_score:
                    st.write(f"⭐ **{idx}등 : {name} ({score}점)** - [3등 완료]")
                else:
                    st.write(f"▫️ {idx}등 : {name} ({score}점)")