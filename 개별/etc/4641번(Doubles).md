[백준 4641번 문제](https://www.acmicpc.net/problem/4641)

### 문제
2~15개의 서로 다른 자연수로 이루어진 리스트가 있을 때, 이들 중 리스트 안에 자신의 정확히 2배인 수가 있는 수의 개수를 구하는 문제

### 풀이

```
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {
        	
            while(true) {
            	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            	
            	int input = Integer.parseInt(st.nextToken());
            	
            	if(input == -1) {
            		break;
            	}
            	
            	List<Integer> intList = new ArrayList<>();
            	intList.add(input);
            	
            	while(st.hasMoreTokens()) {
            		int token = Integer.parseInt(st.nextToken());
            		
            		if(token == 0) {
            			break;
            		}
            		
            		intList.add(token);
            	}
            	
            	int cnt = 0;
            	for(int i = 0; i < intList.size() - 1; i++) {
            		for(int j = i + 1; j < intList.size(); j++) {
            			double front = (double)intList.get(i);
            			double back = (double)intList.get(j);
            			
            			if(front / back == 2.0) {
            				cnt++;
            			} else if(back / front == 2.0) {
            				cnt++;
            			}
            		}
            	}
            	
            	bw.write(cnt + "\n");
            }
            
            bw.flush();
        }
    }
}
```


### 고민했던 사항

