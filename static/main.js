function updateUser(event, userId) {
  const name = event.target.value;
  fetch(`/api/users/${userId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name }),
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleUserError(error, userId));
    })
    .catch((error) => console.error(error));
}

function updateTask(event, taskId) {
  const name = event.target.value;
  fetch(`/api/tasks/${taskId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name }),
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleTaskError(error, taskId));
    })
    .catch((error) => console.error(error));
}

function handleUserError(error, userId) {
  const button = document.querySelector(`#user-${userId} button`);
	const previousText = button.innerText;

  button.innerText = error.detail;
	button.classList.add("error");
  setTimeout(() => {
    button.innerText = previousText;
		button.classList.remove("error");
  }, 3000);
}

function handleUserFormError(error) {
  const errorSpan = document.querySelector(`#user-form .error`);
  errorSpan.innerText = error.detail;
  setTimeout(() => {
    errorSpan.innerText = "";
  }, 3000);
}

function handleTaskFormError(error) {
  const errorSpan = document.querySelector(`#task-form .error`);
  errorSpan.innerText = error.detail;
  setTimeout(() => {
    errorSpan.innerText = "";
  }, 3000);
}

function createTask(event) {
  event.preventDefault();
  const name = event.target[0].value;
  fetch(`/api/tasks/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name }),
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleTaskFormError(error));
    })
    .catch((error) => console.error(error));
}

function createUser(event) {
  event.preventDefault();
  const name = event.target[0].value;
  fetch(`/api/users/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name }),
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleUserFormError(error));
    })
    .catch((error) => console.error(error));
}

function deleteUser(userId) {
  fetch(`/api/users/${userId}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleUserError(error, userId));
    })
    .catch((error) => console.error(error));
}

function handleTaskError(error, taskId) {
  const button = document.querySelector(`#task-${taskId} button`);
	const previousText = button.innerText;

  button.innerText = error.detail;
	button.classList.add("error");
  setTimeout(() => {
    button.innerText = previousText;
		button.classList.remove("error");
  }, 3000);
}

function deleteUserFromTask(taskId, userId) {
  fetch(`/api/tasks/${taskId}/${userId}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleTaskError(error, taskId));
    })
    .catch((error) => console.error(error));
}

function addUser(event, taskId) {
  event.preventDefault();

  const userId = event.target[0].value;
  fetch(`/api/tasks/${taskId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user_id: userId }),
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleTaskError(error, taskId));
    })
    .catch((error) => console.error(error));
}

function deleteTask(taskId) {
  fetch(`/api/tasks/${taskId}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (response.ok) response.json().then(window.location.reload());
      else response.json().then((error) => handleTaskError(error, taskId));
    })
    .catch((error) => console.error(error));
}
