document.getElementById('formularioai').addEventListener('submit', function (e) {
  e.preventDefault();

  const usuario = document.getElementById('usuario').value.trim();
  const correo = document.getElementById('correo').value.trim();
  const password = document.getElementById('password').value;

  const messageElement = document.getElementById('message');
  messageElement.innerText = '';
  messageElement.className = '';

  if (usuario.length < 4) {
    messageElement.innerText = 'El nombre de usuario debe tener al menos 4 caracteres.';
    messageElement.className = 'error';
    return;
  }

  const correoRegex = /^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if (!correoRegex.test(correo)) {
    messageElement.innerText = 'Por favor, introduce un correo electrónico válido.';
    messageElement.className = 'error';
    return;
  }

  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passwordRegex.test(password)) {
    messageElement.innerText = 'La contraseña debe tener al menos 8 caracteres, incluyendo al menos una letra minúscula, una mayúscula y un número.';
    messageElement.className = 'error';
    return;
  }

  
  setTimeout(function () {
    messageElement.innerText = 'Registro exitoso. Te redirigiremos en breve.';
    messageElement.className = 'success';
    document.getElementById('formularioai').reset();
  }, 1000);
});