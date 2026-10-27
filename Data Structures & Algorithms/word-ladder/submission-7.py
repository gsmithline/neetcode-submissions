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
        kept = set()

        count = 1

        while que:
            for i in range(len(que)):
                word = que.popleft()

                if word == endWord:
                    return count
                for w in range(len(word)):
                    pattern = word[:w] + "*" + word[w+1:] 
                    words = holder[pattern]
                    for o in words:
                        if o not in kept:
                            kept.add(o)
                            que.append(o)
            count += 1
        return 0
                            
                 
                
            
                
        
        