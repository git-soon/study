#실습6. 함수 종합 프로그래밍
#초기 날씨데이터
weather_data = [
    ["2024-11-20", "서울", 15.2, 0.0],
    ["2024-11-20", "부산", 18.4, 0.0],
    ["2024-11-21", "서울", 10.5, 2.3],
    ["2024-11-21", "부산", 14.6, 1.2],
    ["2024-11-22", "서울", 8.3, 0.0],
    ["2024-11-22", "부산", 12.0, 0.0]
]

#평균 기온 계산 함수
def avg_temperatures(weather):
    city = input("도시 이름을 입력하세요: ")

    total = 0
    count = 0
    for data in weather:
        if data[1] == city:
            total += data[2]
            count += 1
    return city, total / count

    # temp = filter(lambda x : x[1] == city, weather)
    # temperatures = list(map(lambda x : x[2], temp))
    # if not temperatures:
    #     return city, None
    # else:
    #     return city, sum(temperatures) / len(temperatures)
    
# 최고/최저 기온 찾는 함수
def maxmin_temperatures(weather):
    city = input("도시 이름을 입력하세요: ")
    temperatures = [  data[2]  for data in weather if data[1] == city ]
    # temp = filter(lambda x : x[1] == city, weather)
    # temperatures = list(map(lambda x : x[2], temp))
    if not temperatures:
        return city, None, None
    else:
        return city, max(temperatures), min(temperatures)
    
# 강수량과 비온날을 찾는 함수
def total_rain_day(weather):
    city = input("도시 이름을 입력하세요: ")
    temp = filter(lambda x : x[1] == city, weather)
    rain = list(map(lambda x : x[3], temp)) # 강수량
    total_rain = sum(rain) # 총 강수량
    rain_day = len(list(filter(lambda x : x > 0, rain))) #비가온날
    return city, total_rain, rain_day

# 데이터 추가 함수
def add_weather(weather):
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시 이름을 입력하세요: ")
    temperatures = float(input("평균기온을 입력하세요 (℃) : "))
    rain = float(input("강수량을 입력하세요 (mm) : "))
    weather.append([date, city, temperatures, rain])
    return city

# 전체 데이터 출력
def all_print(weather):
    print("\n현재 저장된 날씨 데이터")
    for data in weather:
        print(f"날짜: {data[0]}, 도시: {data[1]}, 평균기온: {data[2]}℃ , 강수량: {data[3]}mm")


def main_program():
    while True:
        print("\n[날씨 데이터 분석 프로그램]")
        print("1. 평균 기온 계산")
        print("2. 최고/최저 기온 찾기")
        print("3. 강수량 분석")
        print("4. 날씨 데이터 추가")
        print("5. 전체 데이터 출력")
        print("6. 종료")
        choice = input("원하는 기능의 번호를 입력하세요: ")
        if choice == "1":
            city, avg = avg_temperatures(weather_data)
            if avg is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 평균기온은 {avg:.2f}℃")

        elif choice == "2":
            city, max_value, min_value = maxmin_temperatures(weather_data)
            if max_value is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 최고기온은 {max_value}℃ , 최저기온은 {min_value}℃")

        elif choice == "3":
            city, total_rain, rain_day = total_rain_day(weather_data)
            print(f"{city}의 총 강수량: {total_rain:.1f}mm")
            print(f"{city}의 비가온날: {rain_day}일")

        elif choice == "4":
            city = add_weather(weather_data)
            print(f"{city}의 날씨 데이터가 추가되었습니다")

        elif choice == "5":
            all_print(weather_data)
        
        elif choice == "6":
            print("프로그램을 종료합니다")
            break
        else:
            print("1~6까지의 번호를 입력하세요")
            

#프로그램 실행 함수
main_program()