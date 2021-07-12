const arr1 = [0, 1, 2, [3, 4],[1,9]];
console.log("First Example ");
console.log(arr1.flat());
// expected output: [0, 1, 2, 3, 4]

const arr2 = [0, 1, 2, [[[3, 4]]]];
console.log("Second Example ");
console.log(arr2.flat(2));

function flatten(arr) {
    return arr.reduce((acc, cur) => acc.concat(Array.isArray(cur) ? flatten(cur) : cur), []);
};
 
const nested_Arr = [[[10,1],2],[[3,[9,7]],[4,[5]]]];
 
const single_list = flatten(nested_Arr);
console.log("Required single array");
console.log(single_list);