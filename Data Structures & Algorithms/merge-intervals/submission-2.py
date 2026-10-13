class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []

        intervals_first = sorted(intervals)
        output.append(intervals_first[0])

        for start, end in intervals_first[1:]:
            back = output[-1]

            if start <= back[1]:
                output[-1][1] = max(back[1], end)

            else:
                output.append([start, end])

        return output
