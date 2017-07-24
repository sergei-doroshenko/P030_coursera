package hackerRank.graph;

public class GraphTest {
    public static void main(String[] args) {
        Graph graph = new Graph();
        graph.addNode(1).addNode(2).addNode(3).addNode(4).addNode(5);
        graph.addEdge(1, 3).addEdge(3, 5).addEdge(1, 4);
        System.out.println(graph.hasPathDFS(1, 5));
        System.out.println(graph.hasPathBFS(1, 5));

        System.out.println(graph.hasPathDFS(1, 4));
        System.out.println(graph.hasPathBFS(1, 4));

        System.out.println(graph.hasPathDFS(3, 1));
        System.out.println(graph.hasPathBFS(3, 1));

        System.out.println(graph.hasPathDFS(3, 2));
        System.out.println(graph.hasPathBFS(5, 2));
    }
}
