class TimeTickets:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        bigcount = 0
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                time += tickets[i]
            else:
                time += tickets[k]
                if i > k:
                    bigcount += 1

        return time - bigcount


if __name__ == '__main__':
    tt = TimeTickets()
    print(tt.timeRequiredToBuy([2, 3, 2], 2))
