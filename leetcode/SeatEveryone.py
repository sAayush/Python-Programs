class SeatEveryone:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(seats[i] - students[i]) for i in range(len(seats)))
