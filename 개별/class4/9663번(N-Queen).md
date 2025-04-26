[백준 9663번 문제](https://www.acmicpc.net/problem/9663)

### 문제
N×N 체스판에 N개의 퀸을 서로 공격하지 않게 배치하는 모든 경우의 수를 구하는 백트래킹 문제

### 풀이
```
import java.io.*;

public class Main {
    static boolean[] col;     // 각 열에 퀸이 있는지
    static boolean[] diag1;   // ↙ 대각선 (x + y)
    static boolean[] diag2;   // ↘ 대각선 (x - y + N - 1)
    static int queenCnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 체스판 크기 (N x N)

        // 배열 크기 설정
        col = new boolean[N];              // 열: 0 ~ N-1
        diag1 = new boolean[2 * N - 1];    // ↙ 대각선: x + y → 0 ~ 2N-2
        diag2 = new boolean[2 * N - 1];    // ↘ 대각선: x - y + (N - 1) → 0 ~ 2N-2

        dfs(0, N);  // 0번째 행부터 시작

        System.out.println(queenCnt);
    }

    /**
     * 현재 row 번째 행에 퀸을 놓는 경우의 수를 탐색
     */
    static void dfs(int row, int N) {
        // 퀸을 N개 모두 놓은 경우
        if (row == N) {
            queenCnt++;
            return;
        }

        // 현재 행(row)에 열(col)을 바꿔가며 퀸을 놓을 수 있는지 확인
        for (int colIdx = 0; colIdx < N; colIdx++) {
            // 해당 열과 대각선에 퀸이 없으면 놓기 가능
            if (!col[colIdx] && !diag1[row + colIdx] && !diag2[row - colIdx + N - 1]) {
                // 상태 표시 (퀸 배치)
                col[colIdx] = true;
                diag1[row + colIdx] = true;
                diag2[row - colIdx + N - 1] = true;

                // 다음 행으로 진행
                dfs(row + 1, N);

                // 상태 복원 (백트래킹)
                col[colIdx] = false;
                diag1[row + colIdx] = false;
                diag2[row - colIdx + N - 1] = false;
            }
        }
    }
}
```

### 고민했던 사항
- 대각선 정보를 어떤 식으로 배열에 저장해야할지 고민함
- 백트래킹을 할 때 depth를 따로 변수에 저장했는데, y(row) 자체가 depth를 의미하므로 통일했음
- 재귀에 대해서 아직도 조금 덜 익숙해서 조금 더 문제를 풀어볼 필요성을 느낌