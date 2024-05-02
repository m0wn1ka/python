#include <stdio.h>
#include <stdlib.h>

struct node {
    int x;
    struct node *left;
    struct node *right;
};

void inorder(struct node *ptr){
    if(ptr != NULL){
        printf("%d\t", ptr->x);
        inorder(ptr->left);
        inorder(ptr->right);
    }
}

void create(struct node *ptr){
    ptr->left = NULL;
    ptr->right = NULL;
}

int main(){
    struct node *tree = (struct node *)malloc(sizeof(struct node));
   
    create(tree);
    
   
    return 0;
}
