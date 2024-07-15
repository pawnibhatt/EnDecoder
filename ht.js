function encodeText() {
  const form = document.querySelector("form.login");
  const formData = new FormData(form);

  fetch('/encrypt', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    form.querySelector("input[name='result']").value = data.result;
  })
  .catch(error => console.error('Error:', error));
}

function decodeText() {
  const form = document.querySelector("form.signup");
  const formData = new FormData(form);

  fetch('/decrypt', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    form.querySelector("input[name='result']").value = data.result;
  })
  .catch(error => console.error('Error:', error));
}

const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");

signupBtn.onclick = () => {
  document.querySelector("form.login").style.marginLeft = "-50%";
};
loginBtn.onclick = () => {
  document.querySelector("form.login").style.marginLeft = "0%";
};


