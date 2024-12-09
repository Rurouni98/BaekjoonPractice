[백준 18110번 문제](https://www.acmicpc.net/problem/18110)

### 문제
입력받은 난이도 점수의 절사평균 구하기
(양 끝단 15%씩 제외)

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

            // 입력받은 난이도 의견 개수
            int num = Integer.parseInt(br.readLine());

            // 의견이 없는 경우 난이도를 0으로 출력
            if (num == 0) {
                bw.write("0\n");
                bw.flush();
                return;
            }

            // 난이도 의견 배열 입력
            int[] intArr = new int[num];
            for (int i = 0; i < num; i++) {
                intArr[i] = Integer.parseInt(br.readLine());
            }

            // 난이도 의견 배열 정렬
            Arrays.sort(intArr);

            // 절사평균 계산에 사용할 범위 설정
            double arrLen = intArr.length;
            int start = (int) (Math.round(arrLen / 100 * 15)); // 아래 15% 제외
            int end = (int) (arrLen - start); // 위 15% 제외

            // 절사평균 범위 내 합계 계산
            int sum = 0;
            for (int i = start; i < end; i++) {
                sum += intArr[i];
            }

            // 평균 계산 (반올림)
            long avg = Math.round(sum / (double) (end - start));

            bw.write(avg + "\n");
            bw.flush();
        }
    }
}
```

### 고민했던 사항
- start, end 어느 지점인지 아주 조금 고민