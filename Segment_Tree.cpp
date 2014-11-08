#include<iostream>
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1
using namespace std;

const int inf = 0x7fffffff;
int m[4*10000], n;

void pushup(int rt){
	m[rt] = min(m[rt<<1], m[rt<<1|1]);
}

void build(int l, int r, int rt){
	if(l==r){
		cin >> m[rt];
		return;
	}

	int m = (l+r)>>1;

	build(lson);
	build(rson);
	pushup(rt);
}

void update(int changeto, int p, int l, int r, int rt){
	if(l==r){
		m[rt] = changeto;
		return;
	}

	int m = (l+r)>>1;

	if(l<=p&&m>=p)
		update(changeto, p, lson);
	else if(m<p&&r>=p)
		update(changeto, p, rson);

	pushup(rt);
}

int query(int L, int R, int l, int r, int rt){
	if(L <= l && R >= r){
		return m[rt];
	}

	int res1 = inf, res2 = inf,  m = (l+r)>>1;

	if(L <= m)
		res1 = query(L, R, lson);
	if(R > m)
		res2 = query(L, R, rson);

	return min(res1,res2);
}

int main(){
	cin >> n;
	build(1,n,1);
	int q;
	cin >> q;
	while(q--){
		int t,a,b;
		cin >> t;
		if(0 == t){
			cin >> a >> b;
			cout << query(a,b,1,n,1) << endl;
		}
		else{
			cin >> a >> b;
			update(b,a,1,n,1);
		}
	}
}

