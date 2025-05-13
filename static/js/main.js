document.addEventListener('DOMContentLoaded', function() {
    // Pronunciation toggle
    const pronunciationLink = document.getElementById('pronunciation-link');
    const pronunciationText = document.getElementById('pronunciation-text');
    
    if (pronunciationLink && pronunciationText) {
        pronunciationLink.addEventListener('click', function(e) {
            e.preventDefault();
            if (pronunciationText.style.display === 'none') {
                pronunciationText.style.display = 'block';
            } else {
                pronunciationText.style.display = 'none';
            }
        });
    }
    
    // Image gallery on art page
    const artworkItems = document.querySelectorAll('.artwork-item');
    
    artworkItems.forEach(function(item) {
        item.addEventListener('click', function() {
            const img = this.querySelector('img');
            if (img) {
                // Simple lightbox effect
                const overlay = document.createElement('div');
                overlay.className = 'lightbox-overlay';
                
                const enlargedImg = document.createElement('img');
                enlargedImg.src = img.src;
                enlargedImg.className = 'lightbox-image';
                
                overlay.appendChild(enlargedImg);
                document.body.appendChild(overlay);
                
                overlay.addEventListener('click', function() {
                    document.body.removeChild(overlay);
                });
            }
        });
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.getAttribute('href').length > 1) { // Ignore single # links
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}); 