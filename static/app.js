function allowOnlyNumbers(input) {
  input.value = input.value.replace(/\D/g, "");
}

function togglePassword(inputId, icon) {
  const input = document.getElementById(inputId);
  if (input.type === "password") {
    input.type = "text";
    icon.textContent = "🙈";
  } else {
    input.type = "password";
    icon.textContent = "👁";
  }
}

function checkEmailChange(input) {
  const originalEmail = input.dataset.original;
  const passwordSection = document.getElementById("password-section");

  if (input.value !== originalEmail) {
    passwordSection.style.display = "block";
  } else {
    passwordSection.style.display = "none";
  }
}

async function checkDuplicate(type, value, input, docId = null) {
  if (!value) return;

  const response = await fetch("/check-duplicate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      [type]: value,
      doc_id: docId,
    }),
  });

  const result = await response.json();

  if (result.status === type) {
    alert(type.toUpperCase() + " already exists");
    input.value = "";
    input.focus();
  }
}
document
  .getElementById("editUserForm")
  ?.addEventListener("submit", function (e) {
    e.preventDefault();
    let valid = true;

    const name = document.getElementById("name");
    const contact = document.getElementById("contact");
    const email = document.getElementById("email");

    const password = document.getElementById("password");
    const confirm = document.getElementById("confirm_password");
    const passwordSection = document.getElementById("password-section");

    // Clear errors
    document
      .querySelectorAll(".error-input")
      .forEach((i) => i.classList.remove("error-input"));
    document.querySelectorAll("small").forEach((s) => (s.textContent = ""));

    // Name
    if (name.value.trim().length < 3) {
      name.classList.add("error-input");
      name.nextElementSibling.textContent = "Minimum 3 characters required";
      valid = false;
    }

    // Contact
    if (!/^[0-9]{10}$/.test(contact.value)) {
      contact.classList.add("error-input");
      contact.nextElementSibling.textContent = "Contact must be 10 digits";
      valid = false;
    }

    // Email
    if (!/^\S+@\S+\.\S+$/.test(email.value)) {
      email.classList.add("error-input");
      email.nextElementSibling.textContent = "Enter valid email";
      valid = false;
    }

    // Password required only if email changed
    if (passwordSection.style.display === "block") {
      if (password.value.length < 6) {
        password.classList.add("error-input");
        password.nextElementSibling.textContent =
          "Minimum 6 characters required";
        valid = false;
      }
      if (password.value !== confirm.value) {
        confirm.classList.add("error-input");
        confirm.nextElementSibling.textContent = "Passwords do not match";
        valid = false;
      }
    }

    if (valid) {
      this.submit();
    }
  });
