class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals_first = sorted(intervals)
        
        holder = [intervals_first[0]]

        for s, e in intervals_first[1:]:
            lastend = holder[-1][1]

            if s <= lastend:
                holder[-1][1] = max(lastend, e)

            else:
                holder.append([s, e])
            
        return holder




        


        