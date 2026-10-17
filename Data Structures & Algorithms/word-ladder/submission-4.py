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

        q = deque([beginWord])
        visited = set([beginWord])
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for w in range(len(word)):
                    pattern = word[:w] + "*" + word[w+1:]
                    for newWord in holder[pattern]:
                        if newWord not in visited:
                            q.append(newWord)
                            visited.add(newWord)
            count += 1
        return 0

                
                
        