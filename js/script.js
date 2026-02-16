document.addEventListener('DOMContentLoaded', () => {
    fetchPublications();
});

async function fetchPublications() {
    const listElement = document.getElementById('publication-list');

    try {
        const response = await fetch('data/publications.json');
        if (!response.ok) throw new Error('Failed to load publications');

        const publications = await response.json();

        if (publications.length === 0) {
            listElement.innerHTML = '<li>No publications found or data is being generated. Check back later.</li>';
            return;
        }

        listElement.innerHTML = ''; // Clear loading text

        publications.forEach(pub => {
            const li = document.createElement('li');
            li.className = 'publication-item';

            // Highlight current author
            const authors = pub.authors.replace(/Frida Snilstveit Hoem|F\. S\. Hoem|Hoem, F\. S\.|Hoem, Frida Snilstveit/gi,
                '<span class="highlight-author">$&</span>');

            let links = '';
            if (pub.url) links += `<a href="${pub.url}" target="_blank">[Link]</a> `;
            if (pub.eprint_url) links += `<a href="${pub.eprint_url}" target="_blank">[PDF]</a>`;

            const titleHtml = pub.url ? `<a href="${pub.url}" target="_blank" class="pub-title-link">${pub.title}</a>` : pub.title;

            li.innerHTML = `
                <div class="pub-title">${titleHtml}</div>
                <div class="pub-authors">${authors}</div>
                <div class="pub-venue">${pub.venue} (${pub.year})</div>
                <div class="pub-links">${links}</div>
            `;

            listElement.appendChild(li);
        });

    } catch (error) {
        console.error('Error:', error);
        listElement.innerHTML = '<li>Error loading publications.</li>';
    }
}
