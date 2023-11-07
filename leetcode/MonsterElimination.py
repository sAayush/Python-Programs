class Monster:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        time = [dist[i] / speed[i] for i in range(len(dist))]
        time.sort()
        for i in range(len(time)):
            if time[i] <= i:
                return i
        return len(time)


if __name__ == '__main__':
    monster = Monster()
    distance = [1, 3, 4]
    speed = [1, 1, 1]
    print(monster.eliminateMaximum(distance, speed))