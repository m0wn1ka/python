#include <stdio.h>
#include <stdlib.h>
struct node {
    int x;
    struct node *left;
    struct node *right;

};

void preorder(struct node *ptr){
    if(ptr!=NULL){
        printf("%d\t",ptr->x);
        preorder(ptr->left);
        preorder(ptr->right);
    }
}
void inorder(struct node *ptr){
    if(ptr!=NULL){
        inorder(ptr->left);
        printf("%d\t",ptr->x);
        
        inorder(ptr->right);
    }
}
void create(struct node *ptr){
    ptr->left=NULL;
    ptr->right=NULL;
}
struct node * insert(struct node *ptr,int x){
    struct node *reference=ptr;
    struct node *new_node=(struct node *)malloc(sizeof(struct node));
    new_node->x=x;
    new_node->left=NULL;
    new_node->right=NULL;

    if(ptr==NULL){
        ptr=new_node;
        return ptr;
    }
    else{
        struct node *parent=NULL;
        while (ptr!=NULL)
        {parent=ptr;
            if(ptr->x>x){
                ptr=ptr->left;
            }
            else{
                ptr=ptr->right;
            }
        }
        if(parent->x>x){
            parent->left=new_node;
        }
        else{
            parent->right=new_node;
        }
        return reference;
        
    }
}
struct node *delete (struct node *ptr,int x){
    if(ptr==NULL){
        printf("\ncant find element %d",x);
    }
    sss
    struct node *parent=ptr;
    while(ptr!=NULL){
        parent=ptr;
        if(ptr->x>x){
            ptr=ptr->left;
        }
        else if(ptr->x<x){
            ptr=ptr->right;
        }
        else{
            break;
        }
    }
    if(ptr->left==NULL && ptr->right==NULL){
        parent->left=NULL;
        parent->right=NULL;

    }

}
int main(){
    struct node *tree=(struct node *)malloc(sizeof(struct node));
    
    create(tree);
    tree=insert(tree,22);
    
    tree=insert(tree,33);
    tree=insert(tree,11);
    preorder(tree);
    printf("\n in order is\n");
    inorder(tree);
    return 0;
}
