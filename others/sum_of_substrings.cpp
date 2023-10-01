/**
 * @file sum_of_substrings.cpp
 * @author jhonatangopereira
 * @brief Given a string of binary digits, find the minimum sum of all substrings of length 2
 * @date 2023-10-01
*/
#include <bits/stdc++.h>

using namespace std;


int calculate_sum_of_substrings(int n, string s);
int get_the_best_optimal_string(int n, int k, string s);

/**
 * @brief Given a string of digits, find the maximum sum of any substring of length k
 * @return 0
*/
int main(void) {
    int t = 0;  // number of test cases
    cin >> t;
    for (int i = 0; i < t; i++) {  // for each test case
        int n;  // length of string
        int k;  // maximum number of operations
        cin >> n >> k;

        string s;  // string
        cin >> s;

        int sum = get_the_best_optimal_string(n, k, s);
        for (int j = 0; j < k; j++) {  // for each operation
            sum += s[j] - '0';
        }
        cout << sum << endl;
    }

    return 0;
}

/**
 * @brief Calculate the sum of all substrings of a string
 * @param n length of string
 * @param s string
 * @return sum of all substrings of a string
*/
int calculate_sum_of_substrings(int n, string s) {
    int sum = 0;
    string two_digits;
    for (int i = 0; i < n - 1; i++) {
        two_digits = s[i] + s[i + 1];
        // transform two_digits to integer
        sum += stoi(two_digits);
    }
    return sum;
}

/**
 * @brief Get the best optimal string with minimum sum of all substrings of length 2
 * @param n length of string
 * @param k maximum number of operations
 * @param s string
 * @return the best optimal string
*/
int get_the_best_optimal_string(int n, int k, string s) {
    int actual_sum, lowest_sum = 0;
    lowest_sum = calculate_sum_of_substrings(n, s);
    int sum = 0;
    for (int op = 0; op < k; op++) {  // for each operation
        sum = calculate_sum_of_substrings(n, s);
        if (sum > lowest_sum) {
            lowest_sum = sum;
        }
    }
    return sum;
}
