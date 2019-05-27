#include <stdio.h> 
#include<conio.h>
#include<iostream>
//the rods are A B C
int A[100];
int B[100];
int C[100];
int possibelMoves[100];
int n,topA, topB, topC;
using namespace std;

void initialize() {
	for (int i = 0; i < n; i++) {
		A[i+1] =n-i;
	}
 }


bool isfinal() {
	for (int i = 0; i < n; i++) {
		if (C[i+1] !=n-i)
			return false;
	}
	return true;
}
void Move(int &topA,int &topB,int &topC) {
	bool ok = false;
	int start;
	int choose;
	while (ok != true) {
		start=rand() % 3 + 1;
		if (start == 1 && topA!=0) {
			if (A[topA] < B[topB]||topB==0)
				possibelMoves[0] = 2;
			if (A[topA] < C[topC]||topC==0)
				possibelMoves[1] = 3;
			
			if (possibelMoves[0] != 0 && possibelMoves[1] != 0)
			{
				choose = rand() % 2 + 1;
				ok = true;
			}
			else if (possibelMoves[0] != 0) {
				choose = 2;
				ok = true;
			}
			else if (possibelMoves[1] != 0) {
				choose = 3;
				ok = true;
			}
		}
		else if (start == 2 && topB!=0) {
			if (B[topB] < A[topA]||topA==0)
				possibelMoves[0] = 1;
			if (B[topB] < C[topC]||topC==0)
				possibelMoves[1] = 3;

			if (possibelMoves[0] != 0 && possibelMoves[1] != 0)
			{
				choose = rand() % 2 + 1;
				ok = true;
			}
			else if (possibelMoves[0] != 0) {
				choose = 1;
				ok = true;
			}
			else if (possibelMoves[1] != 0) {
				choose = 3;
				ok = true;
			}
		}
		else if (start == 3&&topC!=0) {
			if (C[topC] < B[topB]||topB==0)
				possibelMoves[0] = 2;
			if (C[topC] < A[topA]||topA==0)
				possibelMoves[1] = 1;

			if (possibelMoves[0] != 0 && possibelMoves[1] != 0)
			{
				choose = rand() % 2 + 1;
				ok = true;
			}
			else if (possibelMoves[0] != 0) {
				choose = 2;
				ok = true;
			}
			else if (possibelMoves[1] != 0) {
				choose = 1;
				ok = true;
			}
		}

		cout << A[topA] << " ";

		cout << B[topB] << " ";

		cout << C[topC] << endl;

	}
	if (start == 1) {
		if (possibelMoves[choose] == 2) {
			
			topB++;
			B[topB] = A[topA];
			A[topA] = 0;
			topA--;
		}
		else if (possibelMoves[choose] == 3) {
			topC++;
			C[topC] = A[topA];
			A[topA] = 0;
			topA--;
		}
	}
	else if(start==2){
		if (possibelMoves[choose] == 1) {

			topA++;
			A[topA] = B[topB];
			B[topB] = 0;
			topB--;
		}
		else if (possibelMoves[choose] == 3) {
			topC++;
			C[topC] = B[topB];
			B[topB] = 0;
			topB--;
		}
	}
	else if (start == 3) {
		if (possibelMoves[choose] == 1) {
			topA++;
			A[topA] = C[topC];
			C[topC] = 0;
			topC--;
		}
		else if (possibelMoves[choose] == 2) {
			topB++;
			B[topB] = C[topC];
			C[topC] = 0;
			topC--;
		}
	}
}
void solveHanoi() {
	initialize();
	while(isfinal()==false) {
		Move(topA, topB, topC);
	}
}

int main() {
	cout << "Introdu numarul de cercuri:";
	cin >> n;
	topA = n;
	topB = 0;
	topC = 0;
	solveHanoi();
}