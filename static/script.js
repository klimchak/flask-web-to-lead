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

  function inputs(){
      let inputsAll = document.getElementsByTagName('input');
      let arrIdInput = [];
      for (let i = 0; i < 11; i++){
        arrIdInput.push(inputsAll[i].id);
      }
      jQuery.each( arrIdInput, function( i, val ) {
        $( "#" + val ).on("change", function (){
          if (val == 'company_site' || val == 'email'){
          }else {
            this.value = this.value[0].toUpperCase() + this.value.slice(1);
          }
          let text = this.value;
          let idText = val + 'Text';
          $( "#" + idText).text(text);
        });
      });
      return arrIdInput;
    }
    let arrIdInputGlobal = inputs();

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
          let regSite = /((((http|https):(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)(\.\w{2,3})))/i;
          let regDate = /^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])/;
          let regEmail = /^([a-z0-9]+(?:[._-][a-z0-9]+)*)@([a-z0-9]+(?:[.-][a-z0-9]+)*\.[a-z]{2,})$/i;
          let error = 'Error value in fields: ';
          jQuery.each( arrIdInputGlobal, function( i, val ) {
            let valInput = $( "#" + val ).val();
            valInput = valInput.trim();
            if (val == 'company_site'){
              if(!regSite.test(valInput)){
                let valInError = val.replace('_', ' ');
                error = error + valInError + '; ';
              }
            }
            else if (val == 'birthday'){
              if(!regDate.test(valInput)){
                error = error + val + '; ';
              }
            }
            else if (val == 'email'){
              if(!regEmail.test(valInput)){
                error = error + val + '; ';
              }
            }
            else{
              let regString = /^([A-Z0-9][A-Za-z0-9 ,.'`-]{3,50})$/gm;
              if(!regString.test(valInput)){
                if (val.indexOf("_") === -1) {
                    error = error + val + '; ';
                }else {
                  let valInError = val.replace('_', ' ');
                  error = error + valInError + '; ';
                }
              }
            }
          });
          if (error.length > 23){
            event.preventDefault();
            event.stopPropagation();
            $('.toast-body').text(error);
            $('.toast').toast('show');
          }
          form.classList.add('was-validated')
        }, false)
      })
    })()

});