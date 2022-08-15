/**
 * 59. 螺旋矩阵 II 左闭右开画法
 */
class Solution {
    public int[][] generateMatrix(int n) {
        int[][] matrix = new int[n][n];

        int startX = 0;
        int startY = 0;
        int loop = n / 2;
        int count = 1;
        int offset = 1;
        int x;
        int y;

        while (loop-- > 0) {
            // 填充上边
            for (x = startX; x < n - offset; x++) {
                matrix[startY][x] = count++;
            }
            // 填充右边
            for (y = startY; y < n - offset; y++) {
                matrix[y][x] = count++;
            }
            // 填充下边
            for (; x > startX; x--) {
                matrix[y][x] = count++;
            }
            // 填充左边
            for (; y > startY; y--) {
                matrix[y][x] = count++;
            }

            startX++;
            startY++;
            offset++;
        }

        if (n % 2 == 1) {
            int mid = n / 2;
            matrix[mid][mid] = count;
        }

        return matrix;
    }
}
