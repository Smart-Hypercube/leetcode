def scorec(sticker, target):
    return {k: min(sticker[k], target[k]) for k in target if k in sticker}

def maked(s, cache={}):
    if s in cache:
        return dict(cache[s])
    d = {}
    for c in s:
        d.setdefault(c, 0)
        d[c] += 1
    cache[s] = d
    return dict(d)

class Solution:
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        target = maked(target)
        stickers = [maked(s) for s in stickers]
        scores = []
        for i in range(len(stickers)):
            s = stickers[i]
            score = scorec(s, target)
            scores.append((sum(score.values()), i, score, s))
        scores.sort(reverse=True)
        count = 0
        while target:
            count += 1
            sticker = scores[0][2]
            if not sticker:
                return -1
            changed = set()
            removed = set()
            for k in sticker:
                target[k] -= sticker[k]
                if target[k]:
                    changed.add(k)
                else:
                    del target[k]
                    removed.add(k)
            for i in range(len(scores)):
                s = scores[i]
                rebuild = False
                for c in changed:
                    if c in s[2]:
                        rebuild = True
                        break
                if rebuild:
                    score = scorec(s[3], target)
                    scores[i] = sum(score.values()), s[1], score, s[3]
                    continue
                recalc = False
                for r in removed:
                    if r in s[2]:
                        recalc = True
                        del s[2][r]
                if recalc:
                    scores[i] = sum(s[2].values()), s[1], s[2], s[3]
            scores.sort(reverse=True)
        return count
