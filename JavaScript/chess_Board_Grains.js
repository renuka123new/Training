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
            arr[i][j] = count;
            count=count*2;
        }
    }
    return arr;
}

const x = 8;
const y = 8;

const result = twoDimensionArray(x, y);
//console.log(result);
ans=result.flat();
var user_input=12;      //Number of block given by user
console.log(ans[user_input-1]);
