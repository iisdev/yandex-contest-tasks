#include <iostream>
#include <algorithm>

long long max_el(long long* a, long beg, long en)
{
    long long max_v = 0;
    for (long i = beg; i < en; i++)
        if (a[i] > max_v)
            max_v = a[i];
    return max_v;
}


using namespace std;
int main() {
    long n, m;
    cin >> n;
    cin >> m;

    long long *layers = new long long[n];
    long long *warriors = new long long[m];
    long long max_v = 0;

    for (long i = 0; i < n; i++)
    {
        cin >> layers[i];
        if (layers[i] > max_v)
            max_v = layers[i];
    }

    for (long i = 0; i < m; i++)
        cin >> warriors[i];

    for(long i = 0; i < n-1; i++) //¬ычисление всех солнечных участков
    {
        if (layers[i] == max_v)
            max_v = max_el(layers, i+1, n);
        layers[i] -= max_v;
    }

    //qSortR(layers, n);
    //qSortR(warriors, m);
    sort(layers, layers+n);
    sort(warriors, warriors+m);

    /*for (int i = 0; i < n; i++)
        cout << layers[i] << " ";
    cout << endl;
    for (int i = 0; i < m; i++)
        cout << warriors[i] << " ";
    cout << endl;*/


    long l = 0;
    long mw_i = 0;
    long long mw;
    long answer = 0;

    while ((l < n) && (layers[n-(l+1)] > 0) && (mw_i < m))
    {
        mw = warriors[m-(1+mw_i)];

        if (mw <= layers[n-(l+1)])
        {
            answer++;
            l++;
        }
        mw_i++;
    }

    cout << answer << endl;
    return 0;
}
