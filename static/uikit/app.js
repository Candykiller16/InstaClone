// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();

});


let alertWrapper = document.getElementsByClassName('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertWrapper.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}