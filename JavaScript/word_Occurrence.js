const str = "big black bug bit a big black dog on his big black nose big big on";
const findDuplicateWords = str => {
   const strArr = str.split(" ");
   return strArr;
};
//console.log(findDuplicateWords(str));
var str_Array=findDuplicateWords(str);

function removeDuplicate(data){
  return data.filter((value,index)=>data.indexOf(value)===index);
}
//console.log(removeDuplicate(str_Array));
no_Duplicate_Array=removeDuplicate(str_Array);

function countOccurrences(str,word)
{
    // split the string by spaces in a
let a = str.split(" ");

// search for pattern in a
let count = 0;
for (let i = 0; i < a.length; i++)
{
// if match found increase count
if (word==(a[i]))
    count++;
}

return count;
}

for(let x=0;x<no_Duplicate_Array.length;x++){
  let word=no_Duplicate_Array[x];
  console.log (word+" = "+countOccurrences(str, word));
}