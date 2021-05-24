document.body.onload = event => {
  if (localStorage.getItem("notificate") === null) {
    Swal.fire({
      showCancelButton: true,
      confirmButtonText: `Согласен с условиями`,
      cancelButtonText: 'Закрыть',
      html: '<p class="mt-3"> Продолжая работу с сайтом вы косвенно соглашаетесь с <a style="text-color: orange!important; " href=/privacy/><strong>политикой в отношении обработки персональных данных</strong></a></p>'
      + '<p>При использовании данного сайта, вы подтверждаете свое согласие на использование файлов cookie в соответствии с настоящим уведомлением в отношении данного типа файлов. Если вы не согласны с тем, чтобы на сайте используется данный тип файлов, то вы должны соответствующим образом установить настройки вашего браузера или не использовать Сайт.</p>'
    }).then((result) => {
      if (result.isConfirmed) {
        localStorage.setItem("notificate","true");
      } else {
      }
    })
  }

};
