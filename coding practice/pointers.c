#include <stdio.h>
void swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void main(){
    int a=1,b=2;
    swap(&a,&b);
    printf("after swap a =%d and b=%d",a,b);

}