// Toggle between English and Arabic when the links are clicked
document.getElementById('lang-en').addEventListener('click', function(e) {
    e.preventDefault();
    // Switch to English (LTR)
    document.documentElement.setAttribute('lang', 'en');
    document.documentElement.setAttribute('dir', 'ltr');
    // Update text content and placeholders to English
    document.getElementById('formTitle').textContent =
      document.getElementById('formTitle').getAttribute('data-en');
    document.getElementById('fullname').placeholder =
      document.getElementById('fullname').getAttribute('data-en');
    document.getElementById('email').placeholder =
      document.getElementById('email').getAttribute('data-en');
    document.getElementById('password').placeholder =
      document.getElementById('password').getAttribute('data-en');
    document.getElementById('confirm-password').placeholder =
      document.getElementById('confirm-password').getAttribute('data-en');
    document.getElementById('submitBtn').textContent =
      document.getElementById('submitBtn').getAttribute('data-en');
  });
  
  document.getElementById('lang-ar').addEventListener('click', function(e) {
    e.preventDefault();
    // Switch to Arabic (RTL)
    document.documentElement.setAttribute('lang', 'ar');
    document.documentElement.setAttribute('dir', 'rtl');
    // Update text content and placeholders to Arabic
    document.getElementById('formTitle').textContent =
      document.getElementById('formTitle').getAttribute('data-ar');
    document.getElementById('fullname').placeholder =
      document.getElementById('fullname').getAttribute('data-ar');
    document.getElementById('email').placeholder =
      document.getElementById('email').getAttribute('data-ar');
    document.getElementById('password').placeholder =
      document.getElementById('password').getAttribute('data-ar');
    document.getElementById('confirm-password').placeholder =
      document.getElementById('confirm-password').getAttribute('data-ar');
    document.getElementById('submitBtn').textContent =
      document.getElementById('submitBtn').getAttribute('data-ar');
  });