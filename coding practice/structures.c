#include <stdio.h>
struct node{
    int x;
    int y;
};
void chagne(struct node n){
    int t=n.x;
    n.x=n.y;
    n.y=t;
}
void chagneref(struct node *n){
    int t=n->x;
    n->x=n->y;
    n->y=t;
}
void display(struct node n){
    printf("\n n.x is %d n.y is %d\n",n.x,n.y);
}
void display_ptr(struct node *ptr){
    printf("\n n.x is %d and n.y is %d",ptr->x,ptr->y);
}
void main(){
    struct node    n1= {11,22};
    struct node n2= {1,2};
    struct node * ptr1=&n1;
    struct node *ptr2=(struct node *)malloc(sizeof(struct node ));
    ptr2->x=111;
    ptr2->y=222;
    // display(n1);
    // chagneref(ptr1);
    // display(n1);
    display_ptr(ptr2);

}