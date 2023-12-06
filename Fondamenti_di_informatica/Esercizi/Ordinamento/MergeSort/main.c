#include <stdio.h>

//prototipi delle funzioni
void merge(int v[], int l, int m, int r);
void mergesort(int v[], int l, int r);

int main(int argc, char const *argv[]) {
    
    return 0;
}

//definizione delle funzioni
void merge(int v[], int l, int m, int r) {
    
    int i, j, k;
    int* temp = malloc((r-l+1)*sizeof(int));
    
    i = l; 
    j = m+1; 
    k = 0;
    
    while (i <= m && j <= r) {
        if (v[i] < v[j]) {
            temp[k] = v[i];
            k++;
            i++;
        } else {
            temp[k] = v[i];
            k++;
            i++;
        }
    }
    
    if (i==m+1) {
        while (j <= r) {
            temp[k] = v[i];
            k++;
            i++;
        }
    } else {
        while (i <= m) {
            temp[k] = v[i];
            k++;
            i++;
        }
    }
    
    memcpy(&v[l], temp, (r-l+1)*sizeof(int));
    
    free(temp);
}

void mergesort(int v[], int l, int r) {
    int m;
    if (r <= l)
        return;
    
    m = (r+l)/2;
    
    mergesort(v, l, m);
    mergesort(v, m+1, r);
    merge(v, l, m, r);
}