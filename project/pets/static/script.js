document.addEventListener('DOMContentLoaded', function() {
  const toggleButtons = document.querySelectorAll('.btn');

  toggleButtons.forEach(button => {
    button.addEventListener('click', function(event) {
      const div = this.nextElementSibling;
      div.classList.toggle('d-none');
     });
  });
});
