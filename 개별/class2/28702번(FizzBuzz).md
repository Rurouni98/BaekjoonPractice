[백준 28702번 문제](https://www.acmicpc.net/problem/28702)

### 문제
연속된 3개의 숫자를 입력받고, 그 다음에 올 숫자가 3의 배수 / 5의 배수 / 3과 5의 배수 / 어느 쪽도 아님을 판단하는 문제

### 풀이

```
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException{
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {
        
        String[] input = new String[3];
        
        for(int i = 0; i < 3; i++) {
        	input[i] = br.readLine();
        }
        
        int num = 0;
        int idx = 0;
        for(String s : input) {
        	idx++;
        	if(!s.equals("Fizz") && !s.equals("Buzz") && !s.equals("FizzBuzz")) {
        		num = Integer.parseInt(s);
        		idx--;
        		break;
        	}
        }
        
        int result = num + (3 - idx);

        if(result % 3 == 0 && result % 5 == 0) {
        	bw.write("FizzBuzz");
        } else if(result % 3 == 0) {
        	bw.write("Fizz");
        } else if(result % 5 == 0) {
        	bw.write("Buzz");
        } else {
        	bw.write(result + "");
        }
        	
        bw.flush();
        
        }
    }
}
```

### 고민했던 사항
- 세 가지 숫자를 입력받을 때도 Fizz, Buzz 같은 느낌으로 입력받으니, 다음에 올 숫자를 어떻게 하면 확실하게 알 수 있을지 조금 고민함

