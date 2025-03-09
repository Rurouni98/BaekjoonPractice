[백준 14753번 문제](https://www.acmicpc.net/problem/14753)

### 문제
주어진 n개의 정수 중 두 개 또는 세 개를 선택하여 만들 수 있는 최대 곱을 구하는 문제

### 풀이

```
package test;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int cardNum = Integer.parseInt(br.readLine());
        int[] cards = new int[cardNum];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < cardNum; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(cards);

        // 1. 가장 큰 두 개의 곱
        int maxTwo = Math.max(cards[0] * cards[1], cards[cardNum - 1] * cards[cardNum - 2]);

        // 2. 가장 큰 세 개의 곱 vs 가장 작은 두 개 * 가장 큰 수
        int maxThree = Math.max(cards[cardNum - 1] * cards[cardNum - 2] * cards[cardNum - 3], 
                                cards[0] * cards[1] * cards[cardNum - 1]);

        // 3. 두 개만 선택하는 경우도 비교해야 함
        int maxProduct = Math.max(maxTwo, maxThree);
        
        bw.write(maxProduct + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
```


### 고민했던 사항
- 생각보다 최대곱의 경우의 수가 많아서 당황함
