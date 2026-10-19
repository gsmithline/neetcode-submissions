class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0
        holder = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for w in range(len(word)):
                pattern = word[:w] + "*" + word[w+1:]
                holder[pattern].append(word)
        

        que = deque([beginWord])
        visited = set([beginWord])
        result = 1

        while len(que) != 0:
            for i in range(len(que)):
                word = que.popleft()
                
                if word == endWord:
                    return result
                for w in range(len(word)):
                    pattern = word[:w] + "*" + word[w+1:]
                    for item in holder[pattern]:
                        if item not in visited:
                            que.append(item)
                            visited.add(item)

                
            result += 1
        return 0            

        
        