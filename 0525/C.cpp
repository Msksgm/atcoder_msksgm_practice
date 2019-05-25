#include <iostream>
#include <string>
using namespace std;

int main() {
    int N, M, i, j;
    cin >> M;
    int box[M];

    for (i = 0; i<M; i=i+1){
        cin >> j;
        box[i] = j;
    }

    cout << sizeof(box) << "\n";

    // for (i = 0; i<sizeof(box); i=i+1){
    //     cout << box[i];
    // }

}
