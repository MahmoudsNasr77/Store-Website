document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const resultElement = document.getElementById("loginResult");

    const response = await fetch("http://127.0.0.1:8000/accounts/token/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("access_token", data.access);
        localStorage.setItem("refresh_token", data.refresh);
        resultElement.textContent = "تم تسجيل الدخول بنجاح!";
        resultElement.classList.remove("text-danger");
        resultElement.classList.add("text-success");
        window.location.href = "http://127.0.0.1:5000/";


        // Optional: redirect to home or dashboard
        // window.location.href = "/home/";
    } else {
        resultElement.textContent = "فشل تسجيل الدخول: " + (data.detail || "تحقق من البيانات.");
        resultElement.classList.remove("text-success");
        resultElement.classList.add("text-danger");
    }
});
