from abc import ABC, abstractmethod
electricity = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]


class ElectricityData(ABC):
    """날짜별 전력 사용량 데이터를 관리하는 추상 클래스"""

    def __init__(self, usage_data):
        """생성자: usage_data와 total_usage 초기화"""
        self._usage_data = usage_data  # 전력 사용량 데이터 리스트
        self._total_usage = self._calculate_total_usage()  # 총 사용량 계산

    @property
    def usage_data(self):
        """usage_data getter"""
        return self._usage_data

    @usage_data.setter
    def usage_data(self, usage_data):
        """usage_data setter"""
        self._usage_data = usage_data
        self._total_usage = self._calculate_total_usage()  # 데이터 변경 시 총 사용량 재계산

    @property
    def total_usage(self):
        """total_usage getter"""
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """total_usage setter"""
        self._total_usage = total_usage

    @abstractmethod
    def _calculate_total_usage(self):
        """총 사용량 계산 (내부 메서드)"""
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        """특정 날짜의 사용량 반환"""
        pass

    def add_usage(self, date, usage):
        """새로운 날짜의 사용량 추가"""
        self._usage_data.append({"date": date, "usage": usage})
        self._total_usage = self._calculate_total_usage()  # 총 사용량 재계산

    def remove_usage(self, date):
        """특정 날짜의 사용량 데이터 삭제"""
        self._usage_data = [
            data for data in self._usage_data if data["date"] != date]
        self._total_usage = self._calculate_total_usage()  # 총 사용량 재계산


class HomeElectricityData(ElectricityData):
    """가정용 전력 사용량 데이터 클래스"""

    def _calculate_total_usage(self):
        """총 사용량 계산 (구현)"""
        return sum(data["usage"] for data in self._usage_data)

    def get_usage_on_date(self, date):
        """특정 날짜의 사용량 반환 (구현)"""
        for data in self._usage_data:
            if data["date"] == date:
                return data["usage"]
        return None  # 해당 날짜 데이터가 없는 경우 None 반환


# 예시 데이터
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6},
]

# 객체 생성 및 사용
home_data = HomeElectricityData(electricity_usage)

print(f"총 사용량: {home_data.total_usage}")
print(f"2024-11-03 사용량: {home_data.get_usage_on_date('2024-11-03')}")

home_data.add_usage("2024-11-06", 16.0)
print(f"총 사용량 (추가 후): {home_data.total_usage}")

home_data.remove_usage("2024-11-01")
print(f"총 사용량 (삭제 후): {home_data.total_usage}")
