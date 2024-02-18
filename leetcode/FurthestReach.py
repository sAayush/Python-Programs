import heapq
class FurthestReachLadderBricks:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        # # Using a heap
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
                # print(heap, bricks, ladders)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
                # print(heap, bricks, ladders)
            if bricks < 0:
                return i
        return len(heights) - 1


if __name__ == "__main__":
    frlb = FurthestReachLadderBricks()
    print(frlb.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))  # 4
