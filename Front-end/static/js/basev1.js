
    document.addEventListener("DOMContentLoaded", function () {
        const accessToken = localStorage.getItem("access_token");

        const loginBtn = document.getElementById("loginBtn");
        const signupBtn = document.getElementById("signupBtn");
        const logoutBtn = document.getElementById("logoutBtn");
        const addBtn = document.getElementById("addBtn");

        if (accessToken) {
            // المستخدم مسجل دخول
            loginBtn.classList.add("d-none");
            signupBtn.classList.add("d-none");
            logoutBtn.classList.remove("d-none");
            addBtn.classList.remove("d-none");

            logoutBtn.addEventListener("click", function (e) {
                e.preventDefault();
                localStorage.removeItem("access_token");
                localStorage.removeItem("refresh_token");
                window.location.href = "http://127.0.0.1:5000/login";
            });
        }
    });
    document.getElementById("logoutBtn").addEventListener("click", function (e) {
        e.preventDefault();
    
        // Remove JWT tokens from localStorage
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
    
        // Redirect to the login page (or any other page)
        window.location.href = "http://127.0.0.1:5000/login";
    });
    document.addEventListener("DOMContentLoaded", function () {
        const accessToken = localStorage.getItem("access_token");

        const logoutBtn = document.getElementById("logoutBtn");

        if (accessToken) {
            // If user is authenticated, show logout button
            logoutBtn.classList.remove("d-none");
        } else {
            // If user is not authenticated, hide logout button
            logoutBtn.classList.add("d-none");
        }
    });

   