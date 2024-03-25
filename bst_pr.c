#include<stdio.h>
#include<stdlib.h>

typedef struct treenode{
    int data;
    struct treenode *left;
    struct treenode *right;
}TreeNode,*Tree;

Tree create(int data){
    Tree new = (Tree)malloc(sizeof(TreeNode));
    new->data = data;
    new->left = NULL;
    new->right = NULL;
    return new;
}
Tree insert(Tree node,int data){
    if(node == NULL){
        return create(data);
    }
    if(data<node->data){
        node->left = insert(node->left,data);
    }
    if(data>node->data){
        node->right = insert(node->right,data);
    }
    return node;
}
Tree search(Tree root,int target){
    if(root == NULL || root->data == target){
        return root;
    }
    if(target>root->data){
       return search(root->right,target);
    }
    
       return search(root->left,target);
    
}
Tree Delete(Tree root){
    if(root == NULL){
        return NULL;
    }
    
}
int main(){
    Tree root = NULL;
    root = insert(root,50);
    insert(root,30);
    insert(root,40);
    insert(root,70);
    insert(root,60);
    insert(root,20);
    return 0;
}
