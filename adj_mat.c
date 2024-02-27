#include<stdio.h>
#include<stdlib.h>

typedef struct{
    int numVertices;
    int **adjmatrix;
}*Graph;
Graph createGraph(int vertices){
    Graph graph = (Graph) malloc(sizeof(Graph));
    graph->numVertices = vertices;
    graph->adjmatrix = malloc(vertices * sizeof(int *));
    for(int i=0;i<vertices;i++){
        graph->adjmatrix[i] = malloc(vertices * sizeof(int));
        for(int j = 0;j<vertices;j++){
            graph->adjmatrix[i][j] = 0;
        }
    }
    return graph;
}
void addEdge(Graph graph,int src,int dst){
    graph->adjmatrix[src][dst] = 1;
    graph->adjmatrix[dst][src] = 1;
}
void printGraph(Graph graph){
    for(int i=0;i<graph->numVertices;i++){
        for(int j=0;j<graph->numVertices;j++){
            printf("%d",graph->adjmatrix[i][j]);
        }
        printf("\n");
    }
}
void freeGraph(Graph graph){
    for(int i=0;i<graph->numVertices;i++){
        free(graph->adjmatrix[i]);
    }
    free(graph->adjmatrix);
    free(graph);
}
int main(){
    int numVertices = 4;
    Graph graph = createGraph(numVertices);
    addEdge(graph,2,3);
    printGraph(graph);
    freeGraph(graph);
    return 0;
}

