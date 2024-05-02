#include <stdio.h>
void read(int arr[],int n);
void display(int arr[],int n);
void change_last(int arr[],int n);
void main(){
    // int n;
    // scanf("%d",&n);
    int a[20]={1,2,3};
    printf(" a is %d and &a is %d and &a[0] is %d",a,&a,&a[0]);
    // read(a,n);
    // display(a,n);
    // change_last(a,n);
    // printf("\n at last displayin\n");
    // display(a,n);
}
void read(int arr[],int n){
    for (int i=0;i<n;i++){
        printf("\n arry[%d]=",i);
        scanf("%d",&arr[i]);
    }
}
void display(int arr[],int n){
    for(int i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
}
void change_last(int arr[],int n){
    arr[n-1]=99;
}