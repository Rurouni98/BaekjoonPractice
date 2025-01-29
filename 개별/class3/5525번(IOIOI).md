[백준 5525번 문제](https://www.acmicpc.net/problem/5525)

### 문제
주어진 문자열에 특정 패턴이 몇 개나 포함되어있는지 출력하는 문제

### 풀이
```
package test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            
            int num = Integer.parseInt(br.readLine());
            int parentSize = Integer.parseInt(br.readLine());
            String parent = br.readLine();

            // 패턴 생성 (IOI 형태)
            StringBuilder patternBuilder = new StringBuilder("I");
            for (int i = 0; i < num; i++) {
                patternBuilder.append("OI");
            }
            String pattern = patternBuilder.toString();

            int[] table = makeTable(pattern);
            int patternSize = pattern.length();
            int j = 0;
            int cnt = 0;

            // KMP 문자열 매칭
            for (int i = 0; i < parentSize; i++) {
                while (j > 0 && parent.charAt(i) != pattern.charAt(j)) {
                    j = table[j - 1];
                }
                if (parent.charAt(i) == pattern.charAt(j)) {
                    if (j == patternSize - 1) { // 패턴 매칭 성공
                        cnt++;
                        j = table[j]; // j 위치 업데이트
                    } else {
                        j++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }

    // KMP 부분 일치 테이블 (LPS Table) 생성
    static int[] makeTable(String pattern) {
        int patternSize = pattern.length();
        int[] table = new int[patternSize];
        int j = 0;

        for (int i = 1; i < patternSize; i++) { // i는 1부터 시작해야 함
            while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) {
                j = table[j - 1];
            }
            if (pattern.charAt(i) == pattern.charAt(j)) {
                table[i] = ++j;
            }
        }
        return table;
    }
}
```

### 고민했던 사항
- KMP 알고리즘을 사용하면 되겠다고 생각은 했으나, 저번에 제대로 이해하지 못해서 이번 기회에 이해하는 겸 쭉 보느라 꽤 힘들었음
- 부분 일치 테이블(LPS Table)을 생성하는 이유나, i와 j의 갱신 방식에 대해 많이 헷갈려서 어려웠음

