#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 100

void dfs(int adj_matrix[MAX_VERTICES][MAX_VERTICES], int num_vertices, int visited[MAX_VERTICES], int vertex) {
    printf("%d ", vertex); 
    visited[vertex] = 1; 

    
    for (int i = 0; i < num_vertices; i++) {
        if (adj_matrix[vertex][i] && !visited[i]) {
            dfs(adj_matrix, num_vertices, visited, i);
        }
    }
}


void bfs(int adj_matrix[MAX_VERTICES][MAX_VERTICES], int num_vertices, int visited[MAX_VERTICES], int start_vertex) {
    int queue[MAX_VERTICES];
    int front = -1, rear = -1;

    printf("BFS traversal starting from vertex %d: ", start_vertex);
    printf("%d ", start_vertex);
    visited[start_vertex] = 1;
    queue[++rear] = start_vertex;

    while (front != rear) {
        int current_vertex = queue[++front];

        for (int i = 0; i < num_vertices; i++) {
            if (adj_matrix[current_vertex][i] && !visited[i]) {
                printf("%d ", i);
                visited[i] = 1;
                queue[++rear] = i;
            }
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
        
        adj_matrix[vertex1][vertex2] = 1;
        adj_matrix[vertex2][vertex1] = 1; 
    }

    int start_vertex;
    printf("Enter the starting vertex: ");
    scanf("%d", &start_vertex);

    int choice;
    printf("Choose traversal method:\n1. DFS\n2. BFS\nEnter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("DFS traversal starting from vertex %d: ", start_vertex);
            dfs(adj_matrix, num_vertices, visited, start_vertex);
            break;
        case 2:
            
            for (int i = 0; i < num_vertices; i++) {
                visited[i] = 0;
            }
            bfs(adj_matrix, num_vertices, visited, start_vertex);
            break;
        default:
            printf("Invalid choice\n");
    }

    return 0;
}
