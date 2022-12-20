const navbar = document.getElementById('navbar');
const a = document.getElementById('a');
const b = document.getElementById('b');
const c = document.getElementById('c');
const i = document.getElementById('i');

window.onscroll = function() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    navbar.classList.add('nav');
    a.style.color = "black";
    b.style.color = "black";
    c.style.color = "black";
    i.classList.add('fa-solid');
    i.classList.add('fa-circle-up');
    i.classList.add('toup');
  } 
  else{
      navbar.classList.remove('nav');
      a.style.color = "white";
      b.style.color = "white";
      c.style.color = "white";
      i.classList.remove('fa-solid');
      i.classList.remove('fa-circle-up');
      i.classList.remove('toup');
  }
}
// button ke atas
const tutop = function(){
  return location.href="#home";
}
// toggle menu 
const menu = document.getElementById('menu_');

const ganti = function(){
  menu.classList.toggle('opened');
}
const hilang = function(){
  menu.classList.remove('opened');
}

// ketika gambar tidak sesuai
window.onload = function(){
if (document.getElementById("p").innerHTML == 'upload gambar ikan cupang dengan format .jpg , .jpeg atau .png') {
   location.href="#prediksi";
}
else if(document.getElementById("p").innerHTML == 'ini bukan gambar ikan cupang'){
  location.href="#prediksi";
}
else{

}
}


// MENAMPILKAN GAMBAR YANG AKAN DI UPLOAD
//selecting all required elements
const abc = document.querySelector(".file-form");
const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
button = abc.querySelector("button"),
input = abc.querySelector("input");
let file; //this is a global variable and we'll use it inside multiple functions

// button.onclick = ()=>{
//   input.click(); //if user click on the button then the input also clicked
// }

input.addEventListener("change", function(){
  //getting user select file and [0] this means if user select multiple files then we'll select only the first one
  file = this.files[0];
  dropArea.classList.add("active");
  showFile(); //calling function
});

function showFile(){
  let fileType = file.type; //getting selected file type
  let validExtensions = ["image/jpeg", "image/jpg", "image/png"]; //adding some valid image extensions in array
  if(validExtensions.includes(fileType)){ //if user selected file is an image file
    let fileReader = new FileReader(); //creating new FileReader object
    fileReader.onload = ()=>{
      let fileURL = fileReader.result; //passing user file source in fileURL variable
      let imgTag = `<img src="${fileURL}" alt="">`; //creating an img tag and passing user selected file source inside src attribute
      dropArea.innerHTML = imgTag; //adding that created img tag inside dropArea container
    }
    fileReader.readAsDataURL(file);
  }else{
    alert("This is not an Image File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}


