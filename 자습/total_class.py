# # 마지막 실습
# # 날짜별 전력 사용량


# from abc import ABC, abstractmethod
# electricity = [
#     {"date": "2024-11-01", "usage": 12.5},
#     {"date": "2024-11-02", "usage": 15.3},
#     {"date": "2024-11-03", "usage": 10.8},
#     {"date": "2024-11-04", "usage": 14.2},
#     {"date": "2024-11-05", "usage": 13.6}
# ]


# # 부모 클래스: ElectricityData


# class ElectricityData(ABC):
#     # 사용 데이터를 초기화합니다. 입력된 리스트를 복사하여 내부 상태를 보호합니다.
#     def __init__(self, usage_data):
#         self._usage_data = usage_data.copy()

#     @property
#     # usage_data의 getter로, 데이터 리스트의 복사본을 반환하여 캡슐화를 유지합니다.
#     def usage_data(self):
#         return self._usage_data.copy()

#     @usage_data.setter
#     def usage_data(self, value):  # usage_data의 setter로, 입력된 리스트를 복사하여 설정합니다.
#         self._usage_data = value.copy()

#     @property
#     def total_usage(self):  # total_usage를 계산하여 반환하는 속성입니다.
#         return self.calculate_total_usage()

#     @abstractmethod
#     # 총 사용량을 계산하는 추상 메서드입니다. 자식 클래스에서 구현해야 합니다.
#     def calculate_total_usage(self):
#         pass

#     @abstractmethod
#     # 특정 날짜의 사용량을 조회하는 추상 메서드입니다. 자식 클래스에서 구현해야 합니다.
#     def get_usage_on_date(self, date):

#         pass

#     def add_usage(self, date, usage):  # 새로운 사용 데이터를 추가합니다.
#         self._usage_data.append({"date": date, "usage": usage})

#     def remove_usage(self, date):  # 지정된 날짜의 사용 데이터를 삭제합니다.

#         self._usage_data = [
#             data for data in self._usage_data if data["date"] != date]

# # 자식 클래스: HomeElectricityData


# class HomeElectricityData(ElectricityData):
#     def calculate_total_usage(self):
#         """총 전력 사용량을 계산합니다. 사용량의 합계를 반환합니다."""
#         return sum(data["usage"] for data in self._usage_data)

#     def get_usage_on_date(self, date):
#         """특정 날짜의 사용량을 조회합니다. 없으면 예외를 발생시킵니다."""
#         for data in self._usage_data:
#             if data["date"] == date:
#                 return data["usage"]
#         raise ValueError(f"{date}에 대한 데이터가 없습니다.")

#     @classmethod
#     def filter_by_date_range(cls, usage_data, start_date, end_date):
#         """특정 날짜 범위 내의 데이터를 필터링하여 반환합니다."""
#         return [data for data in usage_data if start_date <= data["date"] <= end_date]

#     @staticmethod
#     def find_highest_usage(usage_data):
#         """데이터에서 가장 높은 사용량을 찾아 반환합니다. 데이터가 없으면 예외를 발생시킵니다."""
#         if not usage_data:
#             raise ValueError("데이터가 없습니다.")
#         return max(data["usage"] for data in usage_data)


# # 테스트 코드
# if __name__ == "__main__":
#     # 샘플 데이터 초기화
#     electricity_usage = [
#         {"date": "2024-11-01", "usage": 12.5},
#         {"date": "2024-11-02", "usage": 15.3},
#         {"date": "2024-11-03", "usage": 10.8},
#         {"date": "2024-11-04", "usage": 14.2},
#         {"date": "2024-11-05", "usage": 13.6}
#     ]

#     # HomeElectricityData 인스턴스 생성
#     home_data = HomeElectricityData(electricity_usage)

#     # 총 사용량 출력
#     print(f"총 사용량: {home_data.total_usage}")  # 66.4

#     # 특정 날짜 사용량 조회
#     # 10.8
#     print(f"2024-11-03 사용량: {home_data.get_usage_on_date('2024-11-03')}")

