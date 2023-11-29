# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list = []
        z = ZigZagRow(numRows)
        for e in s:
            list.append((z.step(), e))
        print(list)
        list = sorted(list, key=lambda a: a[0])

        list_zigzagged = [e[1] for e in list]
        print(list_zigzagged)
        return "".join(list_zigzagged)


class ZigZagRow:
    def __init__(self, size, going_down=None):
        self.going_down = going_down
        self.size = size
        self.row = 0

    def step(self):
        if self.going_down == None:
            self.going_down = False
            return 0
        return self._step()

    def __repr__(self):
        return f"ZigZagRow(going_down={self.going_down},row={self.row})"

    def _step(self):
        if (self.row == self.size - 1) or (self.row == 0):
            self.going_down = not self.going_down

        self.row += 1 if self.going_down else -1
        return self.row


s = Solution()
print(s.convert("PAYPALISHIRING", 3))

z = ZigZagRow(4)
