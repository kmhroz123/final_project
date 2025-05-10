document.getElementById('lang-en').addEventListener('click', function(e) {
    e.preventDefault();
    if (isEnglish) {
        document.body.dir = "rtl";
        document.getElementById("title").innerText = "مدير الصحة";
        document.getElementById("description").innerText = "أضف وصفًا";
        document.getElementById("login-title").innerText = "تسجيل الدخول";
        document.getElementById("email-label").innerText = "البريد الإلكتروني";
        document.getElementById("password-label").innerText = "كلمة المرور";
        document.getElementById("show-password-label").innerText = "عرض كلمة المرور";
        document.getElementById("sign-in-btn").innerText = "تسجيل الدخول";
        document.getElementById("forgot-link").innerText = "نسيت اسم المستخدم / كلمة المرور؟";
        document.getElementById("signup-link").innerText = "ليس لديك حساب؟ اشترك";
        this.innerText = "التبديل إلى الإنجليزية";
    } else {
        document.body.dir = "ltr";
        document.getElementById("title").innerText = "Health Director";
        document.getElementById("description").innerText = "Add a description";
        document.getElementById("login-title").innerText = "Login";
        document.getElementById("email-label").innerText = "Email";
        document.getElementById("password-label").innerText = "Password";
        document.getElementById("show-password-label").innerText = "Show Password";
        document.getElementById("sign-in-btn").innerText = "SIGN IN";
        document.getElementById("forgot-link").innerText = "Forgot Username / Password?";
        document.getElementById("signup-link").innerText = "Don't have an account? Sign up";
        this.innerText = "Switch to Arabic";
    }
});