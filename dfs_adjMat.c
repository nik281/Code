#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

// Function to perform DFS traversal
void dfs(int adj_matrix[MAX_VERTICES][MAX_VERTICES], int num_vertices, int visited[MAX_VERTICES], int vertex) {
    printf("%d ", vertex); // Print the current vertex
    visited[vertex] = 1; // Mark the current vertex as visited

    // Visit all adjacent vertices of the current vertex
    for (int i = 0; i < num_vertices; i++) {
        if (adj_matrix[vertex][i] && !visited[i]) {
            dfs(adj_matrix, num_vertices, visited, i);
        }
    }
}

int main() {
    int num_vertices, num_edges;
    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &num_vertices, &num_edges);

    int adj_matrix[MAX_VERTICES][MAX_VERTICES] = {0};
    int visited[MAX_VERTICES] = {0};

    printf("Enter the edges (vertex1 vertex2):\n");
    for (int i = 0; i < num_edges; i++) {
        int vertex1, vertex2;
        scanf("%d %d", &vertex1, &vertex2);
        // Assuming input vertices are 0-indexed
        adj_matrix[vertex1][vertex2] = 1;
        adj_matrix[vertex2][vertex1] = 1; // Since the graph is undirected
    }

    int start_vertex;
    printf("Enter the starting vertex: ");
    scanf("%d", &start_vertex);

    printf("DFS traversal starting from vertex %d: ", start_vertex);
    dfs(adj_matrix, num_vertices, visited, start_vertex);

    return 0;
}