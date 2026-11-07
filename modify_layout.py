import re

with open('aman-malviya-portfolio/src/layouts/Layout.astro', 'r') as f:
    content = f.read()

script = """
		<script>
			document.addEventListener("DOMContentLoaded", function() {
				const sections = document.querySelectorAll('.section, .hero, .impact-section');
				sections.forEach(sec => sec.classList.add('fade-in-section'));

				const observer = new IntersectionObserver((entries, observer) => {
					entries.forEach(entry => {
						if (entry.isIntersecting) {
							entry.target.classList.add('is-visible');
							observer.unobserve(entry.target);
						}
					});
				}, { threshold: 0.1 });

				sections.forEach(section => {
					observer.observe(section);
				});
			});
		</script>
	</body>
"""

content = content.replace('\t</body>', script)

with open('aman-malviya-portfolio/src/layouts/Layout.astro', 'w') as f:
    f.write(content)
