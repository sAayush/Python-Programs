class MeetingRooms:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings = sorted(meetings, key=lambda x: x[0])
        rooms = [0] * n



if __name__ == "__main__":
    mr = MeetingRooms()
    print(mr.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))  # 0
