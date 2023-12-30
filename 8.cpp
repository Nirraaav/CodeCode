#include <bits/stdc++.h>
 
using namespace std;

typedef long long int ll;
typedef long double ld;
 
const ld pi = acos(-1.0);

#define lb lower_bound
#define ub upper_bound
#define endl '\n'
#define sz(x) (ll) x.size()
#define all(v) v.begin(),v.end() 
#define rall(v) v.rbegin(),v.rend() 
#define pb push_back
#define mp make_pair

typedef pair<long long int, long long int> pii;
typedef vector<long long int> vl;
typedef vector<vector<long long int>> vvl;
 
void solve(){
	set<ll> s;
	for(ll i = 0; i < 27; i++){
		for(ll j = 0; j < 17; j++){
			if(pow(2, i) * pow(3, j) < 82301728 && pow(2, i) * pow(3, j) >= 12){
				s.insert(pow(2, i) * pow(3, j));
			}
		}
	}
	for(auto i : s){
		cout << i << ' ';
	}
	cout << endl;
	cout << sz(s) << endl;
}
 
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); 
	cout.tie(NULL);	

	ll t = 1;
	// cin >> t;
	while(t--){
		solve();
	}    
}    