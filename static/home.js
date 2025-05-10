document.getElementById("language-toggle").addEventListener("click", function() {
    let isEnglish = document.body.dir === "ltr";

    if (isEnglish) {
        document.body.dir = "rtl";
        document.getElementById("home-link").innerText = "الرئيسية";
        document.getElementById("services-link").innerText = "الخدمات";
        document.getElementById("about-link").innerText = "عنّا";
        document.getElementById("login-link").innerText = "تسجيل الدخول";
        document.getElementById("welcome-text").innerText = "مرحبًا بك في مدير الصحة";
        document.getElementById("sub-text").innerText = "شريكك الموثوق لصحة أفضل";
        document.getElementById("cta-btn").innerText = "ابدأ الآن";
        this.innerText = "التبديل إلى الإنجليزية";
    } else {
        document.body.dir = "ltr";
        document.getElementById("home-link").innerText = "Home";
        document.getElementById("services-link").innerText = "Services";
        document.getElementById("about-link").innerText = "About Us";
        document.getElementById("login-link").innerText = "Login";
        document.getElementById("welcome-text").innerText = "Welcome to Health Director";
        document.getElementById("sub-text").innerText = "Your trusted partner for better healthcare";
        document.getElementById("cta-btn").innerText = "Get Started";
        this.innerText = "Switch to Arabic";
    }
});