#     # 데이터 추가
#     home_data.add_usage("2024-11-06", 11.0)
#     print(f"데이터 추가 후 총 사용량: {home_data.total_usage}")  # 77.4

#     # 데이터 삭제
#     home_data.remove_usage("2024-11-02")
#     print(f"데이터 삭제 후 총 사용량: {home_data.total_usage}")  # 62.1

#     # 날짜 범위 필터링
#     filtered_data = HomeElectricityData.filter_by_date_range(
#         home_data.usage_data, "2024-11-03", "2024-11-05"
#     )
#     print("2024-11-03 ~ 2024-11-05 데이터:", filtered_data)

#     # 가장 높은 사용량 찾기
#     highest = HomeElectricityData.find_highest_usage(home_data.usage_data)
#     print(f"가장 높은 사용량: {highest}")  # 14.2

#     # 예외 처리 테스트
#     try:
#         HomeElectricityData.find_highest_usage([])
#     except ValueError as e:
#         print(f"예외 발생: {e}")


#         코드 설명
# ElectricityData 클래스(부모 클래스)
# 추상 클래스: ABC를 상속받아 추상 베이스 클래스로 정의되었습니다.

# 초기화: __init__에서 usage_data를 받아 내부 변수 _usage_data에 복사본으로 저장합니다.

# 캡슐화:
# @property와 @ usage_data.setter를 사용하여 usage_data에 대한 getter와 setter를 구현했습니다. getter는 리스트 복사본을 반환하여 내부 데이터를 보호합니다.
# total_usage는 속성으로 정의되어 calculate_total_usage를 호출하며, setter는 제공되지 않아 읽기 전용입니다.

# 추상 메서드:
# calculate_total_usage: 총 사용량 계산, 자식 클래스에서 구현.
# get_usage_on_date: 특정 날짜 사용량 조회, 자식 클래스에서 구현.

# 구체 메서드:
# add_usage: 새로운 사용 데이터를 리스트에 추가.
# remove_usage: 지정된 날짜의 데이터를 리스트에서 제거.

# HomeElectricityData 클래스(자식 클래스)
# 상속: ElectricityData를 상속받아 부모 클래스의 기능을 확장합니다.
# 추상 메서드 구현:
# calculate_total_usage: _usage_data 리스트의 "usage" 값을 모두 합산하여 반환.
# get_usage_on_date: 지정된 날짜를 찾아 사용량을 반환하며, 없으면 ValueError 발생.

# 클래스 메서드:
# filter_by_date_range: 주어진 usage_data 리스트에서 시작 날짜와 종료 날짜 사이의 데이터를 필터링하여 반환. 날짜는 "YYYY-MM-DD" 형식으로 문자열 비교 가능.

# 정적 메서드:
# find_highest_usage: usage_data에서 최대 사용량을 찾아 반환. 데이터가 없으면 ValueError 발생.

# 추가 요구사항 충족
# 데이터 추가/삭제: add_usage와 remove_usage로 구현.
# 총 사용량 계산 및 날짜별 조회: total_usage 속성과 get_usage_on_date로 구현.
# 예외 처리: find_highest_usage에서 빈 리스트에 대한 예외 처리 포함.
# 날짜 범위 필터링: filter_by_date_range로 구현.

from abc import ABC, abstractmethod

# 부모 클래스: ElectricityData


class ElectricityData(ABC):
    def __init__(self, usage_data, total_usage=0):
        """사용 데이터를 초기화합니다. 입력된 리스트를 복사하여 내부 상태를 보호합니다."""
        self._usage_data = usage_data.copy()
        self._total_usage = total_usage

    @property
    def usage_data(self):
        """usage_data의 getter로, 데이터 리스트의 복사본을 반환하여 캡슐화를 유지합니다."""
        return self._usage_data.copy()

    @usage_data.setter
    def usage_data(self, value):
        """usage_data의 setter로, 입력된 리스트를 복사하여 설정합니다."""
        self._usage_data = value.copy()

    @property
    def total_usage(self):
        """total_usage를 계산하여 반환하는 속성입니다."""
        return self.calculate_total_usage()

    # 추상 메서드

    @abstractmethod
    # 총 사용량을 계산하는 추상 메서드입니다. 자식 클래스에서 구현해야 합니다.
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):  # """특정 날짜의 사용량을 조회하는 추상 메서드입니다. 자식 클래스에서 구현해야 합니다."""
        pass

    def add_usage(self, date, usage):  # 새로운 사용 데이터를 추가합니다.

        self._usage_data.append({"date": date, "usage": usage})

    def remove_usage(self, date):  # 지정된 날짜의 사용 데이터를 삭제합니다.

        self._usage_data = [
            data for data in self._usage_data if data["date"] != date]

