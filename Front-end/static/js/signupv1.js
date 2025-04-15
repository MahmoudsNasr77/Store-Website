document.getElementById('registerForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const form = e.target;

    const data = {
        username: form.username.value,
        email: form.email.value,
        phone_number: form.phone_number.value,
        city: form.city.value,
        country: form.country.value,
        password: form.password.value
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/accounts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById('registerResult').innerText = 'تم التسجيل بنجاح!';
            form.reset();
        } else {
            // Check for specific error codes and show a user-friendly message
            const errors = result.username || result.email;
            let errorMessage = 'حدث خطأ أثناء التسجيل';
            if (errors) {
                errorMessage = errors[0]; // This gets the first error message
            }
            document.getElementById('registerResult').innerText = errorMessage;
        }

    } catch (error) {
        document.getElementById('registerResult').innerText = 'فشل الاتصال بالخادم';
    }
});
