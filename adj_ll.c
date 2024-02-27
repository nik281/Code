#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int vertex;
    struct node *next;
}*Node;

int numVertices;
Node **adjList;

Node createNode(int v){
    Node newNode = (Node)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

void initializeGraph(int vertices){
    numVertices = vertices;
    adjList = (Node)malloc(vertices * sizeof(Node));
    for(int i=0;i<vertices;i++){
        adjList[i] = NULL;
    }
}
void addEdge(int src,int dest){
    Node newNode = createNode(dest);
    newNode->next = adjList[src];
    adjList[src] = newNode;
    newNode = createNode(src);
    newNode->next = adjList[dest];
    adjList[dest] = newNode;
}
void printGraph(){
    for(int v = 0;v<numVertices;v++){
        Node temp = adjList[v];
        printf("Vertex %d:",v);
        while(temp){
            printf("-> %d",temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}
int main(){
    initializeGraph(5);
    addEdge(0,1);
    addEdge(0,4);
    addEdge(1,3);
    addEdge(1,4);
    addEdge(2,3);
    printGraph();
    return 0; 
}