class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_first = sorted(intervals)

        output = [intervals_first[0]]

        for s, e in intervals_first[1:]:

            if s <= output[-1][1]:
                output[-1][1] = max(output[-1][1], e)
            else:
                output.append([s, e])
        
        return output

