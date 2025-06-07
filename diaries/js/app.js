// static/diaries/js/app.js

document.addEventListener('DOMContentLoaded', () => {
    // helper: デバウンス
    function debounce(fn, delay = 300) {
        let timer = null;
        return (...args) => {
            clearTimeout(timer);
            timer = setTimeout(() => fn(...args), delay);
        };
    }

    // 1. Live Markdown Preview
    const mdTextarea = document.getElementById('id_body_md');
    const mdPreview  = document.getElementById('markdown-preview');
    if (mdTextarea && mdPreview && window.marked) {
        const updatePreview = () => {
            mdPreview.innerHTML = marked.parse(mdTextarea.value);
        };
        mdTextarea.addEventListener('input', debounce(updatePreview, 300));
        updatePreview();
    }

    // 2. Image Preview
    const imgInput   = document.getElementById('id_cover_image');
    const imgPreview = document.getElementById('image-preview');
    if (imgInput && imgPreview) {
        imgInput.addEventListener('change', () => {
            const file = imgInput.files[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = e => {
                    imgPreview.src = e.target.result;
                    imgPreview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // 3. Unsaved Changes Warning
    let formChanged = false;
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('change', () => { formChanged = true; });
        window.addEventListener('beforeunload', e => {
            if (formChanged) {
                e.preventDefault();
                e.returnValue = '';
            }
        });
        form.addEventListener('submit', () => { formChanged = false; });
    }
});
