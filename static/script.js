$(document).ready(function(){
  $("#formStep2").hide();
  $("#formStep3").hide();

  $("#btnNextOn2").click(function(){
    $("#formStep1").hide();
    $("#formStep2").show();
  });

  $("#btnNextOn3").click(function(){
    $("#formStep2").hide();
    $("#formStep3").show();
  });

  $("#btnPrevOn1").click(function(){
    $("#formStep2").hide();
    $("#formStep1").show();
  });

  $("#btnPrevOn2").click(function(){
    $("#formStep3").hide();
    $("#formStep2").show();
  });

  (function () {
  'use strict'
  let forms = document.querySelectorAll('.needs-validation')
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
      }, false)
    })
  })()

  function inputs(){
    let inputsAll = document.getElementsByTagName('input');
    let arrIdInput = [];
    for (let i = 0; i < 11; i++){
      arrIdInput.push(inputsAll[i].id);
    }
    jQuery.each( arrIdInput, function( i, val ) {
      $( "#" + val ).on("change", function (){
        let text = this.value;
        let idText = val + 'Text';
        $( "#" + idText).text(text);
      });
    });
  }
  inputs();

});