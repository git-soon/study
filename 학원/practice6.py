
# 실습 6. 함수 종합 프로그래밍
# 데이터 분석 할수있는 함수들을 생성하여 제작
# 1. 도시별 평균 기온 계산
# 2. 도시별 최고/ 최소 기온 찾기
# 3. 도시별 강수량 분석
# 4. 데이터 추가
# 5. 전체 데이터 출력
# 6. 종료


while True:

    wheather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-21", "서울", 8.3, 0.0],
    ["2024-11-21", "부산", 12.0, 0.0]
    ]

    start_menu = input("\n\n [날씨 데이터 분석 프로그램 \n 1.평균 기온 계산  \n 2.최고/최저 기온 찾기 \n 3.강수량 분석 \n 4.날씨 데이터 추가 \n 5.전체 데이터 출력 \n 6.종료 \n 원하는 기능의 번호를 입력하세요 : " )
   
    
    # 1. 도시별 평균 기온 계산
    if start_menu == "1":
        city = input("도시 이름을 입력하세요 : ")
        if city == '서울':
            a = filter(lambda x : x[1] == city, wheather_data ) # 서울만 값 분리하기기
            b = list(map(lambda x : x[2], list(a))) #서울의 평균 기온 값만 뽑아낸거
            # 이 다음은 뽑아낸 기온들 다 더해서 list 길이 만큼 나누면 되는거 같은데
            c = sum(b)/len(b)
            c2 = round(c,2) 
            print(f'{city}의 평균 기온 : {c2} ℃')

        elif city == '부산':
            a = filter(lambda x : x[1] == city, wheather_data ) # 부산
            b = list(map(lambda x : x[2], list(a))) #부산의 평균 기온 값만 뽑아낸거
            c = sum(b)/len(b)
            c2 = round(c,2) 
            print(f'{city}의 평균 기온 : {c2} ℃')
    



    # 2. 도시별 최고 최대 기온 찾기
    elif start_menu == "2":
         city = input("도시 이름을 입력하세요 : ")

         if city == "서울":
            a = filter(lambda x : x[1] == city, wheather_data ) # 서울만 값 분리하기기
            b = list(map(lambda x : x[2], list(a))) #서울의 평균 기온 값만 뽑아낸거
            #최대기온 H_temp ,최저기온 L_temp
            H_temp = max(b)
            L_temp = min(b)
            print(f'{city}의 최고 기온 : {H_temp}℃ ,최저기온: {L_temp}℃')

         elif city == "부산":
            a = filter(lambda x : x[1] == city, wheather_data ) # 부산
            b = list(map(lambda x : x[2], list(a))) 
            #최대기온 H_temp ,최저기온 L_temp
            H_temp = max(b)
            L_temp = min(b)
            print(f'{city}의 최고 기온 : {H_temp}℃ ,최저기온: {L_temp}℃')
    
    # 3. 강수량 분석
    elif start_menu == "3":
        city = input("도시 이름을 입력하세요 : ")

        if city == "서울":
            a = filter(lambda x : x[1] == city, wheather_data ) # 서울만 값 분리하기기
            b = list(map(lambda x : x[3], list(a))) #서울의 강수량 값만 뽑아낸거
            # 총 강수량 = 걍 다 더하기 or 0이 아닌 값만 찾아서 더하기
            #걍 다 더하기
            total_rain = sum(b)

            # 강수량 있던날  = 0이 아닌 날 = 전체 길이 - count(o)
            rain__day = len(b) - b.count(0.0)

            print (f'{city}의 총 강수량 : {total_rain}mm')
            print(f'{city}의 강수량이 있던날 : {rain__day}일')

        elif city == "부산":
            a = filter(lambda x : x[1] == city, wheather_data ) # 부산
            b = list(map(lambda x : x[3], list(a))) # 부산 
            total_rain = sum(b)
            rain__day = len(b) - b.count(0.0)

            print (f'{city}의 총 강수량 : {total_rain:.1f}mm')
            print(f'{city}의 강수량이 있던날 : {rain__day}일')


    
    # 4. 데이터 추가 append 쓰면 되것네
    elif start_menu == "4":
        day_input = input("원하는 날짜를 입력하세요 (YYYY-MM-DD) : ")
        city = input("도시 이름을 입력하세요 : ")
        avg_teamp = float(input("평균 기온을 입력하세요(℃) : "))
        rain_input = float(input("강수량을 입력하세요(mm) : "))
        wheather_data.append([day_input, city, avg_teamp, rain_input])
        print(f"{city}의 날씨 데이터가 추가 되었습니다.")
    
    # 5. 전체 데이터 출력
    elif start_menu == "5":
        print("현재 저장된 날씨 데이터")
        print(wheather_data)

    
    # 6. 종료
    elif start_menu == "6":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요")


        # day_input = input("원하는 날짜를 입력하세요 (YYYY-MM-DD) : ")
        # city = input("도시 이름을 입력하세요 : ")
        # avg_teamp = input("평균 기온을 입력하세요(`C) : ")
        # rain_input = input("강수량을 입력하세요(mm) : ") 

        