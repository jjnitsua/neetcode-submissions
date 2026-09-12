class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:      
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        if target>matrix[-1][cols-1] or target<matrix[0][0]:
            return False

        lr=0
        rr=rows-1 
        while lr<=rr:
            m=(lr+rr)//2
            if matrix[m][0]>target:
                rr=m-1
            elif matrix[m][cols-1]<target:
                lr=m+1
            else :
                break
        lc=0
        rc=cols-1
        while lc<=rc:
            mc=(lc+rc)//2
            if matrix[m][mc]>target:
                rc=mc-1
            elif matrix[m][mc]<target:
                lc=mc+1
            else:
                return True

        return False