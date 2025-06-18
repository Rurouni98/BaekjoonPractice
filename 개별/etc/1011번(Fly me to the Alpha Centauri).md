[백준 1011번 문제](https://www.acmicpc.net/problem/1011)

### 문제
x지점에서 y지점까지, 마지막 이동을 1광년으로 하면서 최소 횟수로 도달하는 문제
(단, 이동거리는 이전 이동거리의 -1, 0, +1만 가능함)

### 풀이

```
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int num = Integer.parseInt(br.readLine());  // 테스트 케이스 개수 입력
        int[][] xy = new int[num][2];  // 각 케이스마다 시작점과 도착점 저장할 배열
        
        // 각 테스트 케이스에 대해 입력 받기
        for(int i = 0; i < num; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            xy[i][0] = Integer.parseInt(st.nextToken());  // x
            xy[i][1] = Integer.parseInt(st.nextToken());  // y
        }
        
        int[] results = new int[num];  // 결과 저장용 배열
        
        for(int i = 0; i < num; i++) {
            int start = xy[i][0];
            int target = xy[i][1];
            double dist = target - start;  // 전체 이동 거리 계산
            
            int n = (int)Math.sqrt(dist);  // n을 √거리로 설정
            
            // 세 가지 조건으로 최소 작동 횟수 판단
            if(dist > n * (n + 1)) {
                results[i] = 2 * n + 1;
            } else if(dist > (n * n) && dist <= n * (n + 1)) {
                results[i] = 2 * n;
            } else {
                results[i] = 2 * n - 1;
            }
        }
        
        // 결과 출력
        for(int i : results) {
            System.out.println(i);
        }
        
        br.close();
    }
}
```

### 고민했던 사항
- 문제에서 "마지막 이동은 무조건 1광년"이라는 조건이 반영된 공식을 찾기 어려웠음
- Math.sqrt(dist)를 기준으로 패턴이 나뉜다는 부분을 찾느라 살짝 헤맴
