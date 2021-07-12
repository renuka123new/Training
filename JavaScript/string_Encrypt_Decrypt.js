const str = 'HellothisIsAString';
const getMap = (legend, shift) => {
   return legend.reduce((charsMap, currentChar, charIndex) => {
      const copy = { ...charsMap };
      let ind = (charIndex + shift) % legend.length;
      if (ind < 0) {
         ind += legend.length;
      };
      copy[currentChar] = legend[ind];
      return copy;
   }, {});
};
const encrypt = (str, shift = 0) => {
   const legend = 'abcdefghijklmnopqrstuvwxyz'.split('');
   const map = getMap(legend, shift);
   return str.toLowerCase().split('').map(char => map[char] || char).join('');
};
var encrypted_String = encrypt(str, 6);
console.log("Encrypted string = "+encrypted_String);

const getMapDecrypt = (legend, shift) => {
	return legend.reduce((charsMap, currentChar, charIndex) => {
	   const copy = { ...charsMap };
	   let ind = (charIndex - shift) % legend.length;
	   if (ind < 0) {
		  ind += legend.length;
	   };
	   copy[currentChar] = legend[ind];
	   return copy;
	}, {});
 };
 const decrypt = (str, shift = 0) => {
	const legend = 'abcdefghijklmnopqrstuvwxyz'.split('');
	const map = getMapDecrypt(legend, shift);
	return str.toLowerCase().split('').map(char => map[char] || char).join('');
 };

 var decrypt_String = decrypt(encrypted_String, 6);
console.log("Decrypted string = "+decrypt_String);
