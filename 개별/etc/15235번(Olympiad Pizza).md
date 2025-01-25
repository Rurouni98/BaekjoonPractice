[백준 15235번 문제](https://www.acmicpc.net/problem/15235)

### 문제
주어진 수 N에 대해 특정 규칙으로 수를 변환하며 처음 수로 돌아올 때까지의 반복 횟수(사이클 길이)를 구하는 문제

### 풀이

```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            int num = Integer.parseInt(br.readLine()); // 참가자 수
            Queue<int[]> intQue = new LinkedList<>(); // [필요한 피자 조각 수, 인덱스]를 저장할 큐
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < num; i++) {
                int needed = Integer.parseInt(st.nextToken());
                intQue.add(new int[]{needed, i}); // 필요한 피자 수와 참가자 인덱스를 저장
            }

            int cnt = 0; // 현재 시간
            int[] result = new int[num]; // 결과 배열 (각 참가자가 피자를 다 받은 시간 저장)

            while (!intQue.isEmpty()) {
                cnt++; // 시간 증가
                int[] current = intQue.poll(); // 큐에서 현재 참가자 가져오기
                current[0]--; // 피자 1조각 배분

                if (current[0] <= 0) {
                    // 필요한 피자를 다 받았으면 결과 저장
                    result[current[1]] = cnt;
                } else {
                    // 아직 필요량이 남았다면 다시 큐에 추가
                    intQue.add(current);
                }
            }

            // 결과 출력 (공백으로 구분)
            for (int time : result) {
                System.out.print(time + " ");
            }
        }
    }
}
```

### 고민했던 사항
- 
