package com.test.question.q13;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q09 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		// 요구사항.009
		// 아래와 같이 출력하시오.
	    System.out.print("행/열 입력(ex. 1, 2, 3, 4, ...) : ");
	    int size=Integer.parseInt(reader.readLine());
        
	    int[][] array=new int[size][size];
	    
	    int x=0; // 행을 나타내며, y와 합쳐져서 위치를 나타낸다.
	    int y=0; // 열을 나타내며, x와 합쳐져서 위치를 나타낸다.
	    int num=1;
	    int move=size; // 한 방향으로 이동하는 횟수. 제일 처음 시작하면 오른쪽방향으로 size만큼 이동하기 때문에 size로 초기화.
	    for (int i=0;i<2*size-1;i++) { // 방향을 바꾸며 진행되는 횟수가 2*size-1이다.
	    	// 달팽이 알고리즘은 오른쪽, 아래쪽, 왼쪽, 위쪽 총 4개 방향으로 진행된다.
	    	// 진행횟수를 방향과 연결지어보면
	    	// 진행횟수%4가 0이면 오른쪽, 1이면 아래쪽, 2면 왼쪽, 3이면 위쪽이다.
	    	switch(i%4) {
		    	case 0: // 오른쪽으로 증가
		    		for (int j=0;j<move;j++) { // 오른쪽으로 move만큼 이동하라는 의미.
		    			array[y][x]=num; // 오른쪽으로 1씩 이동하면서 1씩 증가하는 num을 넣어준다.
		    			x++;
		    			num++;
		    		}
		    		x--; // 오른쪽으로 이동하는 위 for문이 끝나면 x는 1만큼 벗어나게 되므로 1을 빼준다.
		    		y++; // 마찬가지로, 오른쪽 이동이 끝나면 한 칸 아래로 내려와 아래쪽으로 증가해야하므로 y를 1 증가시킨다.
		    		move--; // 아래쪽으로 이동하면서 원래 이동했던 사이즈보다 1 작은 사이즈만큼 이동해야 하므로 1을 빼준다.
		    		break;
		    	case 1: // 아래쪽으로 증가(오른쪽으로 이동이 끝나고 y가 1씩 증가해야 한다.)
		    		for (int j=0;j<move;j++) {
		    			array[y][x]=num; // 아래쪽으로 1씩 이동하면서 1씩 증가하는 num을 넣어준다.
		    			y++;
		    			num++;
		    		}
		    		y--;
		    		x--; // 아래쪽으로의 이동이 끝나면 왼쪽으로 증가해야 하므로 x를 -1 해준다.
		    		// 오른쪽으로의 이동이 끝나면서 size를 줄여야해서 move--;를 해줬지만 아래쪽으로 이동했다가 왼쪽으로 가는 경우는 같은 size이기 때문에 move를 바꿔주지 않는다.
		    		break;
		    	case 2: // 왼쪽으로 증가
		    		for (int j=0;j<move;j++) {
		    			array[y][x]=num; // 왼쪽으로 1씩 이동하면서 1씩 증가하는 num을 넣어준다.
		    			x--;
		    			num++;
		    		}
		    		y--; // 왼쪽으로의 이동이 끝나면 위쪽으로 증가해야 하므로 y를 -1 해준다.
		    		x++;
		    		move--;
		    		break;
		    	case 3: // 위쪽으로 증가
		    		for (int j=0;j<move;j++) {
		    			array[y][x]=num; // 위쪽으로 1씩 이동하면서 1씩 증가하는 num을 넣어준다.
		    			y--;
		    			num++;
		    		}
		    		y++;
		    		x++; // 위쪽으로의 이동이 끝나면 오른쪽으로 이동해야 하므로 x를 1 증가시킨다.
		    		break;
	    	}
	    }
	    for(int k=0;k<array.length;k++) {
          for(int t=0; t<array[k].length;t++) {
              System.out.printf("%3s", array[k][t]);  
          }
          System.out.println();
	    }
    }
}
