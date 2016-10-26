# https://leetcode.com/problems/valid-sudoku


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if c == '.':
                    continue

                g = math.floor(i / 3) * 3 + math.floor(j / 3)
                if c in d:
                    rows, cols, groups = d[c][0], d[c][1], d[c][2]
                    if i in rows or j in cols or g in groups:
                        return False
                    rows.append(i)
                    cols.append(j)
                    groups.append(g)
                else:
                    d[c] = [[i], [j], [g]]
        return True
