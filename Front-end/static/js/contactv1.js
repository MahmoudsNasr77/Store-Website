document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', async function (e) {
            e.preventDefault();

            const form = e.target;
            const data = {
                name: form.name.value,
                email: form.email.value,
                message: form.message.value
            };

            try {
                const response = await fetch('http://127.0.0.1:8000/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                const resultDiv = document.getElementById('result');

                if (response.ok) {
                    resultDiv.innerText = 'تم إرسال الرسالة بنجاح!';
                    resultDiv.className = 'alert alert-success mt-3';
                    form.reset();
                } else {
                    resultDiv.innerText = 'حدث خطأ: ' + (result.detail || 'تحقق من البيانات');
                    resultDiv.className = 'alert alert-danger mt-3';
                }

            } catch (error) {
                document.getElementById('result').innerText = 'فشل الاتصال بالخادم.';
                resultDiv.className = 'alert alert-danger mt-3';
            }
        });
    }
});

