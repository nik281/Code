#include<stdio.h>
#include<stdlib.h>

typedef struct treenode{
    int data;
    struct treenode *left;
    struct treenode *right;
} TreeNode, *TREE;

TREE createnode(int data)
{
    TREE newnode = (TREE)malloc(sizeof(TreeNode));
    newnode->data = data;
    newnode->left = NULL;
    newnode->right = NULL;
    return newnode;
}

TREE insert(TREE node, int data)
{
    if(node==NULL)
    {
        return createnode(data);
    }
    
    if(data < node->data)
    {
        node->left = insert(node->left, data);
    }
    else if(data > node->data)
    {
        node->right = insert(node->right, data);
    }
    
    return node;
}

void inordertraversal(TREE node)
{
    if(node!=NULL)
    {
        inordertraversal(node->left);
        printf("%d", node->data);
        inordertraversal(node->right);
    }
}
int main()
{
    TREE root = NULL;
    root = insert(root, 10);
    insert(root, 5);
    insert(root, 15);
    insert(root, 7);
    insert(root, 3);
    
    printf("Inorder traversal: ");
    inordertraversal(root);
    printf("\n");
    return 0;
}