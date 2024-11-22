[백준 15829번 문제](https://www.acmicpc.net/problem/15829)

### 문제
해시함수 만들기

### 풀이

```
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int strNum = Integer.parseInt(br.readLine());
        
        String hashStr = br.readLine();
        long hash = 0;
        long powValue = (long)Math.pow(31, 0);
        int M = 1234567891;
        
        for(int i = 0; i < strNum; i++) {
        	int idx = hashStr.charAt(i) - 'a' + 1;
        	hash += idx * powValue % M;
        	powValue = (powValue * 31) % M;
        }
        
        hash %= M;
        
        bw.write(hash + "");
        
        bw.flush();
        bw.close();
        br.close();
    }
}
```

### 고민했던 사항
- 모듈러 연산의 분배법칙을 몰라서 고생함, 중간중간 mod 연산해주고 마지막에도 해줘야하는 특이한 법칙
- 특히, 거듭제곱의 연산의 경우엔 mod 연산을 한 수를 계속 거듭제곱해줘야 해서 더 생소했음
- (a+b) mod M = [(a mod M)+(b mod M)]mod M