# 자식 클래스: HomeElectricityData


class HomeElectricityData(ElectricityData):
    # 추상메서드 구현
    def calculate_total_usage(self):  # 총 전력 사용량을 계산합니다. 사용량의 합계를 반환합니다.
        return sum(data["usage"] for data in self._usage_data)

    def get_usage_on_date(self, date):  # 특정 날짜의 사용량을 조회합니다. 없으면 예외를 발생시킵니다.
        for data in self._usage_data:
            if data["date"] == date:
                return data["usage"]

        raise ValueError(f"{date}에 대한 데이터가 없습니다.")

    # 클래스 메서드
    @classmethod
    # 특정 날짜 범위 내의 데이터를 필터링하여 반환합니다.
    def filter_by_date_range(cls, usage_data, start_date, end_date):
        return [data for data in usage_data if start_date <= data["date"] <= end_date]

    # 정적 메서드
    @staticmethod
    # 데이터에서 가장 높은 사용량과 그 날짜를 찾아 반환합니다. 데이터가 없으면 예외를 발생시킵니다.
    def find_highest_usage(usage_data):
        if not usage_data:
            raise ValueError("데이터가 없습니다.")
        highest_usage_data = max(usage_data, key=lambda x: x["usage"])
        return {
            "date": highest_usage_data["date"],
            "usage": highest_usage_data["usage"]
        }


# 테스트 코드
if __name__ == "__main__":
    # 샘플 데이터 초기화
    electricity_usage = [
        {"date": "2024-11-01", "usage": 12.5},
        {"date": "2024-11-02", "usage": 15.3},
        {"date": "2024-11-03", "usage": 10.8},
        {"date": "2024-11-04", "usage": 14.2},
        {"date": "2024-11-05", "usage": 13.6}
    ]

    # HomeElectricityData 인스턴스 생성
    home_data = HomeElectricityData(electricity_usage)

    # 총 사용량 출력
    print(f"총 사용량: {home_data.total_usage}")  # 66.4

    # 특정 날짜 사용량 조회
    # 10.8
    print(f"2024-11-03 사용량: {home_data.get_usage_on_date('2024-11-03')}")

    # 데이터 추가
    home_data.add_usage("2024-11-06", 11.0)
    print(f"데이터 추가 후 총 사용량: {home_data.total_usage}")  # 77.4

    # 데이터 삭제
    home_data.remove_usage("2024-11-02")
    print(f"데이터 삭제 후 총 사용량: {home_data.total_usage}")  # 62.1

    # 날짜 범위 필터링
    filtered_data = HomeElectricityData.filter_by_date_range(
        home_data.usage_data, "2024-11-03", "2024-11-05"
    )
    print("2024-11-03 ~ 2024-11-05 데이터:", filtered_data)

    # 가장 높은 사용량과 날짜 찾기
    highest = HomeElectricityData.find_highest_usage(home_data.usage_data)
    # 14.2 (날짜: 2024-11-04)
    print(f"가장 높은 사용량: {highest['usage']} (날짜: {highest['date']})")

    # 예외 처리 테스트
    try:
        HomeElectricityData.find_highest_usage([])
    except ValueError as e:
        print(f"예외 발생: {e}")


# 만드는 순서(위에서 부터)
# 1. 생성사 __into__
# 2. 캡슐화 (getter,setter)
# 3. 추상 메서드
