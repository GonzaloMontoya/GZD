document.getElementById('formularioa').addEventListener('submit', function (e) {
    e.preventDefault();
  
    const usuario1 = document.getElementById('usuario1').value.trim();
    const contraseña = document.getElementById('contraseña').value;
    const messageElement = document.getElementById('message');
    if (usuario1.length < 4) {
      console.error('El nombre de usuario debe tener al menos 4 caracteres.');
      return;
    }
  
    if (contraseña.length < 8) {
      console.error('La contraseña debe tener al menos 8 caracteres, incluyendo al menos una letra minúscula, una mayúscula y un número.');
      return;
    }
   
    setTimeout(function () {
      messageElement.innerText = 'login exitoso. Te redirigiremos en breve.';
      document.getElementById('formularioa').reset();
    }, 1000);
  });
  