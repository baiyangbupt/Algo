#include<iostream>
#include<string>
#include<vector>

using namespace std;

int solution(string &s1, string &s2){
	vector<int> v(s1.size(),0);

	for(int i = 0; i < s2.size(); i++){
		int pre = 0;
		for(int j = 0; j < s1.size(); j++){
			int t = v[j];

			if(s1[j]==s2[i]){
				v[j] = min(pre,v[j]+1);
				v[j] = min(v[j],v[j-1]+1);
			}
			else
				v[j] = min(v[j]+1, v[j-1]+1);

			pre = t;
		}
	}

	return v[s1.size()-1];
}


int main(int argc, char **argv){
	string a,b;
	while(cin>>a>>b){
		cout << solution(a,b) << endl;
	}
}
