document.getElementById("addProductForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = document.getElementById("addProductForm");
    const formData = new FormData(form); // ده بياخد كل الـ inputs تلقائيًا حتى الصورة
    console.log("📦 Sending form data...");
    console.log(formData.get("name"));
    console.log(formData.get("image"));
    

    try {
        const response = await fetch("http://127.0.0.1:8000/api/add_product", {
            method: "POST",
            body: formData,  // بدون headers!
        });

        const data = await response.json();

        if (response.ok) {
            alert("✅ تم إضافة المنتج بنجاح");
            window.location.href = "/";  // أو أي صفحة تانية تحب توديه عليها
        } else {
            console.error(data);
            alert("❌ خطأ في إضافة المنتج: " + (data.detail || "راجع البيانات"));
        }
    } catch (error) {
        console.error("Fetch error:", error);
        alert("⚠️ حدث خطأ أثناء الاتصال بالسيرفر.");
    }
});
