class MeetingRooms:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        ans = [0] * n
        times = [0] * n

        for start, end in meetings:
            flag = False
            minimumIndex = -1
            val = float("inf")
            for i in range(n):
                if times[i] < val:
                    val = times[i]
                    minimumIndex = i
                if times[i] <= start:
                    flag = True
                    ans[i] += 1
                    times[i] = end
            if not flag:
                ans[minimumIndex] += 1
                times[minimumIndex] += (end - start)

        maxi = -1
        id = -1

        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i
        return id


if __name__ == "__main__":
    mr = MeetingRooms()
    print(mr.mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]]))  # 0
