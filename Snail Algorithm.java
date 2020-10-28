package com.test.question.q13;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q10 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		// 요구사항.010
		// 아래와 같이 출력하시오.
		// 행/열 동일한 값, 홀수만 입력
		
        System.out.print("몇방진? (ex. 3, 5, 7, ...) :");
        int size=Integer.parseInt(reader.readLine());
       
        int[][] array =new int[size][size];
        
        
        int x=array.length/2;
        int y=size-1;
        array[x][y]=1;
        int num=2;
        while(num<=size*size){ // 칸을 모두 채울 때까지
        	int nx=x-1;
        	int ny=y+1;

        	if (nx<0) {
        		nx+=size;
        	}
        	if (ny>=size) {
        		ny-=size;
        	}
        	
        	if (array[nx][ny]==0) {
        		array[nx][ny]=num;
        		num++;
        		x=nx;
        		y=ny;
        	}else {
        		x++;
        		y-=2;
        	}
        }
		
		for (int i=0;i<array.length;i++) {
			for (int j=0;j<array[0].length;j++) {
				System.out.printf("%4d", array[i][j]);
			}
			System.out.println();
		}
	}
}
