 #include <iostream>
 #include <cmath>

using namespace std;

int main()
{
    float input;
    char quit;
    const float DOTTIE = .74;

    cout << "Enter integer: ";
    cin >> input;
    cout << endl;

    while(input > DOTTIE) {
        cout << cos(input) << endl;
    }

    return 0;
}