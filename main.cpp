#include <bits/stdc++.h>

using namespace std;

#define f first
#define s second
#define sz size
#define pb push_back
#define mp make_pair
#define endl '\n'

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

template < class T >

ostream& operator << (ostream& os, const vector<T>& v) {
  int quantity = 0;
  for (typename vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
    quantity == 0 ? os << *ii : os << " " << *ii;
    quantity++;
  }
  os << endl;
  return os;
}


int main(void) {
  cin.tie(NULL);
  cout.tie(NULL);
  ios::sync_with_stdio(0);
  
  int n, k, c_1, c_2;
  string p_1, p_2;
  unordered_map<string, unordered_set<int>> count;
  cin >> n >> k;
  while (k--) {
    cin >> c_1 >> c_2 >> p_1 >> p_2;
    if (p_1 == p_2) {
      n -= 2;
      count.erase(p_1);
    } else {
      if (count.find(p_1) == count.end()) {
        count.insert({p_1, {}});
      }
      if (count.find(p_2) == count.end()) {
        count.insert({p_2, {}});
      }
      count[p_1].insert(c_1);
      count[p_2].insert(c_2);
    }
  }

  int points = 0;
  int aloneCards = 0;
  for (pair<string, unordered_set<int>> x: count) {
    if ((int) x.s.size() == 2) {
      n -= 2;
      points++;
    } else {
      aloneCards++;
    }
  }
  
  if (n == 2 && aloneCards == 0) {
    points += 1;
  } else if (n - aloneCards == aloneCards ){
    points += aloneCards;
  }
  cout << points << endl;

  return 0;
}

// g++ -Wall -std=c++17 main.cpp -o main && ./main < in > my_out && diff out my_out
