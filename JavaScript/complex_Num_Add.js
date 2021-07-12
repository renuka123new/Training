function Complex(real1, imaginary1) {
 
    this.real1 = 0;
   
    this.imaginary1 = 0;
   
    this.real1 = (typeof real1 === 'undefined') ? this.real1 : parseFloat(real1);
   
    this.imaginary1 = (typeof imaginary1 === 'undefined') ? this.imaginary1 : parseFloat(imaginary1);
   
  }
   
  Complex.transform = function(num) {
   
    var complex;
   
    complex = (num instanceof Complex) ? num : complex;
   
    complex = (typeof num === 'number') ? new Complex(num, 0) : num;
   
    return complex;
   
  };
   
  function display_complex(re, im) {
   
    if(im === '0') return '' + re;
   
    if(re === 0) return '' + im + 'i';
   
    if(im < 0) return '' + re + im + 'i';
   
    return '' + re + '+' + im + 'i';
   
  }
   
  function complex_num_add(first, second) {
   
    var num1, num2;
   
    num1 = Complex.transform(first);
    num2 = Complex.transform(second);
   
    var real1_add = num1.real1 + num2.real1;
    var imaginary1_add = num1.imaginary1 + num2.imaginary1;
    console.log("Addition = "+display_complex(real1_add, imaginary1_add));

    var real1_sub = num1.real1 - num2.real1;
    var imaginary1_sub = num1.imaginary1 - num2.imaginary1;
    console.log("Substraction = "+display_complex(real1_sub, imaginary1_sub));

    var real1_mul = (num1.real1 * num2.real1) - (num1.imaginary1 * num2.imaginary1);
    var imaginary1_mul = (num1.real1 * num2.real1) + (num1.imaginary1 * num2.imaginary1);
    console.log("Multiplication = "+display_complex(real1_mul, imaginary1_mul));

    var real1_div = num1.real1 / num2.real1;
    var imaginary1_div = num1.imaginary1 / num2.imaginary1;
    console.log("Division = "+display_complex(real1_div, imaginary1_div));
   
   
  }
   
   var a = new Complex(2, 3);
   var b = new Complex(4,  5);
   
  //console.log(complex_num_add(a,b));
  complex_num_add(a,b);
   
  //document.getElementById('add').innerHTML=complex_num_add(a,b);