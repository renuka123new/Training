// program to create a two dimensional array

function twoDimensionArray(a, b) {
    let arr = [];

    // creating two dimensional array
    for (let i = 0; i< a; i++) {
        for(let j = 0; j< b; j++) {
            arr[i] = [];
        }
    }

    // inserting elements to array
    var count=1;
    for (let i = 0; i< a; i++) {
        for(let j = 0; j< b; j++) {
            arr[i][j] = 0;
        }
    }
    return arr;
}

function checkQueen(board,a,b){
	if((a===0 || a===(x-1))&&(b===0 || b===(x-1))){
		console.log("corner box");

		if(a===0 && b===0){
			if(board[a][b+1]===1 || board[a+1][b]===1 || board[a+1][b+1]===1){console.log("dead");}
			else{console.log("live");}
		}
		else if(a===0 && b===(x-1)){
			if(board[a][b-1]===1 || board[a+1][b]===1 || board[a+1][b-1]===1){console.log("dead");}
			else{console.log("live");}
		}
		else if(a===(x-1) && b===0){
			if(board[a-1][b]===1 || board[a][b+1]===1 || board[a-1][b+1]===1){console.log("dead");}
			else{console.log("live");}
		}
		else if(a===(x-1) && b===(x-1)){
			if(board[a][b-1]===1 || board[a-1][b]===1 || board[a-1][b-1]===1){console.log("dead");}
			else{console.log("live");}
		}
		
	}

	else if((a===0 || a===(x-1))||(b===0 || b===(x-1))){
		console.log("side box");
		if(a===0){
			if(board[a][b-1]===1 || board[a][b+1]===1 || board[a+1][b]===1 || board[a+1][b-1]===1 || board[a+1][b+1]===1){console.log("dead");}
			else{console.log("live");}
		}
		else if(b===0){
			if(board[a-1][b]===1 || board[a+1][b]===1 || board[a][b+1]===1 || board[a-1][b+1]===1 || board[a+1][b+1]===1){console.log("dead");}
			else{console.log("live");}
		}
		else if(a===(x-1)){
			if(board[a][b-1]===1 || board[a][b+1]===1 || board[a-1][b]===1 || board[a-1][b-1]===1 || board[a-1][b+1]===1){console.log("dead");}
			else{console.log("live");}
		}
		else if(b===(x-1)){
			if(board[a][b-1]===1 || board[a-1][b]===1 || board[a+1][b]===1 || board[a-1][b-1]===1 || board[a+1][b-1]===1){console.log("dead");}
			else{console.log("live");}
		}
	}
	else{
		console.log("middle box");
		if(board[a-1][b-1]===1 || board[a-1][b]===1 || board[a-1][b+1]===1 || board[a][b-1]===1 || 
		   board[a][b+1]===1 || board[a+1][b-1]===1 || board[a+1][b]===1 || board[a+1][b+1]===1){console.log("dead");}
		else{console.log("live");}
	}
}
const x = 8;
const y = 8;

const result = twoDimensionArray(x, y);
var queen1_x=3,queen1_y=5;	//position of first queen given by user
result[queen1_x][queen1_y]=1;
var queen2_x=2,queen2_y=5;	//position of second queen given by user
checkQueen(result,queen2_x,queen2_y);
//console.log(result);

