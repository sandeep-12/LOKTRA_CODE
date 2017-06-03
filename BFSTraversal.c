#include <stdio.h>

int COST = 6;
int EDGE[1000*(1000-1)/2+1][2];
int FROM = 0;
int TO  = 1;
int STATUS  = 1;
int SPENT = 0;
int PENDING = 1;
int DISTANCE = 0;

int main() {
    
	int t, n, m, active, i, s;
	int node[1000+1][2];	
	unsigned int min;
	
	scanf("%d", &t);
	
	while(t--){
		scanf("%d %d", &n, &m);
		
		for(i=1; i <= m; i++){
			scanf("%d %d", &EDGE[i][FROM], &EDGE[i][TO]);
		}
	
		for(i=1; i <= n; i++){
			node[i][DISTANCE] = -1;
			node[i][STATUS] = PENDING;
		}
		
		scanf("%d", &s);
        active = s;
		node[s][DISTANCE] = 0;
		min = 0;
		while(active){
			
			active = 0;
			min = -1;
			for(i=1; i <= n; i++){
				if(node[i][STATUS]==PENDING && node[i][DISTANCE]!=-1 && node[i][DISTANCE]<min){
					min = node[i][DISTANCE];
					active = i;
				}
			}
	
			for(i=1; i<=m; i++){
				if(EDGE[i][FROM]==active){
					if(node[EDGE[i][TO]][DISTANCE]>node[EDGE[i][FROM]][DISTANCE]+COST || node[EDGE[i][TO]][DISTANCE]==-1){
						node[EDGE[i][TO]][DISTANCE]=node[EDGE[i][FROM]][DISTANCE]+COST;
					}
				}
				if(EDGE[i][TO]==active){
					if(node[EDGE[i][FROM]][DISTANCE]>node[EDGE[i][TO]][DISTANCE]+COST || node[EDGE[i][FROM]][DISTANCE]==-1){
						node[EDGE[i][FROM]][DISTANCE]=node[EDGE[i][TO]][DISTANCE]+COST;
					}
				}
			}
	
			node[active][STATUS] = SPENT;
	
		}
	
		for(i=1; i<=n; i++){
			if(i!=s)printf("%d ", node[i][DISTANCE]);
		}
	
		printf("\n");
	}
    
    return 0;
}
