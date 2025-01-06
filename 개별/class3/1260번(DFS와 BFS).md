[백준 1260번 문제](https://www.acmicpc.net/problem/1260)

### 문제
그래프를 DFS와 BFS로 탐색한 결과를 출력하며, 여러 정점을 방문할 수 있을 경우 번호가 작은 정점부터 우선 탐색하는 문제

### 풀이

```
import java.io.*;
import java.util.*;

public class Main {
    static List<List<Integer>> graph; // 그래프의 인접 리스트 표현
    static boolean[] connected; // 방문 여부를 체크하는 배열

    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {
            
            // 입력 처리
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int node = Integer.parseInt(st.nextToken()); // 정점의 개수
            int edge = Integer.parseInt(st.nextToken()); // 간선의 개수
            int startNode = Integer.parseInt(st.nextToken()); // 탐색 시작 정점
            
            // 그래프 초기화
            graph = new ArrayList<>();
            connected = new boolean[node + 1]; // 1번부터 시작하므로 +1
            for (int i = 0; i <= node; i++) {
                graph.add(new ArrayList<>()); // 각 정점을 리스트로 초기화
            }
            
            // 간선 정보 입력
            for (int i = 0; i < edge; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                graph.get(start).add(end);
                graph.get(end).add(start); // 양방향 간선 추가
            }
            
            // 각 정점의 연결 리스트를 정렬 (번호가 작은 정점부터 방문하도록 설정)
            for (int i = 0; i <= node; i++) {
                Collections.sort(graph.get(i));
            }
            
            // DFS 탐색
            dfs(startNode, bw);
            bw.write("\n");
            
            // BFS 탐색
            Arrays.fill(connected, false); // 방문 배열 초기화
            bfs(startNode, bw);
            
            bw.flush();
        }
    }

    // DFS 구현 (재귀 사용)
    static void dfs(int startNode, BufferedWriter bw) throws IOException {
        connected[startNode] = true; // 현재 노드 방문 처리
        bw.write(startNode + " "); // 방문한 노드 출력
        
        // 현재 노드와 연결된 모든 노드를 탐색
        for (int nextNode : graph.get(startNode)) {
            if (!connected[nextNode]) { // 방문하지 않은 경우
                dfs(nextNode, bw); // 재귀 호출
            }
        }
    }

    // BFS 구현 (큐 사용)
    static void bfs(int startNode, BufferedWriter bw) throws IOException {
        Queue<Integer> queue = new LinkedList<>(); // BFS 탐색을 위한 큐
        queue.add(startNode); // 시작 노드를 큐에 추가
        connected[startNode] = true; // 시작 노드 방문 처리
        bw.write(startNode + " "); // 방문한 노드 출력
        
        // 큐가 빌 때까지 반복
        while (!queue.isEmpty()) {
            int node = queue.poll(); // 큐에서 현재 노드 꺼내기
            for (int nextNode : graph.get(node)) { // 현재 노드와 연결된 모든 노드 탐색
                if (!connected[nextNode]) { // 방문하지 않은 경우
                    queue.add(nextNode); // 큐에 추가
                    bw.write(nextNode + " "); // 방문한 노드 출력
                    connected[nextNode] = true; // 방문 처리
                }
            }
        }
    }
}
```

### gpt가 개선해준 코드
```
import java.io.*;
import java.util.*;

public class Main {
    static List<List<Integer>> graph; // 그래프의 인접 리스트 표현
    static boolean[] visited; // 방문 여부 체크 배열

    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out))) {

            // 입력 처리
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int nodeCount = Integer.parseInt(st.nextToken());
            int edgeCount = Integer.parseInt(st.nextToken());
            int startNode = Integer.parseInt(st.nextToken());

            // 그래프 초기화
            graph = new ArrayList<>();
            visited = new boolean[nodeCount + 1];

            for (int i = 0; i <= nodeCount; i++) {
                graph.add(new ArrayList<>());
            }

            // 간선 입력
            for (int i = 0; i < edgeCount; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                graph.get(start).add(end);
                graph.get(end).add(start);
            }

            // 그래프 정렬 (연결된 정점 번호가 작은 순서로 방문하기 위해)
            for (List<Integer> adjacencyList : graph) {
                if (!adjacencyList.isEmpty()) {
                    Collections.sort(adjacencyList);
                }
            }

            // DFS 탐색
            dfs(startNode, bw);
            bw.write("\n");

            // BFS 탐색
            resetVisited(); // 방문 배열 초기화
            bfs(startNode, bw);

            bw.flush();
        }
    }

    // DFS 구현 (재귀 사용)
    static void dfs(int currentNode, BufferedWriter bw) throws IOException {
        visited[currentNode] = true;
        bw.write(currentNode + " ");

        for (int nextNode : graph.get(currentNode)) {
            if (!visited[nextNode]) {
                dfs(nextNode, bw);
            }
        }
    }

    // BFS 구현 (큐 사용)
    static void bfs(int startNode, BufferedWriter bw) throws IOException {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(startNode);
        visited[startNode] = true;

        while (!queue.isEmpty()) {
            int currentNode = queue.poll();
            bw.write(currentNode + " ");

            for (int nextNode : graph.get(currentNode)) {
                if (!visited[nextNode]) {
                    queue.add(nextNode);
                    visited[nextNode] = true;
                }
            }
        }
    }

    // 방문 배열 초기화 메서드
    static void resetVisited() {
        Arrays.fill(visited, false);
    }
}
```

### 고민했던 사항
- 저번에 DFS, BFS 관련 문제를 풀어봤기 때문에 그 문제를 많이 참고해서 풀어봄. DFS는 이제 익숙하지만 BFS는 아직 조금 헷갈림

