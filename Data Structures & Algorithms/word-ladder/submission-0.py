class Solution:
    def ladderLength(self, beginword: str, endword: str, wordlist: List[str]) -> int:
        if (endword not in wordlist) or (beginword == endword):
            return 0
        words = set(wordlist)
        level = 0
        q = deque([beginword])
        while q:
            level +=1
            for i in range(len(q)):
                node = q.popleft()
                if node == endword:
                    return level
                for i in range(len(node)):
                    for c in range(97,123):
                        if chr(c) == node[i]:
                            continue
                        nei = node[:i] + chr(c) + node[i+1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        return 0