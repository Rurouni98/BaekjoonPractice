[백준 17626번 문제](https://www.acmicpc.net/problem/17626)

### 문제
주어진 자연수 n을 최소 개수의 제곱수들의 합으로 표현하는 방법을 구하는 문제

### 풀이

```
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
   public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {
           
           // 사용자로부터 자연수 n 입력 받기
           int n = Integer.parseInt(br.readLine());
           
           // dp 배열 선언 및 초기화: dp[i]는 i를 제곱수의 합으로 나타낼 때 최소 개수
           int[] dp = new int[n + 1];
           
           // 모든 값을 5로 초기화 (최대 4개의 제곱수로 표현 가능하므로 5는 충분히 큰 값)
           Arrays.fill(dp, 5);
           
           // 0은 제곱수의 합이 0개이므로 0으로 초기화
           dp[0] = 0;

           // 1부터 n까지의 모든 수에 대해 최소 제곱수 개수 계산
           for (int i = 1; i <= n; i++) {
               // j는 제곱수 (1, 4, 9, 16, ...) 를 의미
               for (int j = 1; j * j <= i; j++) {
                   // i에서 j의 제곱을 뺀 값(dp[i - j*j])에 1(현재 제곱수 추가)을 더해 최소값 갱신
                   dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
               }
           }

           // 결과 출력: n을 제곱수의 합으로 표현할 때 최소 개수
           bw.write(dp[n] + "\n");
           bw.flush();
        }
   }
}
```

### 고민했던 사항
- 점화식을 구하는 데 고민을 많이 함

