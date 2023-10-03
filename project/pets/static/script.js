

// function show_pets() {
//   let div = document.getElementById('div');
//   div.hidden = !div.hidden;
//   }

// let btn = document.getElementById('btn');
// btn.addEventListener('click', show_pets);


const el = document.getElementById('btn');
if (el) {
  el.addEventListener('click', swapper, false);
}